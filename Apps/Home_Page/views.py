from django.shortcuts import render
from django.views.generic import ListView, View



class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


class AboutUsView(View):
    def get(self, request):
        return render(request, 'home_Page/about-us.html')