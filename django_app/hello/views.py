from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Friend
from .forms import HelloForm

# Create your views here.
def index(request):
    data = Friend.objects.all()
    params = {
        'title':'Hello',
        'message':'',
        'form':HelloForm(),
        'data':[],
    }
    if (request.method == 'POST'):
        num = request.POST['id']
        item = Friend.objects.get(id=num)
        params['data'] = [item]
        params['form'] = HelloForm(request.POST)
    else:
        params['data'] = Friend.objects.all()
    return render(request, 'hello/index.html', params)

def create(request):
    params = {
        'title':'Hello',
        'form':HelloForm(),
    }
    if (request.method == 'POST'):
        name = request.POST['name']
        mail = request.POST['mail']
        gender = 'gender' in request.POST
        age = int(request.POST['age'])
        birthday = request.POST['birthday']
        friend = Friend(name=name,mail=mail,gender=gender,age=age,birthday=birthday)
        friend.save()
    return render(request, 'hello/create.html', params)