var elemA = document.getElementById("er-diagram-1");
var elemB = document.getElementById("er-diagram-2");
var elemC = document.getElementById("er-diagram-3");
var elemD = document.getElementById("er-diagram-4");
var elemE = document.getElementById("green-class-diagram");
var elemF = document.getElementById("master-class-diagram");


function openFullscreen(diagram) {
	if(diagram == 'A') {
		if (elemA.requestFullscreen) {
			elemA.requestFullscreen();
		  } else if (elemA.webkitRequestFullscreen) { /* Safari */
			elemA.webkitRequestFullscreen();
		  } else if (elemA.msRequestFullscreen) { /* IE11 */
			elemA.msRequestFullscreen();
		  }
	}
	else if(diagram == 'B') {
		if (elemB.requestFullscreen) {
			elemB.requestFullscreen();
		  } else if (elemB.webkitRequestFullscreen) { /* Safari */
			elemB.webkitRequestFullscreen();
		  } else if (elemB.msRequestFullscreen) { /* IE11 */
			elemB.msRequestFullscreen();
		  }
	}
	else if(diagram == 'C') {
		if (elemC.requestFullscreen) {
			elemC.requestFullscreen();
		  } else if (elemC.webkitRequestFullscreen) { /* Safari */
			elemC.webkitRequestFullscreen();
		  } else if (elemC.msRequestFullscreen) { /* IE11 */
			elemC.msRequestFullscreen();
		  }
	}
		if(diagram == 'D') {
		if (elemD.requestFullscreen) {
			elemD.requestFullscreen();
		  } else if (elemD.webkitRequestFullscreen) { /* Safari */
			elemD.webkitRequestFullscreen();
		  } else if (elemD.msRequestFullscreen) { /* IE11 */
			elemD.msRequestFullscreen();
		  }
	}
			if(diagram == 'C1') {
		if (elemE.requestFullscreen) {
			elemE.requestFullscreen();
		  } else if (elemE.webkitRequestFullscreen) { /* Safari */
			elemE.webkitRequestFullscreen();
		  } else if (elemE.msRequestFullscreen) { /* IE11 */
			elemE.msRequestFullscreen();
		  }
	}
				if(diagram == 'C2') {
		if (elemF.requestFullscreen) {
			elemF.requestFullscreen();
		  } else if (elemF.webkitRequestFullscreen) { /* Safari */
			elemF.webkitRequestFullscreen();
		  } else if (elemF.msRequestFullscreen) { /* IE11 */
			elemF.msRequestFullscreen();
		  }
	}

}
