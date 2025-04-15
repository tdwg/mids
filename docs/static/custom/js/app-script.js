// App Utility Script
// 20241204

$(document).ready(function () {
	// Help popovers for SKOS terms
	console.log("Document Ready");
	$('[data-bs-toggle="popover"]').popover({
		trigger: 'click',
		container: 'body',
		placement: 'top',
		customClass: 'help-popover',
		html: true
	});
	$('[data-bs-toggle="popover"]').click(function (e) {
		console.log("Popover Click");
		e.stopPropagation();
	});
	$('a.poplink').click(function (e) {
		console.log("Poplink Click");
		e.preventDefault();
	});
	$(document).click(function (e) {
		if (($('.popover').has(e.target).length == 0) || $(e.target).is('.close')) {
			$('[data-bs-toggle="popover"]').popover('hide');
		}
	});

});