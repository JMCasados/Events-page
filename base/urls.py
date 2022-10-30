from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('user/<str:pk>', views.user_page, name="profile"),
    path('account/', views.account_page, name="account"),
    path('event/<str:pk>/', views.event_page, name="event"),
    path('project-submission/<str:pk>', views.project_submission, name="project-submission"),
    path('event-confirmation/<str:pk>', views.registration_confirmation, name="registration_confirmation"),
    path('update-submission/<str:pk>', views.update_submission, name="update-submission"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_page, name="register"),

]
