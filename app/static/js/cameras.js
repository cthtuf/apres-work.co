var cameraimages = (function(){
	return {
		init : function(){
			$('.webcamera-reload i').on('click', function(){
				var img = $(this).parents('.webcamera-image-block').find('img');
				a = document.createElement('a');
				a.href = $(img).attr('src');
				a.search = "?p="+Math.random();
				$(img).attr('src', a.href);
			});

			$('.masonry').masonry({ itemSelector : '.webcamera-image-block'});
		}
	}
}());

$(function(){
	cameraimages.init();
})