// App Utility Script
// 20241204

$(document).ready(function () {
	// Help popovers for SKOS terms
	$('[data-bs-toggle="popover"]').popover({
		trigger: 'click',
		container: '.popover-container',
		placement: 'top',
		customClass: 'help-popover',
		html: true
	});
	$('[data-bs-toggle="popover"]').click(function (e) {
		e.stopPropagation();
	});
	$('a.poplink').click(function (e) {
		e.preventDefault();
	});
	$(document).click(function (e) {
		if (($('.popover').has(e.target).length == 0) || $(e.target).is('.close')) {
			$('[data-bs-toggle="popover"]').popover('hide');
		}
	});

	// Initialize Mermaid E-R Diagrams
	mermaid.initialize({
		theme: 'forest',
		securityLevel: 'loose',
	});

});