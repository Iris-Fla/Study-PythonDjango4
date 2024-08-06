from django.urls import path
from .views import Helloview

urlpatterns = [
    path('', Helloview.as_view() ,name='index'),
]