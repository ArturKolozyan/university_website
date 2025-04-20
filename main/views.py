from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def faculties(request):
    return render(request, 'main/faculties.html')

def admissions(request):
    return render(request, 'main/admissions.html')

def contacts(request):
    return render(request, 'main/contacts.html')