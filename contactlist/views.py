from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "index.html")


def addcontact(request):
    return render(request, "addcontact.html")


def edit(request):
    return render(request, "edit.html")


def delete(request):
    return render(request, "delete.html")


def contact_profile(request):
    return render(request, "contact-profile.html")
