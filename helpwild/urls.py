from django.shortcuts import render
from . import views
from django.urls import path
from django.urls import reverse
from django.contrib.auth.views import LogoutView

from django.contrib.auth import views as auth_views


app_name = "helpwild"

urlpatterns = [
    # path('home', views.home_page_view, name='home'),

    # Home Page
    path('', views.home_page_view, name='home'),

    # Teams Page
    path('teams/', views.teams_page_view, name='teams'),

    # Timeline Page
    path('timeline/', views.timeline_page_view, name='timeline'),

    # Donation Pages
    path('donate/', views.donate_page_view, name='donate'),
    path('charge/', views.charge, name='charge'),
    path('success/<str:args>/', views.successMsg_page_view, name='success'),

    # News Page
    path('news/', views.news_page_view, name='news'),

    # Quiz&Coments Pages
    path('quiz/', views.quiz_page_view, name='quiz'),
    path('newcomment/', views.new_Comments_view, name='newcomment'),
    path('editcomment/<int:comment_id>',
         views.edit_Comments_view, name='editcomment'),
    path('deletecomment/<int:comment_id>',
         views.delete_Comments_view, name='deletecomment'),

    # Register&Login Pages
    path('register/', views.register_page_view, name="register"),
    path('login/', views.login_page_view, name="login"),
    path('logout/', views.logout_page_view, name='logout'),

    # ProfileUser Page
    path('profile/', views.profile_page_view, name='profile'),

#     path('reset_password/',
#          auth_views.PasswordResetView.as_view(),
#          name="reset_password"), 

#     path('reset_password_sent/',
#          auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),

#     path('password_reset_confirm/<uidb64>/<token>/',
#          auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),

#     path('reset_password_complete/',
#          auth_views.PasswordResetCompleteView.as_view(),
#          name="password_reset_complete"),    

]
