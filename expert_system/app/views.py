from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index (request): 
    return render (request, 'app/index.html')
 
def classify (request): 
    return render (request,  'app/classify.html')

# <<< machine learning classification algorithm here >>> 
# This function should take a dictionary of features and 
# return a diagnostic of either 'malignant' or 'benign'
# for now, its just some fake logic.
def do_classify (features): 
    features = {k: float (v) for k, v in features.items () }
    if (features['area'] + features['radius']) > 100: 
        return 'benign'
    else:
        return 'malignant'

def result (request): 
    context = {} 

    # Honest worry: what would be the type of the values gotten from the POST request
    # if it's a string, we'd have to convert it to a number? 
    # what about dynamic typing? 
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

    dignostic = do_classify (context) # <<<< machine learning function here
    context['diagnostic'] = dignostic 

    return render (request, 'app/result.html', context)