from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'fileo/index.html')

@login_required(login_url='login')
def myfiles(request):
    context = {'files': list(range(1, 100))}
    return render(request, 'fileo/myfiles.html', context)

def download(request):
    context = {'file_path': '/yeet.txt'}
    return render(request, 'fileo/download.html', context)
