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


def contactProfile(request, pk):
    contact = ContactModel.objects.get(id=pk)
    return render(request, "contact-profile.html", {'contact': contact})


def edit(request, pk):
    contact = ContactModel.objects.get(id=pk)

    if request.method == "POST":
        contact.fullname = request.POST['fullname']
        contact.relationship = request.POST['relationship']
        contact.email = request.POST['email']
        contact.phone = request.POST['phone_number']
        contact.address = request.POST['address']
        contact.save()
        return redirect('/profile/'+str(contact.id))

    return render(request, "edit.html", {'contact': contact})


def delete(request):
    return render(request, "delete.html")