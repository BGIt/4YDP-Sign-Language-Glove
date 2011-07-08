import sys
import getopt
from svm import *

"""
There are 2 flags for this,
-t - Creates/updates a new model and returns it into the file name that was specified as the second argument.
-m - Matches test data to the model
"""
def main():
    #Read the options
    opts, args = getopt.getopt(sys.argv[1:], "t:m:h", ["help"])
    for o in opts:
        if o == "-t":
            train(args[0], args[1]);
        elif o == "-m":
            match(args[0]);
    return 0

def train(model_name, svmdata):
    y,x = svm_read_problem(svmdata)
    problem = svm_problem(y,x)
    #params?
    model = svm_train(problem, None);
    modelname = "../model/"+model_name+".model"
    svm_save_model(modelname, model)
    return 0

def match(svmdata):
    dirname="../model/"

    y,x = svm_read_problem(svmdata)
    problem = svm_problem(y,x)
    for f in os.listdir(dirname):
        if (os.path.isfile(os.path.join(dirname, f))):
            m = svm_load_model(f);
            labels, accuracy, values = svm_predict(y,x,m,None)
    # We'll see if the labels work, and what they return, and we'll classify from there
    return 0


if __name__ == "__main__":
    main()
