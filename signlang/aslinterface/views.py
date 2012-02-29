from django.template import Context, loader
from django.http import HttpResponse
from django.utils import simplejson
import time
import logic.py

def home(request):
    t = loader.get_template('signlang/index.html')
    c = Context({ 'test': 10 })
    return HttpResponse(t.render(c))

def getword(request):
    #call function
    result = {"word": "A"}
    #runmatchgui(model, garbage)
    json = simplejson.dumps(result)
    time.sleep(5)
    return HttpResponse(json, mimetype='application/json')





