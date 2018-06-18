from django.shortcuts import render
from django.views.generic import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


def index(request):
    return render(request, 'base.html')


class FriendsListView(ListView):
    def get(self, request):
        pass


class SearchFriendsListView(ListView):
    def get(self, request):
        pass

