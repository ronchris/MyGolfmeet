
function initialize() {
	var myLatlng = new google.maps.LatLng(37.723, -122.494);

    var mapOptions = {
      center: myLatlng,
      zoom: 14,
      mapTypeId: google.maps.MapTypeId.ROADMAP
    };

    var map = new google.maps.Map(document.getElementById("map"),
      mapOptions);

    var marker = new google.maps.Marker({
      position: myLatlng,
      map: map,
      title: "Harding Park!"
    });

	    var contentString = '<div id="content">'+
			'<div id="siteNotice">'+
			'</div>'+
			'<h1 id="firstHeading" class="firstHeading">Harding Park Golf Course</h1>'+
			'<div id="bodyContent">'+
			'<p><b>TPC Harding Park</b>, formerly Harding Park Golf Club and commonly known as Harding Park</b>, is a municipal golf course ' +
			'located in the heart of Lake Merced, owned by the city and county of San Francisco. <br>'+
			'<b>Address: 99 Harding Rd, San Francisco, CA 94132</b><br> '+
			'<b>Phone: (415) 664-4690</b></p>' +
			'</div>'+ '<br><p><b>Book a GOLFMEETING!</b></p>' + '<a href="http://www.tpc.com/tpc/courses/tpc.asp?id=7&page=86" target="_blank">www.tpc.com/hardingpark‎</a> ' +
			'</div>';

  		var infowindow = new google.maps.InfoWindow({
      	content: contentString
  		});

  		var marker = new google.maps.Marker({
		position: myLatlng,
		map: map,
		title: 'Harding Park (Golf Course)'
		});
  		
  		google.maps.event.addListener(marker, 'click', function() {
    		infowindow.open(map,marker);
  });
}

google.maps.event.addDomListener(window, 'load', initialize);









