from django.shortcuts import render
from django.http import HttpResponse

import pickle
import sklearn

# Create your views here.

def index (request): 
    return render (request, 'app/index.html')
 
def classify (request): 
    return render (request, 'app/classify.html')

# <<< machine learning classification algorithm here >>> 
# This function should take a dictionary of features and 
# return a diagnostic of either 'malignant' or 'benign'
# for now, its just some fake logic.
def do_classify (features): 
    features = {k: float (v) for k, v in features.items () }
    model = pickle.load (open  ("/home/gaga/repos/csc415/random_forest.sav", "rb"))
    row =  (list (features.values ()))[1:]
    print (row)
    prediction = model.predict ([
       row 
    ])
    if prediction == 1: 
        return 'malignant'
    elif prediction == 0:
        return 'benign'
    else: 
        return 'error'

def result (request): 
    context = {} 

    # Honest worry: what would be the type of the values gotten from the POST request
    # if it's a string, we'd have to convert it to a number? 
    # what about dynamic typing? 
    id = request.POST.get ('id', 0) 
    context['id'] = id

    radius = request.POST.get ('radius', 0.0000) 
    context['radius'] = radius

    texture = request.POST.get ('texture', 0.0000) 
    context['texture'] = texture

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

    concave_points = request.POST.get ('concave_points', 0.0000) 
    context['concave_points'] = concave_points

    symmetry = request.POST.get ('symmetry', 0.0000) 
    context['symmetry'] = symmetry

    fractal_dimension = request.POST.get ('fractal_dimension', 0.0000) 
    context['fractal_dimension'] = fractal_dimension

    dignostic = do_classify (context) # <<<< machine learning function here
    context['diagnostic'] = dignostic 

    return render (request, 'app/result.html', context)