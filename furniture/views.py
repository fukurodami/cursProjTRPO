from cgitb import text
from django.shortcuts import render
from django.views.generic.base import View

class MainView(View):
    def get(self, request):    
        text = {'1': 1, "2": 2}                
        return render(request, "main.html", {"text": text})