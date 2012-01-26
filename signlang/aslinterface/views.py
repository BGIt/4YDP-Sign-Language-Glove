from django.template import Context, loader
from django.http import HttpResponse

def home(request):
    t = loader.get_template('signlang/index.html')
    c = Context({ 'test': 10 })
    return HttpResponse(t.render(c))




