from django.urls import path
from . import views
urlpatterns=[
    path("<int:amount>", views.tax, name="tax"),
    path("taxrate/" ,views.taxrate, name="taxrate"),
    path("", views.index, name="index")
    
]
