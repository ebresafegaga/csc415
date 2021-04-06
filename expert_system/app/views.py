from django.shortcuts import render
from django.http import HttpResponse

from .forms import ClassifyForm

# Create your views here.

def index (request): 
    return  render (request, 'app/index.html')
 
def classify (request): 
    return render (request, 'app/classify.html')

def result (request): 
    # if request.method == 'POST': 
    #     form = ClassifyForm (request.POST)
    #     if form.is_valid (): 
    #         return HttpResponse("Thanks")
    # else: 
    #     form = NameForm()

    return render (request, 'app/result.html')