from django.shortcuts import render
from blog.models import Post, Comment, Contact
from .forms import CommentForm, ContactForm
from django.views.generic import TemplateView, ListView, View
from django.contrib import messages

# Create your views here.

class about(View):
    template_name = "about.html"

    def get(self, request):
        return render(request, self.template_name)


class contact(View):
    template_name = "contact.html"
    form = ContactForm()
    context = {
        "form": form,
    }

    def get(self, request):
        return render(request, self.template_name, self.context)
    
    def post(self, request):
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            cn = Contact(
                name=form.cleaned_data["name"],
                email=form.cleaned_data["email"],
                phone=form.cleaned_data["phone"],
                address=form.cleaned_data["address"],
                message=form.cleaned_data["message"],
                userfile=form.cleaned_data["userfile"],
            )
            cn.save()
            messages.success(request, "Thank You For Contacting Us.")
            return render(request, self.template_name, self.context)
        return render(request, self.template_name, {'form' : form})


def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts": posts,
    }
    return render(request, "blog_index.html", context)


def blog_category(request, category):
    posts = Post.objects.filter(categories__name__contains=category).order_by(
        "-created_on"
    )
    context = {"category": category, "posts": posts}
    return render(request, "blog_category.html", context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)

    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }
    return render(request, "blog_detail.html", context)
