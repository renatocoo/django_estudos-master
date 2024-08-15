from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from galeria import views
from django.urls import path


urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='galeria/login.html'), name='login'),
    path("admin/", admin.site.urls),
    path("home/", include('galeria.urls')),
    path('logout/', views.logout_view, name='logout'),
    path('registro/', views.register, name='register'),
]
