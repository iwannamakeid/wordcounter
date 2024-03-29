"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import myapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('', myapp.views.main, name='main'),
    # id는 꺾쇠: post_id는 변수로
    path ('<int:post_id>', myapp.views.detail, name='detail'),
    path('create/', myapp.views.create, name="create"),
    path('<int:post_id>/delete',myapp.views.delete, name='delete'),
    path('<int:post_id>/edit',myapp.views.edit, name='edit'),
    path('<int:post_id>/comment', myapp.views.comment_create, name='comment'),
    path('result', myapp.views.result, name='result'),

]
