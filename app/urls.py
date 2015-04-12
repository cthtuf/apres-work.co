# -*- coding: utf-8 -*-
from app import app
import views
import weather

app.add_url_rule('/', view_func=views.index, methods=['GET'])
app.add_url_rule('/<string:language_suffix>/', view_func=views.language_index, methods=['GET'])
app.add_url_rule('/<string:language_suffix>/<string:location_suffix>/', view_func=views.location_index, methods=['GET'])
app.add_url_rule('/<string:language_suffix>/<string:location_suffix>/<int:event_id>/attend/', view_func=views.event_attend, methods=['POST'])
app.add_url_rule('/<string:language_suffix>/<string:location_suffix>/subscribe/', view_func=views.subscribe, methods=['POST'])
app.add_url_rule('/<string:language_suffix>/<string:location_suffix>/r/', view_func=views.resorts_short, methods=['GET'])
app.add_url_rule('/<string:language_suffix>/<string:location_suffix>/resorts/', view_func=views.resorts, methods=['GET'])
app.add_url_rule('/<string:language_suffix>/<string:location_suffix>/feedback/', view_func=views.feedback, methods=['GET'])
app.add_url_rule('/<string:location_suffix>/getweather/', view_func=weather.getweather)
app.add_url_rule('/<string:language_suffix>/<string:location_suffix>/howitworks/', view_func=views.howitworks, methods=['GET'])
app.add_url_rule('/<string:language_suffix>/<string:location_suffix>/e/', view_func=views.events_short, methods=['GET'])
app.add_url_rule('/<string:language_suffix>/<string:location_suffix>/events/', view_func=views.events, methods=['GET'])
app.add_url_rule('/<string:language_suffix>/<string:location_suffix>/news/', view_func=views.news, methods=['GET'])
app.add_url_rule('/<string:language_suffix>/<string:location_suffix>/camp/', view_func=views.camp, methods=['GET'])
app.add_url_rule('/<string:language_suffix>/<string:location_suffix>/camp_attend', view_func=views.camp_attend, methods=['POST'])