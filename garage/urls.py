from django.urls import path,include

from garage_manager import urls
from . import views
from .views import GarageView
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()
router.register('garages',views.GarageView)
router.register('cars',views.CarView)

urlpatterns = [
    #path("", views.garage_index, name="garage_index"),
    #path("<int:pk>/", views.garage_cars, name="garage_cars"),
    #path("<int:pk>/", views.car_detail, name="car_detail"),
    #path('garage/', views.GarageView.as_view()), #http://127.0.0.1:8000/api/garage/
    path('',include(router.urls))

]

#urlpatterns = format_suffix_patterns(urlpatterns)