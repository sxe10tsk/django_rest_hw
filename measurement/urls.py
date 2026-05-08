from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from django.views.static import serve

from measurement.views import SensorView, MeasurementsView, SensorUpdate

urlpatterns = [
	path('sensors/', SensorView.as_view()),
	path('sensors/<pk>/', SensorUpdate.as_view()),
	path('measurements/', MeasurementsView.as_view())
]
