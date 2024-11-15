from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Question, Answer, Tag
from typing import Final


all_tags: Final = Tag.objects.distinct().order_by('name')

def main_page(request):
    questions = Question.objects.all()
    page, page_count = paginate(questions, request, 5)
    return render(request, "index.html", {
        "page": page,
        "page_count": page_count,
        "page_number": page.number,
        "all_tags": all_tags
    })
    
def hot_page(request):
    hot_questions = Question.objects.order_by('-created_at')
    page, page_count = paginate(hot_questions, request, 5)
    return render(request, "hot.html", {
        "page": page,
        "page_count": page_count,
        "page_number": page.number,
        "all_tags": all_tags
    })

def ask_page(request):
    return render(request, "ask.html", {
        "all_tags": all_tags
    })

def login_page(request):
    return render(request, "login.html", {
        "all_tags": all_tags
    })

def registration_page(request):
    return render(request, "signup.html", {
        "all_tags": all_tags
    })

def user_settings_page(request):
    return render(request, "settings.html", {
        "all_tags": all_tags
    })

def question_page(request, question_id):
    current_question = get_object_or_404(Question, id=question_id)
    answers = Answer.objects.filter(question=current_question)
    page, page_count = paginate(answers, request, 5)
    return render(request, "question.html", {
        "question": current_question,
        "page": page,
        "page_count": page_count,
        "page_number": page.number,
        "all_tags": all_tags
    })

def tag_page(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name)
    tag_questions = Question.objects.filter(tags=tag)
    page, page_count = paginate(tag_questions, request, per_page=5)
    
    return render(request, "tag.html", {
        "current_tag_name": tag_name,
        "page": page,
        "page_count": page_count,
        "page_number": page.number,
        "all_tags": all_tags
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