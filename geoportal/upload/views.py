from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView
from django.core.files.storage import FileSystemStorage
from .models import UploadFile
from .form import UploadForm


class Home(TemplateView):
    template_name = 'base.html'

class UploadView(CreateView):
    model = UploadFile
    template_name = 'upload_view.html'
    form_class = UploadForm
    # TODO change to list
    success_url = reverse_lazy('upload')

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        # form.save()
        return super().form_valid(form)

class ListView(ListView):
    model = UploadFile
    template_name = 'list_view.html'
    context_object_name = 'upload'