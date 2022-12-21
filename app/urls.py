from app import views
from django.urls import path

urlpatterns = [
    path('question/<int:question_id>', views.question, name='question'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('settings', views.settings, name='settings'),
    path('ask', views.ask, name='ask'),
    path('hot', views.hot, name='hot'),
    path('tag/<tag_name>', views.tag, name='tag')
]
