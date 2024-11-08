from django.shortcuts import render


def main_page(request):    
    return render(request, "index.html", {})

def ask_page(request):
    return render(request, "ask.html", {})

def login_page(request):
    return render(request, "login.html", {})

def registration_page(request):
    return render(request, "signup.html", {})

def user_settings_page(request):
    return render(request, "settings.html", {})

def question_page(request):
    return render(request, "question.html", {})

def tag_page(request):
    return render(request, "tag.html", {})