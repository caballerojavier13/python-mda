$(function(){
	setTimeout(
  		function() {
			$(".loading_wrap").hide();
			$("body").css("background", "white");
			$("body").css("color", "black");
			$(".container").show();
			$("header").show();
			$("footer").show();
		}, 10000);
});