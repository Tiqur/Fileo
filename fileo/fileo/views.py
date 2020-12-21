from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'fileo/index.html')

@login_required(login_url='login')
def files(request):
    return render(request, 'fileo/files.html')



