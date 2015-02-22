var cameraimages = (function(){
	var getWindStatus = function(speed){
		if(speed>6) return 'danger'; else
		if(speed>3) return 'warning'; else
		return 'ok';
	}

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
			$('.resort-info-reload').on('click', function(){
				cameraimages.loadWeather($(this).parents('.resort').eq(0).attr('data-weatherurl'));
			});
			//if($('body').hasClass('desktop-client')) $('.masonry').masonry({ itemSelector : '.webcamera-image-block'});
		},
		loadWeather : function(url){
			if(!weather_loaded)
			$.get(url).done(function(rpo){
				var wNow = '',
					wIn3h = '',
					wIn6h = '',
					wIn24h = '';

				if(rpo.success === 'true'){
					for(r in rpo.resorts){
						var $resort_weather = $('.resort.resort-'+r+ ' .weather');
						wNow = rpo.resorts[r].current.temp+
							'&nbsp;<i class="wi '+ rpo.resorts[r].current.icon+'"></i>'+
							'&nbsp;<i class="wi '+ rpo.resorts[r].current.wind.speed_icon+' '+getWindStatus(rpo.resorts[r].current.wind.speed)+'"></i>'+
							'&nbsp;<i class="wi wi-wind-default '+rpo.resorts[r].current.wind.deg_icon+'"></i>';//rpo[r].current);
						wIn3h = rpo.resorts[r].in3h.temp+
							'&nbsp;<i class="wi '+ rpo.resorts[r].in3h.icon+'"></i>'+
							'&nbsp;<i class="wi '+ rpo.resorts[r].in3h.wind.speed_icon+' '+getWindStatus(rpo.resorts[r].in3h.wind.speed)+'"></i>'+
							'&nbsp;<i class="wi wi-wind-default '+rpo.resorts[r].in3h.wind.deg_icon+'"></i>';//rpo[r].in3h);
						wIn6h = rpo.resorts[r].in6h.temp+
							'&nbsp;<i class="wi '+ rpo.resorts[r].in6h.icon+'"></i>'+
							'&nbsp;<i class="wi '+ rpo.resorts[r].in6h.wind.speed_icon+' '+getWindStatus(rpo.resorts[r].in6h.wind.speed)+'"></i>'+
							'&nbsp;<i class="wi wi-wind-default '+rpo.resorts[r].in6h.wind.deg_icon+'"></i>';//rpo[r].in6h);
						wIn24h = rpo.resorts[r].in24h.temp+
							'&nbsp;<i class="wi '+ rpo.resorts[r].in24h.icon+'"></i>'+
							'&nbsp;<i class="wi '+ rpo.resorts[r].in24h.wind.speed_icon+' '+getWindStatus(rpo.resorts[r].in24h.wind.speed)+'"></i>'+
							'&nbsp;<i class="wi wi-wind-default '+rpo.resorts[r].in24h.wind.deg_icon+'"></i>';//rpo[r].in24h);
						$resort_weather.find('.weather-now').html(wNow);
						$resort_weather.find('.weather-in3h').html(wIn3h);
						$resort_weather.find('.weather-in6h').html(wIn6h);
						$resort_weather.find('.weather-in24h').html(wIn24h);
					}
					weather_loaded = true;
				} else {
					$('.resort .weather .weather-now, \
						.resort .weather .weather-in3h, \
						.resort .weather .weather-in6h, \
						.resort .weather .weather-in24h').html('<i class="resort-info-reload fa fa-reload"></i>');
				}
			}).always(function(){

			})
		}
	}
}());

$(function(){
	cameraimages.init();
})