from django.shortcuts import reverse, redirect, render, get_object_or_404
from django.views import generic
from .forms import UserUzsakymasCreateForm
from django.views.generic.edit import FormMixin
from .models import *
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def index(request):
    return render(request, 'index.html')

class UserTasksListView(LoginRequiredMixin, generic.ListView):
    model = Task
    paginate_by = 4
    template_name = "mytasks.html"
    context_object_name = "mytasks"

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)



class UserTaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    template_name = 'newtask.html'
    success_url = '/mytasks/'
    form_class = UserUzsakymasCreateForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UserTaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Task
    success_url = "/mytasks/"
    template_name = 'newtask.html'
    form_class = UserUzsakymasCreateForm


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        task = self.get_object()
        return self.request.user == task.user


class UserTaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Task
    success_url = "/mytasks/"
    template_name = 'deletetask.html'

    def test_func(self):
        task = self.get_object()
        return self.request.user == task.user


