from django.shortcuts import render


def home(request):
    return render(request, "Sacco/home.html")


def about(request):
    return render(request, "Sacco/about.html")


def services(request):
    return render(request, "Sacco/services.html")


def investo_centre(request):
    return render(request, "Sacco/investo_centre.html")


def contact(request):
    return render(request, "Sacco/contact.html")


def blogs(request):
    return render(request, "Sacco/blogs.html")


def join_us(request):
    return render(request, "Sacco/join_us.html")