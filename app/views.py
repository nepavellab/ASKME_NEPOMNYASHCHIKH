from django.shortcuts import render
from django.core.paginator import Paginator
from random import randint

# ! Для тестов без базы данных
QUESTIONS = [
    {
        "id": i,
        "title": f"Вопрос №{i}",
        "answer_count": randint(0, 1000),
        "text": f"Здесь располагается основной текст вопроса №{i}, описывающий проблематику задачи",
        "tags": [f"Тэг №{j}-{i}" for j in range(1, 6)] 
    } for i in range(1, 21)
]

def main_page(request):
    return render(request, "index.html", {
        "questions": QUESTIONS
    })

def ask_page(request):
    return render(request, "ask.html", {})

def login_page(request):
    return render(request, "login.html", {})

def registration_page(request):
    return render(request, "signup.html", {})

def user_settings_page(request):
    return render(request, "settings.html", {})

def question_page(request, question_id):
    current_question = QUESTIONS[question_id-1]
    return render(request, "question.html", {
        "question": current_question
    })

def tag_page(request):
    return render(request, "tag.html", {
        "questions": QUESTIONS
    })

def paginate(objects_list, request, per_page=10):
    # do smth with Paginator, etc…
    #return page
    pass