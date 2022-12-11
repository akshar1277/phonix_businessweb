from django.urls import path
from . import views

urlpatterns = [
    # path('',views.getContact),
    path('',views.postContact ),
    path('positions/',views.postJob),
]