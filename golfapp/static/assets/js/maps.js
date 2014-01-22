
function initialize() {
	var myLatlng = new google.maps.LatLng(37.790, -122.401);

    var mapOptions = {
      center: myLatlng,
      zoom: 12,
      mapTypeId: google.maps.MapTypeId.ROADMAP
    };

    var map = new google.maps.Map(document.getElementById("map"),
      mapOptions);

    var marker = new google.maps.Marker({
      position: myLatlng,
      map: map,
      title: "RocketSpace's Offices!"
    });

	    var contentString = '<div id="content">'+
			'<div id="siteNotice">'+
			'</div>'+
			'<h1 id="firstHeading" class="firstHeading">Don and Rory Residence</h1>'+
			'<div id="bodyContent">'+
			'<p><b>80 Cayuga</b>, also referred to as <b>Ayers Rock</b>, is a large ' +
			'sandstone rock formation in the southern part of the '+
			'Northern Territory, central Australia. It lies 335&#160;km (208&#160;mi) '+
			'south west of the nearest large town, Alice Springs; 450&#160;km '+
			'(280&#160;mi) by road. Kata Tjuta and Uluru are the two major '+
			'features of the Uluru - Kata Tjuta National Park. Uluru is '+
			'sacred to the Pitjantjatjara and Yankunytjatjara, the '+
			'Aboriginal people of the area. It has many springs, waterholes, '+
			'rock caves and ancient paintings. Uluru is listed as a World '+
			'Heritage Site.</p>'+
			'<p>Attribution: Uluru, <a href="http://en.wikipedia.org/w/index.php?title=Uluru&oldid=297882194">'+
			'http://en.wikipedia.org/w/index.php?title=Uluru</a> '+
			'(last visited June 22, 2009).</p>'+
			'</div>'+
			'</div>';

  		var infowindow = new google.maps.InfoWindow({
      	content: contentString
  		});

  		var marker = new google.maps.Marker({
		position: myLatlng,
		map: map,
		title: 'Uluru (Ayers Rock)'
		});
  		
  		google.maps.event.addListener(marker, 'click', function() {
    		infowindow.open(map,marker);
  });
}

google.maps.event.addDomListener(window, 'load', initialize);









