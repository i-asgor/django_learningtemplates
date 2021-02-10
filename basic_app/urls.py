from django.conf.urls import url
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    url(r'^relatives/$',views.relatives,name='relatives'),
    url(r'^user/$',views.user,name='user'),
]
