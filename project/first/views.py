
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView, View, CreateView, DeleteView
from django.urls import reverse_lazy
from first.models import Tomat, Oder
from .forms import OderForm


# Create your views here.

def first(request):
    return HttpResponse('<h1>qwe</h1>')


def second(request):
    lst = {'qwe235435554':'zxc532523235','qwe':123,True:'asw'}
    return JsonResponse(lst)


def hello(request):
    context = {'name' : 'zxc'}
    return render(request,'first/hello.html',context=context)


def tomat(request,pk):
    tomat = Tomat.objects.get(id=pk)
    context = {'object' : tomat}

    return render(request,'first/tomato.html',context=context)

def tomatt(request,color):
    tomat = Tomat.objects.get(color=color)
    context = {'object' : tomat}

    return render(request,'first/tomato.html',context=context)

def tomati(request):
    print(request.GET)
    tomat = Tomat.objects.all()
    color = request.GET.get('color')
    min_price = request.GET.get('min_price')
    if min_price:
        tomat = tomat.filter(price__gt=min_price)
    if color:
        tomat = tomat.filter(color=color)
    
    context = {'object_list' : tomat}

    return render(request,'first/tomat_list.html',context=context)



class TomatoListView(ListView):
    model = Tomat


class TomatView(DetailView):
    model = Tomat
    template_name = 'first/tomato.html'


class CreateTomatView(CreateView):
    model = Tomat
    fields = '__all__'
    success_url = reverse_lazy('list')


class DeleteTomatView(DeleteView):
    model = Tomat
    template_name = 'first/deletetomato.html'
    success_url = reverse_lazy('list')

class CreateOderView(CreateView):
    template_name = 'first/oder_form.html'
    form_class = OderForm
    success_url = reverse_lazy('list')
