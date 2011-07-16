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
    opts, args = getopt.getopt(sys.argv[1:], "tmn:f:")
    action = ""
    filedata = None
    name = ""
    import pdb; pdb.set_trace()
    for o in opts:
        if o[0] == "-t":
            action = "t"
        elif o[0] == "-m":
            action = "m"
        elif o[0] == "-n":
            name = o[1]
        elif o[0] == "-f":
            filedata = o[1]
    if action == "t":
        if (filedata != None and name != ""):
            train(name, filedata)
    elif action == "m":
        if (name != ""):
            match(filedata)
    return 0

def train(model_name, svmdata):
    import pdb; pdb.set_trace()
    y,x = svmutil.svm_read_problem(svmdata)
    problem = svmutil.svm_problem(y,x)
    #params?
    model = svmutil.svm_train(problem, None);
    modelname = model_name
    svmutil.svm_save_model(modelname, model)
    return 0

def match(svmdata):
    dirname="../model/"

    y,x = svmutil.svm_read_problem(svmdata)
    problem = svmutilsvm_problem(y,x)
    for f in os.listdir(dirname):
        if (os.path.isfile(os.path.join(dirname, f))):
            m = svmutil.svm_load_model(f);
            labels, accuracy, values = svmutil.svm_predict(y,x,m,None)
    # We'll see if the labels work, and what they return, and we'll classify from there
    return 0


if __name__ == "__main__":
    main()
