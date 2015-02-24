var cameraimages = (function(){
	var getWindStatus = function(speed, deg, bad_deg){
		var wind_abs = Math.abs(bad_deg-deg);
		if(speed>6) return 'wind-danger'; else
		if(speed>3) {
			if(wind_abs<60) return 'wind-danger';
			else return 'wind-warning';
		} else
		return 'wind-ok';
	}

	var requestInProgress = false;

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
				cameraimages.loadWeather();
			});
			$('.resort-info-reload').on('click', function(){
				cameraimages.loadWeather();
			});
			cameraimages.loadWeather(); //get weather on page load
			//if($('body').hasClass('desktop-client')) $('.masonry').masonry({ itemSelector : '.webcamera-image-block'});
		},
		loadWeather : function(){
			if(requestInProgress) return; else requestInProgress = true;
			var url = $('.webcameras').attr('data-weatherurl');
			if(!url) return;
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
							'&nbsp;<i title="Осадки" class="wi '+ rpo.resorts[r].current.icon+'"></i>'+
							'&nbsp;<i title="Скорость ветра" class="wind wi '+ rpo.resorts[r].current.wind.speed_icon+'"></i>'+
							'&nbsp;<i title="Направление ветра" class="wind wi wi-wind-default '+rpo.resorts[r].current.wind.deg_icon+'"></i>';//rpo[r].current);
						wIn3h = rpo.resorts[r].in3h.temp+
							'&nbsp;<i title="Осадки" class="wi '+ rpo.resorts[r].in3h.icon+'"></i>'+
							'&nbsp;<i title="Скорость ветра" class="wind wi '+ rpo.resorts[r].in3h.wind.speed_icon+' '+getWindStatus(rpo.resorts[r].in3h.wind.speed)+'"></i>'+
							'&nbsp;<i title="Направление ветра" class="wind wi wi-wind-default '+rpo.resorts[r].in3h.wind.deg_icon+'"></i>';//rpo[r].in3h);
						wIn6h = rpo.resorts[r].in6h.temp+
							'&nbsp;<i title="Осадки" class="wi '+ rpo.resorts[r].in6h.icon+'"></i>'+
							'&nbsp;<i title="Скорость ветра" class="wind wi '+ rpo.resorts[r].in6h.wind.speed_icon+' '+getWindStatus(rpo.resorts[r].in6h.wind.speed)+'"></i>'+
							'&nbsp;<i title="Направление ветра" class="wind wi wi-wind-default '+rpo.resorts[r].in6h.wind.deg_icon+'"></i>';//rpo[r].in6h);
						wIn24h = rpo.resorts[r].in24h.temp+
							'&nbsp;<i title="Осадки" class="wi '+ rpo.resorts[r].in24h.icon+'"></i>'+
							'&nbsp;<i title="Скорость ветра" class="wind wi '+ rpo.resorts[r].in24h.wind.speed_icon+' '+getWindStatus(rpo.resorts[r].in24h.wind.speed)+'"></i>'+
							'&nbsp;<i title="Направление ветра" class="wind wi wi-wind-default '+rpo.resorts[r].in24h.wind.deg_icon+'"></i>';//rpo[r].in24h);
						$resort_weather.find('.weather-now').html(wNow).addClass(getWindStatus(getWindStatus(rpo.resorts[r].current.wind.speed, rpo.resorts[r].current.wind.deg, rpo.resorts[r].current.wind.bad_deg)));
						$resort_weather.find('.weather-in3h').html(wIn3h).addClass(getWindStatus(getWindStatus(rpo.resorts[r].in3h.wind.speed, rpo.resorts[r].in3h.wind.deg, rpo.resorts[r].in3h.wind.bad_deg)));
						$resort_weather.find('.weather-in6h').html(wIn6h).addClass(getWindStatus(getWindStatus(rpo.resorts[r].in6h.wind.speed, rpo.resorts[r].in6h.wind.deg, rpo.resorts[r].in6h.wind.bad_deg)));
						$resort_weather.find('.weather-in24h').html(wIn24h).addClass(getWindStatus(getWindStatus(rpo.resorts[r].in24h.wind.speed, rpo.resorts[r].in24h.wind.deg, rpo.resorts[r].in24h.wind.bad_deg)));
					}
					weather_loaded = true;
				} else {
					$('.resort .weather .weather-now, \
						.resort .weather .weather-in3h, \
						.resort .weather .weather-in6h, \
						.resort .weather .weather-in24h').html('<i class="resort-info-reload fa fa-reload"></i>');
				}
			}).always(function(){
				requestInProgress = false;
			})
		}
	}
}());

$(function(){
	cameraimages.init();
})