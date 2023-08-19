from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm

# Create your views here.

class TodoListView(ListView):
    model = Task
    template_name = 'list.html'

# class TodoDetailView(DetailView):
#     model = Task
#     template_name = 'detail.html'
# <!-- <h4><li> <a href="{% url 'td_detail' todo.id %}"> {{ todo.title }} </a> | {{ todo.created }} </li></h4> -->
# <!-- <h4><li> {{ todo.completed }} | <a href="{% url 'td_detail' todo.id %}">{{ todo.title }}</a> | {{ todo.created }} </li></h4> -->

class TodoCreateView(CreateView):
    model = Task
    template_name = 'create.html'
    fields = ['title']

class TodoUpdateView(UpdateView):
    model = Task
    template_name = 'update.html'
    fields = ['title', 'completed']

class TodoDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('td_list')