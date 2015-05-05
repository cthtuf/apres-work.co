# -*- coding: utf-8 -*-
from app import app
import views, camps, coaches, disciplines, events, howitworks, locations, news, resorts, cameramen, useful, riders, notifications
import weather

#global
app.add_url_rule('/', view_func=views.index, methods=['GET'])
app.add_url_rule('/<string:language_suffix>/', view_func=views.language_index, methods=['GET'])

app.add_url_rule('/<string:language_suffix>/locations/', view_func=locations.locations_g_list, methods=['GET'])
app.add_url_rule('/<string:language_suffix>/resorts/', view_func=resorts.resorts_g_list, methods=['GET'])
app.add_url_rule('/<string:language_suffix>/events/', view_func=events.events_g_list, methods=['GET'])
app.add_url_rule('/<string:language_suffix>/news/', view_func=news.news_g_list, methods=['GET'])
app.add_url_rule('/<string:language_suffix>/coaches/', view_func=coaches.coaches_g_list, methods=['GET'])
app.add_url_rule('/<string:language_suffix>/cameramen/', view_func=cameramen.cameramen_g_list, methods=['GET'])
app.add_url_rule('/<string:language_suffix>/disciplines/', view_func=disciplines.disciplines_g_list, methods=['GET'])
app.add_url_rule('/<string:language_suffix>/riders/', view_func=riders.riders_g_list, methods=['GET'])
app.add_url_rule('/<string:language_suffix>/feedback/', view_func=views.feedback, methods=['GET'])

#usefull
app.add_url_rule('/<string:language_suffix>/useful/', view_func=useful.useful_list, methods=['GET'])
app.add_url_rule('/<string:language_suffix>/useful/<int:id>/', view_func=useful.useful_page, methods=['GET'])

#camps
app.add_url_rule('/<string:language_suffix>/camps/', view_func=camps.camps_g_list, methods=['GET'])
app.add_url_rule('/<string:language_suffix>/camp/<int:id>/', view_func=camps.camps_page, methods=['GET'])
app.add_url_rule('/<string:language_suffix>/camp/<int:id>/attend/', view_func=camps.camps_attend, methods=['POST'])
app.add_url_rule('/<string:language_suffix>/camp/<int:id>/feedback/', view_func=camps.camps_feedback, methods=['POST'])

#howitworks infographics
app.add_url_rule('/<string:language_suffix>/howitworks', view_func=howitworks.howitworks_list, methods=['GET'])
app.add_url_rule('/<string:language_suffix>/howitworks/events/', view_func=howitworks.howitworks_events, methods=['GET'])
app.add_url_rule('/<string:language_suffix>/howitworks/camps/', view_func=howitworks.howitworks_camps, methods=['GET'])
app.add_url_rule('/<string:language_suffix>/howitworks/resorts/', view_func=howitworks.howitworks_resorts, methods=['GET'])
app.add_url_rule('/<string:language_suffix>/howitworks/locations/', view_func=howitworks.howitworks_locations, methods=['GET'])
app.add_url_rule('/<string:language_suffix>/howitworks/news/', view_func=howitworks.howitworks_news, methods=['GET'])
app.add_url_rule('/<string:language_suffix>/howitworks/coaches/', view_func=howitworks.howitworks_coaches, methods=['GET'])

#local
app.add_url_rule('/<string:language_suffix>/<string:location_suffix>/', view_func=locations.locations_index, methods=['GET'])
app.add_url_rule('/<string:language_suffix>/<string:location_suffix>/subscribe/', view_func=locations.locations_subscribe, methods=['POST'])

app.add_url_rule('/<string:language_suffix>/<string:location_suffix>/r/', view_func=resorts.resorts_s_list, methods=['GET'])
app.add_url_rule('/<string:language_suffix>/<string:location_suffix>/resorts/', view_func=resorts.resorts_list, methods=['GET'])
app.add_url_rule('/<string:language_suffix>/<string:location_suffix>/r/<int:id>/', view_func=resorts.resorts_s_page, methods=['GET'])
app.add_url_rule('/<string:language_suffix>/<string:location_suffix>/resort/<int:id>/', view_func=resorts.resorts_page, methods=['GET'])

app.add_url_rule('/<string:language_suffix>/<string:location_suffix>/e/', view_func=events.events_s_list, methods=['GET'])
app.add_url_rule('/<string:language_suffix>/<string:location_suffix>/events/', view_func=events.events_list, methods=['GET'])
app.add_url_rule('/<string:language_suffix>/<string:location_suffix>/e/<int:id>/', view_func=events.events_s_page, methods=['GET'])
app.add_url_rule('/<string:language_suffix>/<string:location_suffix>/event/<int:id>/', view_func=events.events_page, methods=['GET'])
app.add_url_rule('/<string:language_suffix>/<string:location_suffix>/event/<int:id>/attend/', view_func=events.events_attend, methods=['POST'])

app.add_url_rule('/<string:language_suffix>/<string:location_suffix>/n/', view_func=news.news_s_list, methods=['GET'])
app.add_url_rule('/<string:language_suffix>/<string:location_suffix>/news/', view_func=news.news_list, methods=['GET'])
app.add_url_rule('/<string:language_suffix>/<string:location_suffix>/n/<int:id>/', view_func=news.news_s_page, methods=['GET'])
app.add_url_rule('/<string:language_suffix>/<string:location_suffix>/news/<int:id>/', view_func=news.news_page, methods=['GET'])

app.add_url_rule('/<string:language_suffix>/<string:location_suffix>/c/', view_func=coaches.coaches_s_list, methods=['GET'])
app.add_url_rule('/<string:language_suffix>/<string:location_suffix>/coaches/', view_func=coaches.coaches_list, methods=['GET'])
app.add_url_rule('/<string:language_suffix>/<string:location_suffix>/c/<int:id>/', view_func=coaches.coaches_s_page, methods=['GET'])
app.add_url_rule('/<string:language_suffix>/<string:location_suffix>/coach/<int:id>/', view_func=coaches.coaches_page, methods=['GET'])

app.add_url_rule('/<string:language_suffix>/<string:location_suffix>/cameramen/', view_func=cameramen.cameramen_list, methods=['GET'])
app.add_url_rule('/<string:language_suffix>/<string:location_suffix>/cameraman/<int:id>/', view_func=cameramen.cameramen_page, methods=['GET'])

app.add_url_rule('/<string:language_suffix>/<string:location_suffix>/d/', view_func=disciplines.disciplines_s_list, methods=['GET'])
app.add_url_rule('/<string:language_suffix>/<string:location_suffix>/disciplines/', view_func=disciplines.disciplines_list, methods=['GET'])
#app.add_url_rule('/<string:language_suffix>/<string:location_suffix>/d/<int:id>/', view_function=views.s_, methods=['GET'])
#app.add_url_rule('/<string:language_suffix>/<string:location_suffix>/discipline/<int:id>/', view_function=views.discipline, methods=['GET'])

app.add_url_rule('/<string:language_suffix>/<string:location_suffix>/riders/', view_func=riders.riders_list, methods=['GET'])
app.add_url_rule('/<string:language_suffix>/<string:location_suffix>/rider/<int:id>/', view_func=riders.riders_page, methods=['GET'])


#weather
app.add_url_rule('/<string:location_suffix>/getweather/', view_func=weather.getweather)

#notifications
app.add_url_rule('/<string:language_suffix>/<string:location_suffix>/getnotifications/', view_func=notifications.notifications_list, methods=['GET', 'POST'])
app.add_url_rule('/push/', view_func=notifications.notifications_push, methods=['GET'])