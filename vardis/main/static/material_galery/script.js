var gallery = $("#gallery");

function sliderTilt(){
	var itemPrev = gallery.find(".slick-current").prev("li").find(".item");
	var itemNext = gallery.find(".slick-current").next("li").find(".item");

	$(".item").tilt({
		perspective: 300,
		speed: 2000,
		glare: false,
		maxGlare: .2
		});
	itemPrev.tilt.destroy.call(itemPrev);
	itemNext.tilt.destroy.call(itemNext);
}


gallery.on('init', function(event, slick){
	$(sliderTilt);
});

gallery.on('afterChange', function(event, slick, currentSlide){
	$(sliderTilt);
});


gallery.slick({
	dots: false,
	arrows: true,
	infinite: false,
	centerMode: true,
	focusOnSelect: false,
	speed: 1000,
	centerPadding: "24vw",
	slidesToScroll: 1,
	initialSlide: 4,
  draggable: false
});

$(".img").each(function() {
  $(this).append("<img class=\"shad\" src=\"" + $(this).find("img").attr("src") + "\" />");
});
  
  
$(function() {
	$(".img").click(function(){
		if(!$("#gallery").hasClass("detail")){
			$("#gallery").addClass("detail");
      $(".slick-arrow").addClass("none");
		} else if ($("#gallery").hasClass("detail")){
			$("#gallery").removeClass("detail");
      $(".slick-arrow").removeClass("none");
			console.log("overview");
		}
	});
});