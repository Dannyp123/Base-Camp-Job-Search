from django.shortcuts import render
from django.views import View
from app import forms
from app import models
from django.shortcuts import redirect, render


# Create your views here.
class HomePage(View):
    def get(self, request):
        return render(request, "home.html",
                      {"job_post": models.BlogPost.objects.all()})


class Students(View):
    def get(self, request):
        return render(request, "students.html")


class NewPostCreate(View):
    def get(self, request):
        return render(request, 'new-post.html', {'form': forms.BlogPostForm()})

    def post(self, request):
        form = forms.BlogPostForm(data=request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            location = form.cleaned_data["location"]
            postion = form.cleaned_data["postion"]
            benefits = form.cleaned_data["benefits"]
            body = form.cleaned_data['body']
            models.BlogPost.submit_post(title, author, location, postion,
                                        benefits, body)
            return redirect('home')
        else:
            return render(request, 'new-post.html', {'form': form})


class BlogPostDetail(View):
    def get(self, request, id):
        return render(request, 'blog-post.html',
                      {'job_post': models.BlogPost.objects.get(id=id)})


class BlogPostDelete(View):
    def post(self, request, id):
        models.BlogPost.objects.get(id=id).delete()
        return redirect("home")


class MakingComments(View):
    def get(self, request, id):
        return render(request, 'comment.html',
                      {"form": forms.BlogCommentForm()})

    def post(self, request, id):
        form = forms.BlogCommentForm(data=request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            body = form.cleaned_data['body']
            models.BlogComment.submit_comment(title, body, author, id)
            return redirect('home')
        else:
            return render(request, 'comment.html', {'form': form})
