function initLocalStorageControls() {


	var userMessage;

	// Test if browser supports local storage:
	if (Modernizr.localstorage) {
		// geolocation is available
		console.log("Local storage is supported.");
		// userMessage = "Use the form below to sign up!"
		// $(".status-message").html(userMessage);
		// // Events handlers for onload:
		// $('#data-dashboard').show('slow');
		
	} else {
		// No geolocation  support
		console.log("No local storage support.");
		// userMessage = "Sorry, local storage is not available."
		// $(".status-message").html(userMessage);
		// $('#data-dashboard').hide('slow');
	}

		// Hardcode name to text field
		$('#id_name').val(localStorage.getItem('name'));
		$('#id_email').val(localStorage.getItem('email'));
		$('#id_birth_date').val(localStorage.getItem('birth_date'));
		$('#id_gender').val(localStorage.getItem('gender'));
		$('#id_skill_level').val(localStorage.getItem('skill_level'));
		$('#id_handicap').val(localStorage.getItem('handicap'));
		$('#id_location').val(localStorage.getItem('location'));
		$('#id_about_me').val(localStorage.getItem('about_me'));
		$('#id_company').val(localStorage.getItem('company'));
		$('#id_website').val(localStorage.getItem('website'));
		$('#id_picture').val(localStorage.getItem('picture'));
	
		// Events handler for 'update' click
		$('#user-details').click(function() {
		console.log("you clicked the button!");

			$('form input').each(function() {
				console.log(this);
				var myId = $(this).attr('id');
				var myVal = $(this).val();
				localStorage.setItem(myId, myVal);
		
   				var storedVal = localStorage.getItem(myId);
   				console.log(storedVal);

   			});
   		});


		// Clear local storage items
		$('.clear').click(function() {
			var removeValue = $(this).attr('data-localitem');
			localStorage.removeItem(removeValue);
		});


		// Clear all items
		$('#clear-all').click(function() {

			localStorage.clear();
		});

};


$(document).ready(function () {

	initLocalStorageControls();

});












