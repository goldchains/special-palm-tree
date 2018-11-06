import pandas as pd
import numpy as np
import sys
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn import linear_model
from sklearn.externals import joblib

args = sys.argv
if(len(args) == 3):
    logreg = joblib.load('logregbcotest1.joblib') 
    outcome = logreg.predict(np.array(float(args[2])).reshape(-1, 1))
    
elif(len(args) == 4):
    logreg2 = joblib.load('logregbcotest2.joblib') 
    outcome = logreg2.predict(np.array([float(args[2]), float(args[3])]).reshape(1, -1))

if(outcome[0] == False):
    print("Student requires assistance")
elif(outcome[0] == True):
    print("Student is progressing well")