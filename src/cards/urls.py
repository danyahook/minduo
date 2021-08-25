from django.conf.urls import url
from cards import views

urlpatterns = [
    url(r'^api/cards$', views.card_list),
    url(r'^api/card/(?P<pk>[0-9]+)$', views.card_detail),
]