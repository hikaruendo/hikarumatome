from django.shortcuts import render
import requests

def map(request):
    return render(request, 'map/index.html')
