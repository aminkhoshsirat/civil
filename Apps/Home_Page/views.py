from django.shortcuts import render
from django.views.generic import ListView, View


class HeaderView(View):
    def get(self, request):
        return render(request, 'partial/header.html')

class FooterView(View):
    def get(self, request):
        return render(request, 'partial/footer.html')

class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


class AboutUsView(View):
    def get(self, request):
        return render(request, 'home_Page/about-us.html')