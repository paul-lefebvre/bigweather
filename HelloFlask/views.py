#IMPORTS
import json
import requests
import http.client
import time
import threading
from flask_mysqldb import MySQL
from flask_restplus import Resource, Api
from random import randint
from datetime import datetime, timedelta
import locale
locale.setlocale(locale.LC_TIME,'')
from flask import render_template, request, jsonify
from HelloFlask import app, socketio
from flask_socketio import SocketIO, emit, send
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
#-------------------------------------------------


#THREADS
thread = threading.Thread()
thread_stop_event = threading.Event()
#-------------------------------------------------



#--------------[BDD : CONNEXION]--------------
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_HOST'] =  '127.0.0.1'
app.config['MYSQL_DB'] = 'bigweather'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)
#-------------------------------------------------



#--------------------------------------------------[API : OPEN WEATHER MAP]--------------------------------------------------------

#parametres opeanweathermap
import pyowm
owm = pyowm.OWM('651994a64b35edd82f4b84e240ba4a54')
fc = owm.three_hours_forecast('Rouen,fr') 

#f = forecast --> prévision
f = fc.get_forecast()   
list_f = f.get_weathers()

#parametres 
params = {
  'access_key': 'b04076c48780952121ea136db5362ab5',
  'query': 'Rouen'
}

#Requête vers l'api
api_result = requests.get('http://api.weatherstack.com/current', params)

#Conversion vers format json
api_response = api_result.json()



#AFFICHAGE DES CURRENTS
print(u'Température actuelle à %s est de : %d℃ | Taux de humidité : %d%%' % (api_response['location']['name'], api_response['current']['temperature'], api_response['current']['humidity']))
print(u'Lien de l\'icone weather : %s' % (api_response['current']['weather_icons']))

#AFFICHAGE DES FORECAST
i = 1
table_prevision_temp = ['prev1', 'prev2','prev3','prev4','prev5']
index = 0
for weather in f:
    datefc = weather.get_reference_time(timeformat='date')
    formatted_datefc = datefc.strftime("%A %d %B")
    if i==10 or i==18 or i==26 or i==34 or i==40:
        print ('Date de prévision n°%d : %s' % (i, formatted_datefc))
        print('Status du jour : %s' % (weather.get_status()))
        print('Température prévue : %s°C' % (weather.get_temperature(unit='celsius')['temp']))
        table_prevision_temp[index] = weather.get_temperature(unit='celsius')['temp']
        index += 1
    i += 1
#---------------------------------------------------------------------------------------------------------







#----------------------------------------[PREVISIONS REAL-TIME]----------------------------------------------

#génération des 5 prochaines dates à partir d'aujourd'hui
date_aujourdhui = datetime.now()
aujourdhui = date_aujourdhui.day
increm_date = 0
table_prevision_date = [0, 0, 0, 0, 0]
aujourdhui += 1
while increm_date < 5:
    table_prevision_date[increm_date] = aujourdhui
    print("Dates : %d" % (table_prevision_date[increm_date]))
    increm_date += 1
    aujourdhui += 1

print("dates de prévision crées !")

class PrevSemaineThread(threading.Thread):
    def __init__(self):
        self.delay = 10800
        super(PrevSemaineThread, self).__init__()
    def PrevSemaineUpdater(self):
        #Boucle de 3 heures --> pour actualiser la température de prévision [CHART]
        logger.info("[API_WEATHER] > Création des prévisions de température")
        while not thread_stop_event.isSet():
            prevSemaineTemp = table_prevision_temp[0]
            prevSemaineDate = table_prevision_date[0]
            socketio.emit('newprevsemaine1', {'prevsemaine1': prevSemaineTemp}, namespace='/')
            socketio.emit('newprevdate1', {'prevdate1': prevSemaineDate}, namespace='/')
            prevSemaineTemp = table_prevision_temp[1]
            prevSemaineDate = table_prevision_date[1]
            socketio.emit('newprevsemaine2', {'prevsemaine2': prevSemaineTemp}, namespace='/')
            socketio.emit('newprevdate2', {'prevdate2': prevSemaineDate}, namespace='/')
            prevSemaineTemp = table_prevision_temp[2]
            prevSemaineDate = table_prevision_date[2]
            socketio.emit('newprevsemaine3', {'prevsemaine3': prevSemaineTemp}, namespace='/')
            socketio.emit('newprevdate3', {'prevdate3': prevSemaineDate}, namespace='/')
            prevSemaineTemp = table_prevision_temp[3]
            prevSemaineDate = table_prevision_date[3]
            socketio.emit('newprevsemaine4', {'prevsemaine4': prevSemaineTemp}, namespace='/')
            socketio.emit('newprevdate4', {'prevdate4': prevSemaineDate}, namespace='/')
            prevSemaineTemp = table_prevision_temp[4]
            prevSemaineDate = table_prevision_date[4]
            socketio.emit('newprevsemaine5', {'prevsemaine5': prevSemaineTemp}, namespace='/')
            socketio.emit('newprevdate5', {'prevdate5': prevSemaineDate}, namespace='/')
            time.sleep(self.delay)
    def run(self):
        self.PrevSemaineUpdater()
#-----------------------------------------------------------------------------------------------------

#----------------------------------------[MESURES TEMPS REEL]------------------------------------------
class PressionLiveThread(threading.Thread):
    def __init__(self):
        self.delay = 60
        super(PressionLiveThread, self).__init__()
    def PressLiveUpdater(self):
        #Boucle de 1min pour actualiser le taux d'humidité actuelle
        logger.info("[API_WEATHER] > Création du taux de pression en live")
        while not thread_stop_event.isSet():
            pressionlive = api_response['current']['pressure']
            socketio.emit('newpression', {'pression': pressionlive}, namespace='/')
            time.sleep(self.delay)
    def run(self):
        self.PressLiveUpdater()

#-------------------------------------------------------------------------------------------------------

#----------------------------------------[LOGO WEATHER]-------------------------------------------------
class LogoLiveThread(threading.Thread):
    def __init__(self):
        self.delay = 360
        super(LogoLiveThread, self).__init__()
    def LogoLiveUpdater(self):
        #Boucle de 6min pour actualiser l'icone de temps
        logger.info("[API_WEATHER] > Création de l'icon weather en live")
        while not thread_stop_event.isSet():
            iconLiveList = api_response['current']['weather_icons']
            iconLive = ''.join(iconLiveList)
            socketio.emit('newicon', {'icon': iconLive}, namespace='/')
            print(iconLive)
            time.sleep(self.delay)
    def run(self):
        self.LogoLiveUpdater()
#-------------------------------------------------------------------------------------------------------

#------------------------------------------[HORLOGE]----------------------------------------------------
class TimeThread(threading.Thread):
    def __init__(self):
        self.delay = 1
        super(TimeThread, self).__init__()
    def randomNumberGenerator(self):
        #Boucle de 1s pour actualiser l'horloge
        logger.info("[WEBUI] > Création de l'horloge")
        while not thread_stop_event.isSet():
            timenow = datetime.now()
            formatted_time = timenow.strftime("%H:%M")
            number = formatted_time
            socketio.emit('newnumber', {'number': number}, namespace='/')
            time.sleep(self.delay)
    def run(self):
        self.randomNumberGenerator()
#-------------------------------------------------------------------------------------------------------

#----------------------------[LANCEMENT DE LA PAGE HTML]------------------------------------------------

@app.route('/')
def home():
    return render_template(
        "login.php")

@app.route('/dashboard/station/')
def logged():
    #DATE ET HEURE
    datenow = datetime.now()
    formatted_date = datenow.strftime("%A %d %B")

    #REQUETE SQL DES DONNEES ENREGISTRES
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM t_donnee''')
    results = cur.fetchall()


    #-------------[TEMPERATURES SQL]-----------------
    tempUn = str(results[0]['DONTEMPERATURE'])
    socketio.emit('tempSqlUn', {'temp': tempUn}, namespace='/')
    #tempSecond = str(results[1]['DONTEMPERATURE'])
    #tempThird = str(results[2]['DONTEMPERATURE'])


    return render_template(
        "index.html",
        date = formatted_date)

#----------------------------[POST DES DONNEES]------------------------------------------------
@app.route('/api/mesure/add/1/<temp>+<humidity>', methods=['POST'])
def mesure(temp, humidity):
    values = {'temp': temp, 'humidity': humidity}
    print(temp)
    print(humidity)
    socketio.emit('newtempsensor', {'temp': temp}, namespace='/')
    socketio.emit('newhumidity', {'humidity': humidity}, namespace='/')
    return values, 201
#-------------------------------------------------------------------------------------------------------

#-----------------------------[CONNEXION ET DEMARRAGE DES THREADS]--------------------------------------
@socketio.on('connect')
def test_connect():
    global thread
    print('client connecte')
    emit('my response', {'data': 'Connected'})
    if not thread.isAlive():
        print("[WEBUI] > Démarrage des Threads")
        #Démarrage du thread de prévision des températures
        thread_TemperaturePrevue = PrevSemaineThread()
        thread_TemperaturePrevue.start()
        #Démarrage du thread de la pression actuelle
        thread_pressionActuelle = PressionLiveThread()
        thread_pressionActuelle.start()
        #Démarrage du thread du logo de temps
        thread_iconweather = LogoLiveThread()
        thread_iconweather.start()
        #Démarrage du thread de l'horloge
        thread_clock = TimeThread()
        thread_clock.start()
#---------------------------------------------------------------------------------------------------------

#----------------------------------------[DECONNEXION]----------------------------------------------------
@socketio.on('disconnect')
def test_disconnect():
    print('Client deconnecte')
#---------------------------------------------------------------------------------------------------------