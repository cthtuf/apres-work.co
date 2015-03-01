$ = jQuery;

var resorts = (function(){
	var params,
		getWindStatus = function(speed, deg, bad_deg){
			var wind_abs = Math.abs(bad_deg-deg);
			if(speed>6) return 'wind-danger'; else
			if(speed>2) {
				if(wind_abs<60) return 'wind-danger';
				else return 'wind-warning';
			} else
			return 'wind-ok';
		},
		requestInProgress = false,
		weather_loaded = false;


	return {
		init : function(p_params){
			params = p_params;
		},
		loadWeather : function(){
			var beforeRequest = function(){
				$resorts = $('.resorts-one-item');
				$resorts.find('.resorts-weather-load').hide();
				$resorts.find('.resorts-weather-loading').show();
				$resorts.find('.resorts-weather-container').hide();
			}

			var onError = function(){
				$resorts = $('.resorts-one-item');
				$resorts.find('.resorts-weather-load').show();
				$resorts.find('.resorts-weather-loading').hide();
				$resorts.find('.resorts-weather-container').hide();
			}

			var onSuccess = function(){
				$resorts = $('.resorts-one-item');
				$resorts.find('.resorts-weather-loading').hide();
				$resorts.find('.resorts-weather-load').hide();
				$resorts.find('.resorts-weather-container').slideDown();
				weather_loaded = true;
			}

			if(requestInProgress) return; else requestInProgress = true;
			var url = params.weather_url;
			if(!url) return;
			if(weather_loaded) return;
			beforeRequest();
			$.get(url).done(function(rpo){
				var wNow = '',
					wIn3h = '',
					wIn6h = '',
					wIn24h = '';

				if(rpo.success === 'true'){
					for(r in rpo.resorts){
						var $resort_weather = $('.resorts-one-item.resort-'+r+ ' .resorts-weather-container');
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
					onSuccess();
				} else {
					onError();
				}
			}).always(function(){
				requestInProgress = false;
			}).error(function(){
				onError();
			})
		}
	}
})();

$(function(){
	resorts.init({'weather_url' : $('.resorts-one').attr('data-weatherurl')});
	resorts.loadWeather();
	$('.resorts-weather-load').on('click', resorts.loadWeather);
});