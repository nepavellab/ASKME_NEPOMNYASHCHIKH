from django.shortcuts import render


def main_page(request):    
    return render(request, "index.html", {})

def question_page(request):
    return render(request, "ask.html", {})

def login_page(request):
    return render(request, "login.html", {})

def registration_page(request):
    return render(request, "signup.html", {})

def user_settings_page(request):
    return render(request, "settings.html", {})