from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")


def edit(request):
    return render(request, "edit.html")


def new(request):
    return render(request, "new.html")


def delete(request):
    return render(request, "delete.html")


def contact_profile(request):
    return render(request, "contact-profile.html")
