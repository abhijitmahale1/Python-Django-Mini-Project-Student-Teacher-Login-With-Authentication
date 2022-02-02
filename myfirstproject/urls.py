from django.contrib import admin
from django.urls import path,include
from .import views
	
urlpatterns = [
	path('',views.index,name="index"),
    path('register',views.register,name="register"),
    path('save_data',views.save_data,name="save_data"),
    path('login1',views.login1,name="login1"),
    path('login_check',views.login_check,name="login_check"),
    path('welcome',views.welcome,name="welcome"),
    path('delete',views.delete,name="delete"),
    path('edit',views.edit,name="edit"),
    path('update',views.update,name="update"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('logout1',views.logout1,name="logout1"),

    path('form', views.form, name="form"),
# authontication
    path('auth_registration', views.auth_registration, name="auth_registration"),
    path('auth_save', views.auth_save, name="auth_save"),

    path('auth_login', views.auth_login, name="auth_login"),
    path('auth_login_check', views.auth_login_check, name="auth_login_check"),

    path('auth_logout', views.auth_logout, name="auth_logout"),

    path('reset', views.reset, name="reset"),
    path('reset_pass', views.reset_pass, name="reset_pass"),


]