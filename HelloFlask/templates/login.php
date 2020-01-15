<!doctype html>
<html lang="fr">
  <head>
    <title>BigWeather</title>
    <!-- Meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    
    <link rel="shortcut icon" href="{{ url_for('static',filename='favicon.ico') }}" />
    <link rel="icon" type="image/x-icon" href="{{ url_for('static',filename='favicon.ico') }}" />
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <link rel= "stylesheet" type= "text/css" href= "{{ url_for('static',filename='login/login.css') }}">
    </head>
  <body>


    <div>
        <section class="background">
          <div class="content-wrapper">
            <p class="content-title">Big Weather</p>
            <p class="content-subtitle">votre station météo partout</p>
          </div>
        </section>
        <section class="background">
            <div class="content-wrapper">

                <br><br>
                <!--FORECAST-->
                <div class="forecast-container container">
                    <div class="today forecast">
                        <div class="forecast-header">
                            <div class="day">Lundi</div>
                            <div class="date">13 Janvier</div>
                        </div> <!-- .forecast-header -->
                        <div class="forecast-content">
                            <div class="location">Rouen</div>
                            <div class="degree">
                                <div class="num">23<sup>°</sup>C</div>
                                <div class="forecast-icon">
                                    <img src="{{ url_for('static',filename='login/images/icons/icon-1.svg') }}" alt="" width=90>
                                </div>	
                            </div>
                            <span><img src="{{ url_for('static',filename='login/images/icon-umberella.png') }}" alt="">76%</span>
                            <span><img src="{{ url_for('static',filename='login/images/icon-wind.png') }}" alt="">12km/h</span>
                            <span><img src="{{ url_for('static',filename='login/images/icon-compass.png') }}" alt="">Ouest</span>
                        </div>
                    </div>
                    <div class="forecast">
                        <div class="forecast-header">
                            <div class="day">Mardi</div>
                        </div> <!-- .forecast-header -->
                        <div class="forecast-content">
                            <div class="forecast-icon">
                                <img src="{{ url_for('static',filename='login/images/icons/icon-3.svg') }}" alt="" width=48>
                            </div>
                            <div class="degree">23<sup>°</sup>C</div>
                            <small>18<sup>°</sup></small>
                        </div>
                    </div>
                    <div class="forecast">
                        <div class="forecast-header">
                            <div class="day">Mercredi</div>
                        </div> <!-- .forecast-header -->
                        <div class="forecast-content">
                            <div class="forecast-icon">
                                <img src="{{ url_for('static',filename='login/images/icons/icon-5.svg') }}" alt="" width=48>
                            </div>
                            <div class="degree">23<sup>°</sup>C</div>
                            <small>18<sup>°</sup></small>
                        </div>
                    </div>
                    <div class="forecast">
                        <div class="forecast-header">
                            <div class="day">Jeudi</div>
                        </div> <!-- .forecast-header -->
                        <div class="forecast-content">
                            <div class="forecast-icon">
                                <img src="{{ url_for('static',filename='login/images/icons/icon-7.svg') }}" alt="" width=48>
                            </div>
                            <div class="degree">23<sup>°</sup>C</div>
                            <small>18<sup>°</sup></small>
                        </div>
                    </div>
                    <div class="forecast">
                        <div class="forecast-header">
                            <div class="day">Vendredi</div>
                        </div> <!-- .forecast-header -->
                        <div class="forecast-content">
                            <div class="forecast-icon">
                                <img src="{{ url_for('static',filename='login/images/icons/icon-12.svg') }}" alt="" width=48>
                            </div>
                            <div class="degree">23<sup>°</sup>C</div>
                            <small>18<sup>°</sup></small>
                        </div>
                    </div>
                    <div class="forecast">
                        <div class="forecast-header">
                            <div class="day">Samedi</div>
                        </div> <!-- .forecast-header -->
                        <div class="forecast-content">
                            <div class="forecast-icon">
                                <img src="{{ url_for('static',filename='login/images/icons/icon-13.svg') }}" alt="" width=48>
                            </div>
                            <div class="degree">23<sup>°</sup>C</div>
                            <small>18<sup>°</sup></small>
                        </div>
                    </div>
                    <div class="forecast">
                        <div class="forecast-header">
                            <div class="day">Dimanche</div>
                        </div> <!-- .forecast-header -->
                        <div class="forecast-content">
                            <div class="forecast-icon">
                                <img src="{{ url_for('static',filename='login/images/icons/icon-8.svg') }}" alt="" width=48>
                            </div>
                            <div class="degree">23<sup>°</sup>C</div>
                            <small>18<sup>°</sup></small>
                        </div>
                    </div>
                </div>






            </div>
        </section>
        <section class="background d-flex justify-content-center">
          <div class="content-wrapper w-75 p-3">

            <!--FORMULAIRE-->
            <form method="POST" action="/">
            <div id="signin">
            <button class="btn panel bg-secondary" style="left: 0;" type="button" data-toggle="collapse" data-target="#loginCollapse1" aria-expanded="true" aria-controls="loginCollapse1">Connexion</button>
            <button class="btn panel" style="right: 0;" type="button" data-toggle="collapse" data-target="#inscriptionCollapse2" aria-expanded="false" aria-controls="inscriptionCollapse2">Inscription</button>
                <div class="collapse show" id="loginCollapse1" data-parent="#signin">
                    <div class="form-title"><strong>BigWeather</strong> - Tableau de bord</div>
                    <img src="{{ url_for('static',filename='login/images/icons/icon-13.svg') }}" width=130 class="rounded float-middle" alt="Logo BigWeather">
                    <div class="input-field">
                        {{ inputUsernameForm }}
                        <i><img src="{{ url_for('static',filename='login/images/icons/icon-8.svg') }}" class="material-icons" width=27></i>
                        <label for="email">Nom de compte {{ usernameIncorrect }}</label>
                    </div>
                    <div class="input-field">
                        {{ inputPasswordForm }}
                        <i><img src="{{ url_for('static',filename='login/images/icons/icon-8.svg') }}" class="material-icons" width=27></i>
                        <label for="password">Mot de passe {{ passwordIncorrect }}</label>
                    </div>
                    <div class="check">
                        <i><img src="{{ url_for('static',filename='login/images/icons/icon-12.svg') }}" class="material-icons" width=200><h4>Authentification...</h4></i>
                    </div>
                </div>

                <div class="collapse" id="inscriptionCollapse2" data-parent="#signin">
                    <h6>Terminez votre inscription et accédez à <strong>BigWeather</strong></h2>
                    <br><br>
                    <div class="input-group sm-3">
                        <div class="input-group-prepend">
                            <span class="input-group-text" id="basic-addon1">💡</span>
                        </div>
                        <input type="text" class="form-control" placeholder="Nom de compte" aria-label="NomDeCompte" aria-describedby="basic-addon1">
                    </div>
                    <br><br>
                    <div class="input-group sm-3">
                        <div class="input-group-prepend">
                            <span class="input-group-text" id="">🔒</span>
                        </div>
                        <input type="text" class="form-control" placeholder="Mot de passe">
                        <input type="text" class="form-control" placeholder="Confirmez votre mot de passe">
                    </div>
                    <br>
                    <div class="input-group sm-3">
                        <div class="input-group-prepend">
                            <label class="input-group-text" for="inputGroupSelect01">🛠</label>
                        </div>
                        <select class="custom-select" id="inputGroupSelect01">
                            <option selected>Modèle de votre station</option>
                            <option value="1">Standard-Weather</option>
                            <option value="2">Big-Weather</option>
                            <option value="3">Big-Weather Cloud</option>
                        </select>
                    </div>

                </div>
                <button class="login" type="submit">C'est parti 💨</button>

            </div>
            </form>
            <!--FIN FORMULAIRE-->
            
          </div>
        </section>
      </div>











    <!-- jQuery & Bootstrap -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/lodash.js/3.10.1/lodash.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/1.20.3/TweenMax.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/1.12.1/plugins/CSSRulePlugin.min.js"></script>
    <script src="{{ url_for('static',filename='login/dist/jquery.js') }}"></script>
    <script src="{{ url_for('static',filename='login/login.js') }}"></script>
    <?php include('connectdb.php') ?>


  </body>
</html>