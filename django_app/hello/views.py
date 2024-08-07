from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import redirect
from .models import Friend
from .forms import FriendForm,HelloForm,FindForm
from django.views.generic import DetailView, ListView


class FriendList(ListView):
    model = Friend

class FriendDetail(DetailView):
    model = Friend

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
    if (request.method == 'POST'):
        obj = Friend()
        friend = FriendForm(request.POST,instance=obj)
        friend.save()
        return redirect(to='/hello')
    params = {
        'title':'Hello',
        'form':FriendForm(),
    }
    return render(request, 'hello/create.html', params)

def edit(request,num):
    obj = Friend.objects.get(id=num)
    if (request.method == 'POST'):
        friend = FriendForm(request.POST,instance=obj)
        friend.save()
        return redirect(to='/hello')
    params = {
        'title':'Hello',
        'id':num,
        'form':FriendForm(instance=obj),
    }
    return render(request, 'hello/edit.html', params)

def delete(request,num):
    friend = Friend.objects.get(id=num)
    if (request.method == 'POST'):
        friend.delete()
        return redirect(to='/hello')
    params = {
        'title':'Hello',
        'id':num,
        'obj':friend,
    }
    return render(request, 'hello/delete.html', params)

def find(request):
    if (request.method == 'POST'):
        form = FindForm(request.POST)
        find = request.POST['find']
        data = Friend.objects.filter(name__contains=find)
        msg = "result:" + str(data.count())
    else:
        msg = 'search words...'
        form = FindForm()
        data = Friend.objects.all()
    params = {
        'title':'Hello',
        'message':msg,
        'form':form,
        'data':data,
    }
    return render(request, 'hello/find.html', params)