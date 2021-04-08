from django.shortcuts import render
from django.http import HttpResponse

import pickle # to load the serialized python object  
import sklearn # for ML prediction 
import os

def index (request): 
    return render (request, 'app/index.html')
 
def classify (request): 
    return render (request, 'app/classify.html')

def get_path (): 
    return os.path.dirname (os.path.realpath (__file__))

def do_classify (features):
    classifier = "random_forest.sav"
    classifier = os.path.join (get_path (), classifier)

    # convert inputs(features) from string to float values.
    features = { k: float (v) for k, v in features.items () }

    # load the saved model from disk, and convert it to a python object.
    # if we want to use another algorithm, just change the file 
    # e.g for SVM, load "svm.sav" instead of "random_forest.sav"
    # "~/csc415/random_forest.sav"
    model = pickle.load (open (classifier, "rb"))

    # remove the "ID Number" row from the list of features (input)
    row =  (list (features.values ()))[1:]

    # for debugging and ensuring the data is in the right order
    print (row)

    # predict using that model 
    prediction = model.predict ([ row ])[0]
    print ("Prediction", prediction)

    if prediction == 1: 
        return 'malignant'
    elif prediction == 0:
        return 'benign'
    else: 
        return 'error'

def result (request): 
    context = {} 

    def add (name): 
        value = request.POST.get (name, 0)
        context[name] = value 
     
    # The order of this sequential 'add' calls matter
    # Please don't reorder  
    add ('id')
    add ('radius')
    add ('texture')
    add ('perimeter')
    add ('area')
    add ('smoothness')
    add ('compactness')
    add ('concavity')
    add ('concave_points')
    add ('symmetry')
    add ('fractal_dimension')

    dignostic = do_classify (context)
    context['diagnostic'] = dignostic 

    return render (request, 'app/result.html', context)