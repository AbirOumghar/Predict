function onClickedEstimatePrice() {
  console.log("Estimate price button clicked");
  var puissance_electrique_maximale_appelee_en_KVA = document.getElementById("uiPuissance_electrique_maximale_appelee_en_KVA");
  var moyenne_saisonniere = document.getElementById("uiMoyenne_saisonniere");
  var mois = document.getElementById("uiMoiss");
  var estPrice = document.getElementById("uiEstimatedPrice");

  // var url = "http://127.0.0.1:5000/predict_home_price"; //Use this if you are NOT using nginx which is first 7 tutorials
  var url = "http://127.0.0.1:5000/predict_pruissance"; // Use this if  you are using nginx. i.e tutorial 8 and onwards

  $.post(url, {
      puissance_electrique_maximale_appelee_en_KVA: parseFloat(puissance_electrique_maximale_appelee_en_KVA.value),
      moyenne_saisonniere: parseFloat(moyenne_saisonniere.value),
      mois: mois.value
  },function(data, status) {
      console.log(data.estimated_price);
      estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " </h2>";
      console.log(status);
  });
}

function onPageLoad() {
  console.log( "document loaded" );
  // var url = "http://127.0.0.1:5000/get_location_names"; // Use this if you are NOT using nginx which is first 7 tutorials
  var url = "http://127.0.0.1:5000/get_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
  $.get(url,function(data, status) {
      console.log("got response for get_location_names request");
      if(data) {
          var moiss = data.moiss;
          var uiMoiss = document.getElementById("uiMoiss");
          $('#uiMoiss').empty();
          for(var i in moiss) {
              var opt = new Option(moiss[i]);
              $('#uiMoiss').append(opt);
          }
      }
  });
}

window.onload = onPageLoad;
