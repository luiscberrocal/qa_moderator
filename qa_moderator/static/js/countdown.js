// COUNTDOWN
function makeTimer(){

	var endTime = new Date("8 Oct 2018 07:00:00 GMT-05:00");
	endTime = (Date.parse(endTime) / 1000);

	var now = new Date();
	now = (Date.parse(now) / 1000);

	var timeLeft = endTime - now;

	var days = Math.floor(timeLeft / 86400);
	var hours = Math.floor((timeLeft - (days * 86400)) / 3600);
	var minutes = Math.floor((timeLeft - (days * 86400) - (hours * 3600 )) / 60);
	var seconds = Math.floor((timeLeft - (days * 86400) - (hours * 3600) - (minutes * 60)));

	$("#countdowndays p").html(days + " Days");
	$("#countdownhours p").html(hours + " Hours");
	$("#countdownmins p").html(minutes + " Minutes");
	$("#countdownsecs p").html(seconds + " Seconds");

	//ADAPT FONT SIZE
	var fontwidth1 = $('#countdowndays p').width();
  var divwidth = $('.box').width();
  var size1 = parseFloat($('#countdowndays p').css('font-size'));
  var fontsize1 = (divwidth / fontwidth1) * size1;

  var fontwidth2 = $('#countdownhours p').width();
  var divwidth = $('.box').width();
  var size2 = parseFloat($('#countdownhours p').css('font-size'));
  var fontsize2 = (divwidth / fontwidth2) * size2;

  var fontwidth3 = $('#countdownmins p').width();
  var divwidth = $('.box').width();
  var size3 = parseFloat($('#countdownmins p').css('font-size'));
  var fontsize3 = (divwidth / fontwidth3) * size3;

  var fontwidth4 = $('#countdownsecs p').width();
  var divwidth = $('.box').width();
  var size4 = parseFloat($('#countdownsecs p').css('font-size'));
  var fontsize4 = (divwidth / fontwidth4) * size4;

  $('#countdowndays p').css("font-size", fontsize1);
  $('#countdownhours p').css("font-size", fontsize2);
  $('#countdownmins p').css("font-size", fontsize3);
  $('#countdownsecs p').css("font-size", fontsize4);
}
// update every second
setInterval(function() { makeTimer(); }, 1000);



