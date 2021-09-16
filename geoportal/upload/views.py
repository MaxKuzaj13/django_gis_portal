from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView
from django.core.files.storage import FileSystemStorage


class Home(TemplateView):
    template_name = 'base.html'

def upload(request):
    if request.method == 'POST':
        print('test')
        uploaded_file = request.FILES['document']
        print(uploaded_file.name)
        print(uploaded_file.size)
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    return render(request, 'upload_view.html')

# class UpladView