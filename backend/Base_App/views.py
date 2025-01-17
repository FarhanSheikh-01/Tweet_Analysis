from django.shortcuts import render, HttpResponse
from pickle import load
model = load('.\SaveModels\tf.pkl')

# Create your views here.
def index(request):
    return render(request, "index.html")
    # return HttpResponse("this is home page")

def about(request):
    return HttpResponse("this is about page")

def services(request):
    return HttpResponse("this is service page")

def predict(request):
    return render(request, 'index.html')