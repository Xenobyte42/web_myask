from django.urls import path
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.MainPage.as_view(), name='main_page'),
    path('hot/', views.HotPage.as_view(), name='hot_page'),
    path('tag/<str:tag_name>/', views.TagPage.as_view(), name='tag_page'),
    path('question/<int:question_id>/', views.QuestionPage.as_view(), name='quest_page'),
    path('login/', LoginView.as_view(), name='login_page'),
    path('logout/', LogoutView.as_view(), name='logout_page'),
    path('signup/', views.SignupPage.as_view(), name='signup_page'),
    path('ask/', views.AskPage.as_view(), name='ask_page'),
    path('settings/', views.SettingsPage.as_view(), name='settings_page')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
