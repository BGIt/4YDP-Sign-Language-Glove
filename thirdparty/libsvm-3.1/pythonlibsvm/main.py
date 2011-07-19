import sys
import getopt
from pythonlibsvm import svmutil

"""
There are 2 flags for this,
-t - Creates/updates a new model and returns it into the file name that was specified as the second argument.
-m - Matches test data to the model
-name - name of the model
-file - the data file that is being ported
"""
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
    return 0

def train(model_name, svmdata):
    y,x = svmutil.svm_read_problem(svmdata)
    problem = svmutil.svm_problem(y,x)
    param = svmutil.svm_parameter('-t 2 -c 4 -g 0.5')
    model = svmutil.svm_train(problem, param);
    modelname = model_name
    svmutil.svm_save_model(modelname, model)
    return 0

def match(svmdata, modeldata):
    y,x = svmutil.svm_read_problem(svmdata)
    problem = svmutil.svm_problem(y,x)
    m = svmutil.svm_load_model(modeldata);
    labels, accuracy, values = svmutil.svm_predict(y,x,m)
    # We'll see if the labels work, and what they return, and we'll classify from there
    import pdb;pdb.set_trace()
    return 0


if __name__ == "__main__":
    main()
