"""django_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from app import views

urlpatterns = [
    path("", views.LandingPage.as_view(), name="landing"),
    path("jobs/", views.JobPage.as_view(), name="jobs"),
    path("admin/", views.AdminPage.as_view(), name="admin"),
    path("students", views.Students.as_view(), name="students"),
    path(
        "jobs/<int:id>", views.IndivdualJobPage.as_view(), name="single-jobs"),
    path('posts/create/', views.NewPostCreate.as_view(), name='new-post'),
    path('posts/<int:id>/', views.BlogPostDetail.as_view(), name='blog-post'),
    path(
        'posts/<int:id>/delete',
        views.BlogPostDelete.as_view(),
        name='delete-job'),
    path(
        'posts/<int:id>/comment',
        views.MakingComments.as_view(),
        name='make-comment'),
    path(
        'posts/<int:id>/delete/comment',
        views.CommentDelete.as_view(),
        name='delete-comment')
]
