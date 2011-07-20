import sys
import getopt
import serial
from pythonlibsvm import svmutil
from collections import deque

"""
There are 2 flags for this,
-t - Creates/updates a new model and returns it into the file name that was specified as the second argument.
-p - Predicts a given set of data from a text file.
-r - Predicts a constant stream of serial data.
-m - the model file that will be used
-n - name of the model
-f - the data file that will be used
"""
ser = serial.Serial (3)

def main():
    #Read the options
    opts, args = getopt.getopt(sys.argv[1:], "tpn:f:m:")
    action = ""
    filedata = None
    name = ""
    model = ""
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

    if action == "t":
        if (filedata != None and name != ""):
            train(name, filedata)
    elif action == "p":
        if (filedata != "" and model != ""):
            match(filedata, model)
    elif action == "r":
        if (model != ""):
            runmatch(model)
    else:
        print ("No option selected, please take a look at the comments in order to learn about the options available")
    return 0

def train(model_name, svmdata):
    y,x = svmutil.svm_read_problem(svmdata)
    problem = svmutil.svm_problem(y,x)
    param = svmutil.svm_parameter('-s 0 -t 2 -g 0.0007')
    model = svmutil.svm_train(problem, param)
    modelname = model_name
    svmutil.svm_save_model(modelname, model)
    return 0

def match(svmdata, modeldata):
    y,x = svmutil.svm_read_problem(svmdata)
    m = svmutil.svm_load_model(modeldata)
    labels, accuracy, values = svmutil.svm_predict(y,x,m)
    # We'll see if the labels work, and what they return, and we'll classify from there
    import pdb;pdb.set_trace()
    return 0

def runmatch(modeldata):
    m = svmutil.svm_load_model.model(data)
    window = deque()
    consume = False
    while 1:
        output = ser.readline()
        data = output.split(',')
        y = arange(len(data),1,1)
        labels, accuracy, values = svmutil.svm_predict(y,x,m)
        window.appendleft(accuracy)
        if len(window) > 5:
            window.pop()
        if sum(window) > 3 and consume == False:
            print label
            consume = True
        if sum(window) < 2 and consume == True:
            consume = False

def sumdeque(value):
    for i in range(len(value)):
        summed += i
    return summed

if __name__ == "__main__":
    main()
