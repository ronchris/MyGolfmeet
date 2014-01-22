// $(document).ready(function() {
//     $("#menu").accordion({collapsible: true, active: false});
// });

// $(document).ready(function () {

// var pars = [3,4,4,3,5,4,3,3,4];

// var scores = [
// 	{
// 		name:'Jones',
// 		strokes:[3,4,3,5]
// 	},
// 	{
// 		name:'Smith',
// 		strokes:[4,3,3,3]
// 	},
// 	{
// 		name:'Green',
// 		strokes:[5,4,4,3]
// 	},
// 	{
// 		name:'Harris',
// 		strokes:[3,3,4,4]
// 	},
// 	{
// 		name:'Williams',
// 		strokes:[4,4,3,5]
// 	}
// ];

// // ________________________________________________________________ for loops for score form

// 	// Create row for Par row using the "var pars = []"
// 	var parTotal = 0;
// 	// Create loop to enter par array data
// 	for (var k=0; k<pars.length + 9; k++) {
// 		// Create if/else statement whether a 'par count' has been listed for each hole; otherwise append empty cell
// 		if (pars[k] === undefined) {
// 		$('#firstRow').append('<td id="cell_' + (k+1) + "-0" + '">' + 0 + '</td>')
// 		} else {
// 		$('#firstRow').append('<td id="cell_' + (k+1) + "-0" + '">' + pars[k] + '</td>');
// 		// 0 = 0 + 1 will iterate through all the par counts for the total par
// 		parTotal = parTotal + pars[k];
// 		console.log("The par total is:" + parTotal);
// 		}

// 	};
// 	// Append par cell data into par row
// 	$('#firstRow').append('<td id="cell_19-0">' + parTotal + '</td>');


// 			// Create new row for each golfer
// 			for (var i=0; i<scores.length; i++) {
// 				// Create variables to use in for loops for tr's and td's
// 				var playerName = scores[i].name;
// 				var tempTotal = 0;
// 				// Append player name to each row
// 				$('.body').append('<tr id="scoreRows' + i + '"><td id="cell_' + "0" + "-" + (i+1) + '">' + playerName + '</td>');
// 				// Create for loop to iterate through player's stroke per hole
// 				for (var j=0; j<18; j++) {
// 					// Create variables to append player's score per hole
// 					var currentStroke = scores[i].strokes[j];
// 					var golferStroke = currentStroke || "";
// 					// Create if/else statement whether a 'hole score' has been listed for each hole; otherwise append empty cell
// 					if (golferStroke) {
// 						$('#scoreRows' + i).append('<td id="cell_' + (j+1) + "-" + (i+1) + '"><input type="text" + value="' + golferStroke + '"></td>');
// 						tempTotal = tempTotal + golferStroke;
// 						console.log("The temp total is:" + tempTotal);
// 					} else {
// 						$('#scoreRows' + i).append('<td id="cell_' + (j+1) + "-" + (i+1) + '"><input type="text" + value="' + golferStroke + '"></td>');
// 					}
// 				}
// 				// Append score totals for each player
// 				$('#scoreRows' + i).append('<td id="cell_' + (j+1) + "-" + (i+1) + '">' + tempTotal + '</td></tr>');
// 			}




// 	// ________________________________________________________________ for loops for scoreboard

// 	// Create scoreboard table with same dimensions on score form
// 	var scoreTotal = 0;
// 	// Create loop to enter par array data
// 	for (var z=0; z<pars.length + 9; z++) {
// 		// Create if/else statement whether a 'par count' has been listed for each hole; otherwise append empty cell
// 		if (pars[z] === undefined) {
// 		$('#firstRow2').append('<td id="outputCell_' + (z+1) + "-0" + '">' + 0 + '</td>')
// 		} else {
// 		$('#firstRow2').append('<td id="outputCell_' + (z+1) + "-0" + '">' + pars[z] + '</td>');
// 		// 0 = 0 + 1 will iterate through all the par counts for the total par
// 		scoreTotal = scoreTotal + pars[z];
// 		console.log("The par total is:" + scoreTotal);
// 		}

// 	};
// 	// Append par cell data into par row
// 	$('#firstRow2').append('<td id="outputCell_19-0">' + scoreTotal + '</td>');




// 			// Create new row for each golfer
// 			for (var y=0; y<scores.length; y++) {

// 				// Create variables to use in for loops for tr's and td's
// 				var golferName = scores[y].name;
// 				var newTotal = 0;
// 				// Append player name to each row
// 				$('.bod').append('<tr id="eagl' + y + '"><td id="outputCell_' + "0" + "-" + (y+1) + '">' + golferName + '</td>');
// 				// Create for loop to iterate through player's stroke per hole
// 				for (var q=0; q<18; q++) {

// 					// Create variables to append player's + or - score per hole
// 					var golfStroke = scores[y].strokes[q];
// 					var parStroke = pars[q];

// 					// Create comparator statement to change undefined array values to number 0 for calculation
// 					var trutheyStroke = golfStroke || 0;
// 					var trutheyPar = parStroke || 0;

// 					var scoreStroke = trutheyStroke - trutheyPar;

// 					console.log("The over or minus par is: " + scoreStroke);

// 					// Create if/else statement whether a 'hole score' has been listed for each hole; otherwise append empty cell
// 					if (scoreStroke > 0) {
// 						$('#eagl' + y).append('<td id="outputCell_' + (q+1) + "-" + (y+1) + '">' + "+" + scoreStroke + '</td>');
// 						newTotal = newTotal + scoreStroke;
// 						console.log("The temp total is:" + newTotal);
// 					}
// 					else if (scoreStroke < 0) {
// 						$('#eagl' + y).append('<td id="outputCell_' + (q+1) + "-" + (y+1) + '">' + scoreStroke + '</td>');
// 						newTotal = newTotal + scoreStroke;
// 						console.log("The temp total is:" + newTotal);
// 					} else {
// 						$('#eagl' + y).append('<td id="outputCell_' + (q+1) + "-" + (y+1) + '"></td>');
// 					}
// 				}
// 				// Append score totals for each player
// 				$('#eagl' + y).append('<td id="outputCell_' + (q+1) + "-" + (y+1) + '">' + newTotal + '</td></tr>');
// 			}

// 	//====================================================================================================================================
// 	// Take edited value to calculate new score when 'update' is clicked
// 	//====================================================================================================================================

// 		$("#update").click(function calculateScore() {
// 			console.log("You clicked the update button!")

// 			// Function to append new score into cell referenced 'td'
//            	var y=0; // y axis
// 		    var x=0; // x axis
// 		    for (y=1;y<6;y++) {

// 		    	for (x=1;x<20;x++) {
// 	    		// write to 'outputCell_x-y' the value of 'cell_x-y';
// 	    		tempNewCellValue = $("#cell_" + x + "-" + y + " input").val();
// 	    		$("#outputCell_" + x + "-" + y).text(tempNewCellValue);
// 	    		console.log ("tempNewCellValue: " + tempNewCellValue);
// 		    	}


// 		    }
// 		});



// 	//====================================================================================================================================
// 	// Hide/show scoreboard form
// 	//====================================================================================================================================

// 		// To hide button (referring to button ID)
// 	 	$("#hideButton").click(function() {
// 	 		// Create a variable to change text during click
// 		 	var btnText = $(this).text();
// 		 	// Create if/statement to toggle hide/show
// 		 	if (btnText == 'Hide Form') {
// 		 		$(".bod").hide('slow'); // To hide slowly
// 		 		$(this).text('Show Form');
// 		 	} else {
// 		 		$(".bod").show('slow'); // To show slowly
// 		 		$(this).text('Hide Form');
// 		 	}
// 		});





// });

