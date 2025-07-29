
from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, BlogPost, Skill
from django.contrib import messages


def home(request):
    projects = Project.objects.all()
    blog = BlogPost.objects.all()
    skills = Skill.objects.all()

    return render(request, 'home.html', {'projects': projects,'blog_posts': blog,         'skills': skills,
  # match the template variable
})

def blog(request):
    posts = BlogPost.objects.order_by('-created_at')
    return render(request, "blog.html", {"blog_posts": posts})

def blog_detail(request, slug):
    blog = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'blog_details.html', {'blog': blog})

def projects(request):
    projects = Project.objects.all()
    return render(request, "projects.html", {"projects": projects})

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'project_details.html', {'project': project})

def contact(request):
    return render(request, "contact.html")

def send_message(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        print("Message received:", name, email, message)
        # Optional: add logic to email/save/etc.
        return redirect("contact")
    return redirect("contact")