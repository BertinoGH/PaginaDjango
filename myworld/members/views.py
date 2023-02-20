from django.http import HttpResponse
from django.template import loader

def index(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())

def quehacer(request):
  template = loader.get_template('quehacer.html')
  return HttpResponse(template.render({}, request))

def origen(request):
  template = loader.get_template('origen.html')
  return HttpResponse(template.render({}, request))
  
def formas(request):
  template = loader.get_template('formas.html')
  return HttpResponse(template.render({}, request))

def campañas(request):
  template = loader.get_template('campañas.html')
  return HttpResponse(template.render({}, request))

def prueba(request):
  template = loader.get_template('prueba.html')
  return HttpResponse(template.render({}, request))