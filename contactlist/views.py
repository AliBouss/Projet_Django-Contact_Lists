from django.shortcuts import render, redirect
from .models import ContactModel

# Create your views here.


def index(request):
    contacts = ContactModel.objects.all()

    return render(request, "index.html", {"contacts": contacts})


def addcontact(request):
    if request.method == "POST":
        new_contact = ContactModel(
            fullname=request.POST['fullname'],
            relationship=request.POST['relationship'],
            email=request.POST['email'],
            phone=request.POST['phone_number'],
            address=request.POST['address']
        )
        new_contact.save()
        return redirect("/")

    return render(request, "addcontact.html")


def edit(request):
    return render(request, "edit.html")


def delete(request):
    return render(request, "delete.html")


def contact_profile(request):
    return render(request, "contact-profile.html")
