from django.conf.urls import  url
from .  import views

urlpatterns = [
	url(r'^display$', views.display, name='display'),
    url(r'^add$', views.add, name='add'),
    url(r'^update$', views.update, name='update'),
    url(r'^delete$', views.delete, name='delete')
     
]
