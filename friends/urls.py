from django.conf.urls import url 
from . import views

urlpatterns = [
    url(r'', views.index, name='index'),
    url(r'friendslist/', views.FriendsListView.as_view(), name='friendslist'),
    url(r'searchlist/', views.SearchFriendsListView.as_view(), name='searchlist'),
]