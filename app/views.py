from django.shortcuts import render

# Create your views here.
from app.models import *

from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

from django.urls import reverse_lazy

class Schoollist(ListView):
    model=School
    context_object_name='schools'
    ordering=['sname']
    #queryset=School.objects.filter(id__in=(1,3))
    #template_name='school_list.html'


class Schooldetail(DetailView):
    model=School
    context_object_name='SO'


class SchoolCreate(CreateView):
    model=School
    fields='__all__'


class SchoolUpdate(UpdateView):
    model=School
    fields='__all__'


class SchoolDelete(DeleteView):
    model=School
    context_object_name='sclobj'
    success_url=reverse_lazy('Schoollist')
