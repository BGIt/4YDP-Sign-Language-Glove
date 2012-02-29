import sys
import getopt
import serial
import array
from svmutil import *
from collections import deque

"""
There are 2 flags for this,
-t - Creates/updates a new model and returns it into the file name that was specified as the second argument.
-p - Predicts a given set of data from a text file.
-r - Predicts a constant stream of serial data.
-m - the model file that will be used
-g - the model file used for neutral check.
-n - name of the model
-f - the data file that will be used
"""

dict = { 1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H' }

def main():
    #Read the options
    opts, args = getopt.getopt(sys.argv[1:], "tprn:f:m:g:")
    action = ""
    filedata = None
    name = ""
    model = ""
    garbage = ""
    for o in opts:
        if o[0] == "-t":
            action = "t"
        elif o[0] == "-p":
            action = "p"
        elif o[0] == "-r":
            action = "r"
        elif o[0] == "-n":
            name = o[1]
        elif o[0] == "-f":
            filedata = o[1]
        elif o[0] == "-m":
            model = o[1]
        elif o[0] == "-g":
            garbage = o[1]

    if action == "t":
        if (filedata != None and name != ""):
            train(name, filedata)
    elif action == "p":
        if (filedata != "" and model != ""):
            match(filedata, model)
    elif action == "r":
        if (model != "" and garbage != ""):
            runmatch(model, garbage)
    else:
        print ("No option selected, please take a look at the comments in order to learn about the options available")
    return 0

def train(model_name, svmdata):
    y,x = svm_read_problem(svmdata)
    problem = svm_problem(y,x)
    param = svm_parameter('-s 0 -t 2 -g 0.0007 -q')
    model = svm_train(problem, param)
    modelname = model_name
    svm_save_model(modelname, model)
    return 0

def match(svmdata, modeldata):
    y,x = svm_read_problem(svmdata)
    import pdb;pdb.set_trace()
    m = svm_load_model(modeldata)
    labels, accuracy, values = svm_predict(y,x,m)
    # We'll see if the labels work, and what they return, and we'll classify from there
    return 0

def runmatch(modeldata, garbage):
    ser = serial.Serial (3)
    m = svm_load_model(modeldata)
    g = svm_load_model(garbage)
    window = deque()
    predictions = deque()
    consume = False
    while 1:
        output = ser.readline()
        data = output.split(' ')
        datadict = {}
        for i in range(len(data)-1):
            key,value = data[i].split(':')
            datadict[int(key)] = float(value)
        #labels, accuracy, values = svm_predict(y,data[:len(data)-1],m)
        y = [i]
        x = [datadict]
        guess = 0
        label = 0
        labels, accuracy, values = svm_predict(y,x,g)
        if int(labels[0]) != 0:
            #check error if it's low accept it
            window.appendleft(1)
        else:
            window.appendleft(0)
        if len(window) > 5:
            window.pop()
        #update this to check prediciton list as well
        #print window
        #print 'Window sum' + str(sum(window))
        #print predictions
        if sum(window) > 3 and consume == False:
            #print 'Window' + windows
            #print 'Window sum' + sum(window)
            #print 'Predictions' + predictions
            labels, accuracy, values = svm_predict(y,x,m)
            print dict[int(labels[0])]
            consume = True
        if sum(window) < 3 and consume == True:
            consume = False

def runmatchgui(modeldata, garbage):
    ser = serial.Serial (3)
    m = svm_load_model(modeldata)
    g = svm_load_model(garbage)
    window = deque()
    predictions = deque()
    consume = False
    while 1:
        output = ser.readline()
        data = output.split(' ')
        datadict = {}
        for i in range(len(data)-1):
            key,value = data[i].split(':')
            datadict[int(key)] = float(value)
        #labels, accuracy, values = svm_predict(y,data[:len(data)-1],m)
        y = [i]
        x = [datadict]
        guess = 0
        label = 0
        labels, accuracy, values = svm_predict(y,x,g)
        if int(labels[0]) != 0:
            #check error if it's low accept it
            window.appendleft(1)
        else:
            window.appendleft(0)
        if len(window) > 5:
            window.pop()
        #update this to check prediciton list as well
        #print window
        #print 'Window sum' + str(sum(window))
        #print predictions
        if sum(window) > 3 and consume == False:
            #print 'Window' + windows
            #print 'Window sum' + sum(window)
            #print 'Predictions' + predictions
            labels, accuracy, values = svm_predict(y,x,m)
            print dict[int(labels[0])]
            consume = True
            return dict[int(labels[0])]
        if sum(window) < 3 and consume == True:
            consume = False

def sumdeque(value):
    for i in range(len(value)):
        summed += i
    return summed

if __name__ == "__main__":
    main()
