from django import urls
from . import views

urlpatterns = [
    urls.path('', views.index, name='index'),
]