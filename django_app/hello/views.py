from django.shortcuts import render
from .forms import HelloForm, SessionForm
from django.http import HttpRequest
from django.views.generic import TemplateView

# Create your views here.
class HelloView(TemplateView):
    def __init__(self):
        self.params = {
            'title': 'Hello',
            'result': None,
            'form': SessionForm()
        }
    def get(self, request):
        self.params["result"] = request.session.get('last_msg', 'no message.')
        return render(request, 'hello/index.html', self.params)
    def post(self, request):
        ses = request.POST['session']
        self.params['result'] = 'you: "' + ses + '".'
        request.session['last_msg'] = ses
        self.params['form'] = SessionForm(request.POST)
        return render(request, 'hello/index.html', self.params)
        