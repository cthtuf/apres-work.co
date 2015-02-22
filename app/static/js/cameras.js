var cameraimages = (function(){
	var weather_loaded = false;
	return {
		init : function(){
			$('.webcamera-reload i').on('click', function(){
				var img = $(this).parents('.webcamera-image-block').find('img');
				a = document.createElement('a');
				a.href = $(img).attr('src');
				a.search = "?p="+Math.random();
				$(img).attr('src', a.href);
			});
			$('.show-resort-additional-info, .resort-info').on('click', function(e){
				e.stopPropagation();
				e.preventDefault();
				$('.show-resort-additional-info').toggleClass('hidden');
				$('.resort-additional-info').toggleClass('hidden');
				cameraimages.loadWeather($(this).parents('.resort').eq(0).attr('data-weatherurl'));
			});
			//if($('body').hasClass('desktop-client')) $('.masonry').masonry({ itemSelector : '.webcamera-image-block'});
		},
		loadWeather : function(url){
			if(!weather_loaded)
			$.get(url).done(function(rpo){
				for(r in rpo){
					var $resort_weather = $('.resort.resort-'+r+ ' .weather');
					$resort_weather.find('.weather-now').html(rpo[r].current.temp+'&nbsp;<i class="wi '+rpo[r].current.icon+'"></i>&nbsp;'+rpo[r].current.wind.speed+'м/с');//rpo[r].current);
					$resort_weather.find('.weather-in3h').html(rpo[r].in3h.temp+'&nbsp;<i class="wi '+rpo[r].in3h.icon+'"></i>&nbsp;'+rpo[r].in3h.wind.speed+'м/с');;//rpo[r].in3h);
					$resort_weather.find('.weather-in6h').html(rpo[r].in6h.temp+'&nbsp;<i class="wi '+rpo[r].in6h.icon+'"></i>&nbsp;'+rpo[r].in6h.wind.speed+'м/с');;//rpo[r].in6h);
					$resort_weather.find('.weather-in24h').html(rpo[r].in24h.temp+'&nbsp;<i class="wi '+rpo[r].in24h.icon+'"></i>&nbsp;'+rpo[r].in24h.wind.speed+'м/с');;//rpo[r].in24h);
				}
				weather_loaded = true;
			}).always(function(){

			})
		}
	}
}());

$(function(){
	cameraimages.init();
})