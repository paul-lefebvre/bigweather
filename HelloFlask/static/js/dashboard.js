
//fonction sleep(time)
const sleep = (milliseconds) => {
  return new Promise(resolve => setTimeout(resolve, milliseconds))
}


//-----------------------------------[AFFICHAGE DE LA PAGE ACCUEIL DESKTOP]--------------------------------------
$( document ).ready(function() {
  $('*').removeClass("active");  
  $('#date').addClass("active");
  $('#mesures').addClass("active");
  //scrollbar
  document.body.style.overflow = 'visible';
  //Mesures
  var pageMesureDisplay = document.getElementById("pageMesures");
  var pageMesureChartDisplay = document.getElementById("pageMesures-chart");
  //Cartographie
  var pageMapDisplay = document.getElementById("pageMap");
  pageMesureDisplay.style.display = "block";
  pageMesureChartDisplay.style.display = "block";
  pageMapDisplay.style.display = "none";
});
//-----------------------------------------------------------------------------------------------------







//-----------------------------------[AFFICHAGE DE LA PAGE MESURES]--------------------------------------
function pageMesures() {
  if($('#mesures').hasClass('active')){
    console.log('Action impossible...');
  }else{
    $('*').removeClass("active");  
    $('#date').addClass("active");
    $('#mesures').addClass("active");
    //scrollbar
    document.body.style.overflow = 'visible';
    //Mesures
    var pageMesureDisplay = document.getElementById("pageMesures");
    var pageMesureChartDisplay = document.getElementById("pageMesures-chart");
    //Cartographie
    var pageMapDisplay = document.getElementById("pageMap");
    // API
    var pageApiDisplay = document.getElementById("pageApi");
    //AFFICHAGE
    pageMesureDisplay.style.display = "block";
    pageMesureChartDisplay.style.display = "block";
    pageMapDisplay.style.display = "none";
    pageApiDisplay.style.display = "none";
  }
}
//-----------------------------------------------------------------------------------------------------



//-----------------------------------[AFFICHAGE DE LA PAGE CARTOGRAPHIE]-------------------------------
function pageMap() {
  if($('#carte').hasClass('active')){
    console.log('Action impossible...');
  }else{
    $('*').removeClass("active");  
    $('#date').addClass("active");
    $('#carte').addClass("active");
    //scrollbar
    document.body.style.overflow = 'hidden';
    //mesures
    var pageMesureDisplay = document.getElementById("pageMesures");
    var pageMesureChartDisplay = document.getElementById("pageMesures-chart");
    //Cartographie
    var pageMapDisplay = document.getElementById("pageMap");
    // API
    var pageApiDisplay = document.getElementById("pageApi");
    //AFFICHAGE
    pageMesureDisplay.style.display = "none";
    pageMesureChartDisplay.style.display = "none";
    pageMapDisplay.style.display = "block";
    pageApiDisplay.style.display = "none";
  }
}


//-----------------------------------[AFFICHAGE DE LA PAGE API]-------------------------------
function pageApi() {
  if($('#api').hasClass('active')){
    console.log('Action impossible...');
  }else{
    $('*').removeClass("active");  
    $('#date').addClass("active");
    $('#api').addClass("active");
    //scrollbar
    document.body.style.overflow = 'hidden';
    //mesures
    var pageMesureDisplay = document.getElementById("pageApi");
    var pageMesureChartDisplay = document.getElementById("pageApi-chart");
    //Cartographie
    var pageMapDisplay = document.getElementById("pageMap");
    // API
    var pageApiDisplay = document.getElementById("pageApi");
    //AFFICHAGE
    pageMesureDisplay.style.display = "none";
    pageMesureChartDisplay.style.display = "none";
    pageMapDisplay.style.display = "none";
    pageApiDisplay.style.display = "block";
  }
}