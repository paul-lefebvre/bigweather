$(document).ready(function() {

  var socket = io.connect('http://127.0.0.1:8080');

  socket.on('connect', function(){
    socket.emit('[WEBUI] > Utilisateur Connecté');

  });

  //fonction de suppression des loaders (spinners b4)
  function removeTempSpinner() {
    var elem = document.getElementById('tempLoader');
    elem.style.display = "none";

  }
  function removeHumidSpinner() {
    var elemd = document.getElementById('humidLoader');
    elemd.style.display = "none";

  }
  function removePressSpinner() {
    var elemp = document.getElementById('pressLoader');
    elemp.style.display = "none";

  }

  //-----------------[TIME]------------------------
  var numbers_received = [];
    //détail du server
    socket.on('newnumber', function(msg) {
        console.log("[WEBUI] > Heure : " + msg.number);
        //maintien de l'horloge
        if (numbers_received.length >= 1){
            numbers_received.shift()
        }
        numbers_received.push(msg.number);
        clock_string = '';
        for (var i = 0; i < numbers_received.length; i++){
          clock_string = numbers_received[i].toString();
        }
        $('#time').html(clock_string);

      });



        //-----------[TEMPERATURE ACTUELLE]--------------
  var temp_received = [];
  //détail du server
  socket.on('newtempsensor', function(msg) {
      console.log("[WEBUI] > Température : " + msg.temp);
      //maintien de l'horloge
      if (temp_received.length >= 1){
        temp_received.shift()
      }
      temp_received.push(msg.temp);
      tempLive_string = '';
      for (var i = 0; i < temp_received.length; i++){
        tempLive_string = temp_received[i].toString();
      }
      tempLive_string += '°C';
      removeTempSpinner();
      $('#tempLive').html(tempLive_string);

    });

            //-----------[HUMIDITE ACTUELLE]--------------
  var humid_received = [];
  //détail du server
  socket.on('newhumidity', function(msg) {
      console.log("[WEBUI] > Humidité : " + msg.humidity);
      //maintien de l'horloge
      if (humid_received.length >= 1){
        humid_received.shift()
      }
      humid_received.push(msg.humidity);
      humidLive_string = '';
      for (var i = 0; i < humid_received.length; i++){
        humidLive_string = humid_received[i].toString();
      }
      humidLive_string += '%';
      removeHumidSpinner();
      $('#humidLive').html(humidLive_string);

    });

                //-----------[PRESSION ACTUELLE]--------------
  var press_received = [];
  //détail du server
  socket.on('newpression', function(msg) {
      console.log("[WEBUI] > Pression : " + msg.pression);
      //maintien de l'horloge
      if (press_received.length >= 1){
        press_received.shift()
      }
      press_received.push(msg.pression);
      pressLive_string = '';
      for (var i = 0; i < press_received.length; i++){
        pressLive_string = press_received[i].toString();
      }
      pressLive_string += ' hPa';
      removePressSpinner();
      $('#pressLive').html(pressLive_string);
    });


});









//Include des pages HTML --> programmation modulaire
function includeHTML() {
  var z, i, elmnt, file, xhttp;
  /* Loop through a collection of all HTML elements: */
  z = document.getElementsByTagName("*");
  for (i = 0; i < z.length; i++) {
    elmnt = z[i];
    /*search for elements with a certain atrribute:*/
    file = elmnt.getAttribute("w3-include-html");
    if (file) {
      /* Make an HTTP request using the attribute value as the file name: */
      xhttp = new XMLHttpRequest();
      xhttp.onreadystatechange = function() {
        if (this.readyState == 4) {
          if (this.status == 200) {elmnt.innerHTML = this.responseText;}
          if (this.status == 404) {elmnt.innerHTML = "Page introuvable...";}
          /* Remove the attribute, and call this function once more: */
          elmnt.removeAttribute("w3-include-html");
          includeHTML();
        }
      }
      xhttp.open("GET", file, true);
      xhttp.send();
      /* Exit the function: */
      return;
    }
  }
}

