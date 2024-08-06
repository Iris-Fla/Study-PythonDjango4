from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import SessionForm

# Create your views here.
class Helloview(TemplateView):
    def __init__(self):
        self.params = {
            'title':'Hello',
            'form':SessionForm(),
            "result":None
        }
    def get(self, request):
        self.params['result'] = request.session.get('last_msg',"noone")
        return render(request, 'hello/index.html', self.params)
    def post(self, request):
        ses = request.POST['session']
        self.params['result'] = ses
        self.params['form'] = SessionForm(request.POST)
        return render(request, 'hello/index.html', self.params)