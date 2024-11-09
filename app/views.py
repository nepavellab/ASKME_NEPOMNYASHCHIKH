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
    page, page_count = paginate(QUESTIONS, request, 5)
    return render(request, "index.html", {
        "page": page,
        "page_count": page_count,
        "page_number": page.number
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

def paginate(object_list, request, per_page):
    paginator = Paginator(object_list, per_page)
    current_page_number = int(request.GET.get("page", 1))
    
    if current_page_number > paginator.num_pages:
        current_page_number = paginator.num_pages
    
    page = paginator.page(current_page_number)
    return page, paginator.num_pages