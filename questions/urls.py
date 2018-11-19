from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('hot/', views.hot_page, name='hot_page'),
    path('tag/<str:tag_name>/', views.tag_page, name='tag_page'),
    path('question/<int:question_id>/', views.question_page, name='quest_page'),
    path('login/', views.login_page, name='login_page'),
    path('signup/', views.signup_page, name='signup_page'),
    path('ask/', views.ask_page, name='ask_page'),
    path('settings/', views.settings_page, name='settings_page')
]
 
