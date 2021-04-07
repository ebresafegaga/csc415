from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index (request): 
    return render (request, 'app/index.html')
 
def classify (request): 
    return render (request,  'app/classify.html')

# <<< machine learning classification algorithm here >>> 
# This function should take a list of features and 
# return a diagnostic of either 'malignant' or 'benign'
# for now, it just defualts to benign.
def do_classify (): 
    return 'benign'

def result (request): 
    context = {} 
    id = request.POST.get ('id', 0) 
    context['id'] = id

    radius = request.POST.get ('radius', 0.0000) 
    context['radius'] = radius

    perimeter = request.POST.get ('perimeter', 0.0000) 
    context['perimeter'] = perimeter

    area = request.POST.get ('area', 0.0000) 
    context['area'] = area

    smoothness = request.POST.get ('smoothness', 0.0000) 
    context['smoothness'] = smoothness

    compactness = request.POST.get ('compactness', 0.0000) 
    context['compactness'] = compactness

    concavity = request.POST.get ('concavity', 0.0000) 
    context['concavity'] = concavity

    dignostic = do_classify () # <<<< machine learning function here
    context['diagnostic'] = dignostic 

    return render (request, 'app/result.html', context)