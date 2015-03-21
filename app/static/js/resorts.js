$ = jQuery;

resorts = (function(){
	var params,
		getWindStatus = function(speed, deg, bad_deg){
			var wind_abs = Math.abs(bad_deg-deg);
			if(speed>6) return 'wind-danger'; else
			if(speed>3) {
				if(wind_abs<60) return 'wind-danger';
				else return 'wind-warning';
			} else
			return 'wind-ok';
		},
		isEmpty = function(obj){
			var idx = 0;
			for(k in obj){
				return false;
			}
			return true;
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
						var $resort_weather = $('.resorts-one-item.resort-'+r+ ' .resorts-weather-container'),
						wNow = isEmpty(rpo.resorts[r].current) ? '' : '<span class="weather-temp">'+rpo.resorts[r].current.temp+'</span>'+
							'&nbsp;<i title="Осадки" class="wi fallout '+ rpo.resorts[r].current.icon+'"></i>'+
							'&nbsp;<i title="Скорость ветра" class="wind wi '+ rpo.resorts[r].current.wind.speed_icon+'"></i>'+
							'&nbsp;<i title="Направление ветра" class="wind wi wi-wind-default '+rpo.resorts[r].current.wind.deg_icon+'"></i>',//rpo[r].current);
						wTodayNight = isEmpty(rpo.resorts[r].today_night) ? '' : '<span class="weather-temp">'+rpo.resorts[r].today_night.temp+'</span>'+
							'&nbsp;<i title="Осадки" class="wi fallout '+ rpo.resorts[r].today_night.icon+'"></i>'+
							'&nbsp;<i title="Скорость ветра" class="wind wi '+ rpo.resorts[r].today_night.wind.speed_icon+' '+getWindStatus(rpo.resorts[r].today_night.wind.speed)+'"></i>'+
							'&nbsp;<i title="Направление ветра" class="wind wi wi-wind-default '+rpo.resorts[r].today_night.wind.deg_icon+'"></i>',//rpo[r].today_night);
						wTodayMorning = isEmpty(rpo.resorts[r].today_morning) ? '' : '<span class="weather-temp">'+rpo.resorts[r].today_morning.temp+'</span>'+
							'&nbsp;<i title="Осадки" class="wi fallout '+ rpo.resorts[r].today_morning.icon+'"></i>'+
							'&nbsp;<i title="Скорость ветра" class="wind wi '+ rpo.resorts[r].today_morning.wind.speed_icon+' '+getWindStatus(rpo.resorts[r].today_morning.wind.speed)+'"></i>'+
							'&nbsp;<i title="Направление ветра" class="wind wi wi-wind-default '+rpo.resorts[r].today_morning.wind.deg_icon+'"></i>',//rpo[r].today_morning);
						wTodayDay = isEmpty(rpo.resorts[r].today_day) ? '' : '<span class="weather-temp">'+rpo.resorts[r].today_day.temp+'</span>'+
							'&nbsp;<i title="Осадки" class="wi fallout '+ rpo.resorts[r].today_day.icon+'"></i>'+
							'&nbsp;<i title="Скорость ветра" class="wind wi '+ rpo.resorts[r].today_day.wind.speed_icon+' '+getWindStatus(rpo.resorts[r].today_day.wind.speed)+'"></i>'+
							'&nbsp;<i title="Направление ветра" class="wind wi wi-wind-default '+rpo.resorts[r].today_day.wind.deg_icon+'"></i>';//rpo[r].today_day);
						wTodayEvening = isEmpty(rpo.resorts[r].today_evening) ? '' : '<span class="weather-temp">'+rpo.resorts[r].today_evening.temp+'</span>'+
							'&nbsp;<i title="Осадки" class="wi fallout '+ rpo.resorts[r].today_evening.icon+'"></i>'+
							'&nbsp;<i title="Скорость ветра" class="wind wi '+ rpo.resorts[r].today_evening.wind.speed_icon+' '+getWindStatus(rpo.resorts[r].today_evening.wind.speed)+'"></i>'+
							'&nbsp;<i title="Направление ветра" class="wind wi wi-wind-default '+rpo.resorts[r].today_evening.wind.deg_icon+'"></i>';//rpo[r].today_evening);
						wTomorrowNight = isEmpty(rpo.resorts[r].tomorrow_night) ? '' : '<span class="weather-temp">'+rpo.resorts[r].tomorrow_night.temp+'</span>'+
							'&nbsp;<i title="Осадки" class="wi fallout '+ rpo.resorts[r].tomorrow_night.icon+'"></i>'+
							'&nbsp;<i title="Скорость ветра" class="wind wi '+ rpo.resorts[r].tomorrow_night.wind.speed_icon+' '+getWindStatus(rpo.resorts[r].tomorrow_night.wind.speed)+'"></i>'+
							'&nbsp;<i title="Направление ветра" class="wind wi wi-wind-default '+rpo.resorts[r].tomorrow_night.wind.deg_icon+'"></i>';//rpo[r].tomorrow_night);
						wTomorrowMorning = isEmpty(rpo.resorts[r].tomorrow_morning) ? '' : '<span class="weather-temp">'+rpo.resorts[r].tomorrow_morning.temp+'</span>'+
							'&nbsp;<i title="Осадки" class="wi fallout '+ rpo.resorts[r].tomorrow_morning.icon+'"></i>'+
							'&nbsp;<i title="Скорость ветра" class="wind wi '+ rpo.resorts[r].tomorrow_morning.wind.speed_icon+' '+getWindStatus(rpo.resorts[r].tomorrow_morning.wind.speed)+'"></i>'+
							'&nbsp;<i title="Направление ветра" class="wind wi wi-wind-default '+rpo.resorts[r].tomorrow_morning.wind.deg_icon+'"></i>';//rpo[r].tomorrow_morning);
						wTomorrowDay = isEmpty(rpo.resorts[r].tomorrow_day) ? '' : '<span class="weather-temp">'+rpo.resorts[r].tomorrow_day.temp+'</span>'+
							'&nbsp;<i title="Осадки" class="wi fallout '+ rpo.resorts[r].tomorrow_day.icon+'"></i>'+
							'&nbsp;<i title="Скорость ветра" class="wind wi '+ rpo.resorts[r].tomorrow_day.wind.speed_icon+' '+getWindStatus(rpo.resorts[r].tomorrow_day.wind.speed)+'"></i>'+
							'&nbsp;<i title="Направление ветра" class="wind wi wi-wind-default '+rpo.resorts[r].tomorrow_day.wind.deg_icon+'"></i>';//rpo[r].tomorrow_day);
						wTomorrowEvening = isEmpty(rpo.resorts[r].tomorrow_evening) ? '' : '<span class="weather-temp">'+rpo.resorts[r].tomorrow_evening.temp+'</span>'+
							'&nbsp;<i title="Осадки" class="wi fallout '+ rpo.resorts[r].tomorrow_evening.icon+'"></i>'+
							'&nbsp;<i title="Скорость ветра" class="wind wi '+ rpo.resorts[r].tomorrow_evening.wind.speed_icon+' '+getWindStatus(rpo.resorts[r].tomorrow_evening.wind.speed)+'"></i>'+
							'&nbsp;<i title="Направление ветра" class="wind wi wi-wind-default '+rpo.resorts[r].tomorrow_evening.wind.deg_icon+'"></i>';//rpo[r].tomorrow_evening);



						$resort_weather.find('.weather-now').html(wNow).removeClass('hidden').addClass(getWindStatus(rpo.resorts[r].current.wind.speed, rpo.resorts[r].current.wind.deg, rpo.resorts[r].current.wind.bad_deg));
						if(!isEmpty(rpo.resorts[r].today_night)) 
							$resort_weather.find('.weather-today-night').html(wTodayNight).addClass(getWindStatus(rpo.resorts[r].today_night.wind.speed, rpo.resorts[r].today_night.wind.deg, rpo.resorts[r].today_night.wind.bad_deg));
						else
							$resort_weather.find('.weather-today-night').addClass('hidden');
						if(!isEmpty(rpo.resorts[r].today_morning))
							$resort_weather.find('.weather-today-morning').html(wTodayMorning).removeClass('hidden').addClass(getWindStatus(rpo.resorts[r].today_morning.wind.speed, rpo.resorts[r].today_morning.wind.deg, rpo.resorts[r].today_morning.wind.bad_deg));
						else
							$resort_weather.find('.weather-today-morning').addClass('hidden');
						if(!isEmpty(rpo.resorts[r].today_day))
							$resort_weather.find('.weather-today-day').html(wTodayDay).removeClass('hidden').addClass(getWindStatus(rpo.resorts[r].today_day.wind.speed, rpo.resorts[r].today_day.wind.deg, rpo.resorts[r].today_day.wind.bad_deg));
						else
							$resort_weather.find('.weather-today-day').addClass('hidden');
						if(!isEmpty(rpo.resorts[r].today_evening))
							$resort_weather.find('.weather-today-evening').html(wTodayEvening).removeClass('hidden').addClass(getWindStatus(rpo.resorts[r].today_evening.wind.speed, rpo.resorts[r].today_evening.wind.deg, rpo.resorts[r].today_evening.wind.bad_deg));
						else
							$resort_weather.find('.weather-today-evening').addClass('hidden');
						if(!isEmpty(rpo.resorts[r].tomorrow_night))
							$resort_weather.find('.weather-tomorrow-night').html(wTomorrowNight).removeClass('hidden').addClass(getWindStatus(rpo.resorts[r].tomorrow_night.wind.speed, rpo.resorts[r].tomorrow_night.wind.deg, rpo.resorts[r].tomorrow_night.wind.bad_deg));
						else
							$resort_weather.find('.weather-tomorrow-night').addClass('hidden');
						if(!isEmpty(rpo.resorts[r].tomorrow_morning))
							$resort_weather.find('.weather-tomorrow-morning').html(wTomorrowMorning).removeClass('hidden').addClass(getWindStatus(rpo.resorts[r].tomorrow_morning.wind.speed, rpo.resorts[r].tomorrow_morning.wind.deg, rpo.resorts[r].tomorrow_morning.wind.bad_deg));
						else
							$resort_weather.find('.weather-tomorrow-morning').addClass('hidden');
						if(!isEmpty(rpo.resorts[r].tomorrow_day))
							$resort_weather.find('.weather-tomorrow-day').html(wTomorrowDay).removeClass('hidden').addClass(getWindStatus(rpo.resorts[r].tomorrow_day.wind.speed, rpo.resorts[r].tomorrow_day.wind.deg, rpo.resorts[r].tomorrow_day.wind.bad_deg));
						else
							$resort_weather.find('.weather-tomorrow-day').addClass('hidden');
						if(!isEmpty(rpo.resorts[r].tomorrow_evening))
							$resort_weather.find('.weather-tomorrow-evening').html(wTomorrowEvening).removeClass('hidden').addClass(getWindStatus(rpo.resorts[r].tomorrow_evening.wind.speed, rpo.resorts[r].tomorrow_evening.wind.deg, rpo.resorts[r].tomorrow_evening.wind.bad_deg));
						else
							$resort_weather.find('.weather-tomorrow-evening').addClass('hidden');
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
		},
		reloadWebCamera : function(e){
			e.preventDefault();
			e.stopPropagation();
			var img = $(this).parent().find('img');
			a = document.createElement('a');
			a.href = $(img).attr('src');
			a.search = "?p="+Math.random();
			$(img).attr('src', a.href);
		}
	}
})();

$(function(){
	resorts.init({'weather_url' : $('.resorts-one').attr('data-weatherurl')});
	resorts.loadWeather();
	$('.resorts-weather-load').on('click', resorts.loadWeather);
});