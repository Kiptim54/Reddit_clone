from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    title="Home Page | Reddit"
    return HttpResponse("Hey there I already forgot this in a week can you believe me!")