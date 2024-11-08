from django.urls import path
from app import views


app_patterns = [
    path("", views.main_page, name="main_page"),
    path("ask/", views.ask_page, name="ask_page"),
    path("login/", views.login_page, name="login_page"),
    path("register/", views.registration_page, name="register_page"),
    path("settings/", views.user_settings_page, name="settings_page"),
    path("question/<int:question_id>", views.question_page, name="question_page"),
    path("tag/", views.tag_page, name="tag_page")
]