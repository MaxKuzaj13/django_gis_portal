from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.core.files.storage import FileSystemStorage
from .models import UploadFile
from .form import UploadForm
from django.contrib.auth.forms import UserCreationForm


class Main(TemplateView):
    template_name = 'templates/base.html'
    #
    # def dispatch(self, request, *args, **kwargs)
    #     if not request.user.is_authenticated():
    #         return reverse_lazy('upload')

class UploadView(CreateView):
    model = UploadFile
    template_name = 'upload/upload_view.html'
    form_class = UploadForm
    # TODO change to list
    success_url = reverse_lazy('upload')

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        # form.save()
        return super().form_valid(form)

class ListView(ListView):
    # List View- list all info
    model = UploadFile
    template_name = 'upload/list_view.html'
    context_object_name = 'upload'

class DetailView(DetailView):
    # Detail View
    model = UploadFile
    template_name = 'upload/detail_view.html'
    context_object_name = 'detail_view'
