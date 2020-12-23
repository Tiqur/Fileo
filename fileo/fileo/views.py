from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'fileo/index.html')

@login_required(login_url='login')
def myfiles(request):
    print("Request: " + request.method)
    context = {'files': list(range(1, 20))}
    if request.method == 'POST' and request.FILES['upload_file']:
        file = request.FILES.get('upload_file')
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        uploaded_file_url = fs.url(filename)
        context['uploaded_file_url'] = uploaded_file_url

    return render(request, 'fileo/myfiles.html', context)

def download(request):
    context = {'file_path': '/yeet.txt'}

