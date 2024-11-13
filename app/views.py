from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# ! Для тестов без базы данных
QUESTIONS = [
    {
        "id": i,
        "title": f"Вопрос №{i}",
        "answer_count": 100,
        "text": f"Здесь располагается основной текст вопроса №{i}, описывающий проблематику задачи",
        "answers": [f"Здесь располагается ответ №{j + 1} на вопрос №{i}" for j in range(100)],
        "tags": [f"Тэг №{j}-{i}" for j in range(1, 6)]
    } for i in range(1, 201)
]

def main_page(request):
    page, page_count = paginate(QUESTIONS, request, 5)
    return render(request, "index.html", {
        "page": page,
        "page_count": page_count,
        "page_number": page.number
    })
    
def hot_page(request):
    page, page_count = paginate(QUESTIONS, request, 5)
    return render(request, "hot.html", {
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
    page, page_count = paginate(current_question["answers"], request, 5)
    return render(request, "question.html", {
        "question": current_question,
        "page": page,
        "page_count": page_count,
        "page_number": page.number
    })

def tag_page(request):
    return render(request, "tag.html", {
        "questions": QUESTIONS
    })

def paginate(object_list, request, per_page):
    paginator = Paginator(object_list, per_page)
    
    try:
        current_page_number = request.GET.get("page", 1)
        page = paginator.page(current_page_number)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    
    return page, paginator.num_pages