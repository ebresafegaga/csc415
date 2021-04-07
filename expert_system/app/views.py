from django.shortcuts import render
from django.http import HttpResponse

import pickle # to load the serialized python object  
import sklearn # for ML prediction 

def index (request): 
    return render (request, 'app/index.html')
 
def classify (request): 
    return render (request, 'app/classify.html')


def do_classify (features): 

    # convert inputs(features) from string to float values.
    features = { k: float (v) for k, v in features.items () }

    # load the saved model from disk, and convert it to a python object.
    # if we want to use another algorithm, just change the file 
    # e.g for SVM, load "svm.sav" instead of "random_forest.sav"
    model = pickle.load (open ("/home/gaga/repos/csc415/random_forest.sav", "rb"))

    # remove the "ID Number" row from the list of features (input)
    row =  (list (features.values ()))[1:]

    # for debugging and ensuring the data is in the right order
    print (row)

    # predict that data 
    prediction = model.predict ([ row ])[0]

    if prediction == 1: 
        return 'malignant'
    elif prediction == 0:
        return 'benign'
    else: 
        return 'error'

def result (request): 
    context = {} 

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

    dignostic = do_classify (context)
    context['diagnostic'] = dignostic 

    return render (request, 'app/result.html', context)