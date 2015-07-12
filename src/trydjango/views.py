from django.shortcuts import render

def about(request):
    return render(request, "about.html", {})

def login(request):
    return render(request, "login.html", {})

def contact(request):
    return render(request, "contact.html", {})

def register(request):
    return render(request, "register.html", {})

def checkout(request):
    return render(request, "checkout.html", {})