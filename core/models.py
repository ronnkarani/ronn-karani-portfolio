from django.db import models
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import Truncator

# Create your models here.
class Hero(models.Model):
    greeting = models.CharField(max_length=255, default="Hi 👋, I'm")
    name = models.CharField(max_length=255, default="Ronny Karani")
    emoji = models.CharField(max_length=10, default="👨‍💻", blank=True, null=True)
    headline = RichTextUploadingField(blank=True, null=True, max_length=255, default="A Full-Stack Software Engineer, Building Scalable &  Impact-Driven Digital Solutions")
    subtext_1 = RichTextUploadingField(blank=True, null=True)
    subtext_2 = RichTextUploadingField(blank=True, null=True)
    subtext_3 = RichTextUploadingField(blank=True, null=True)

    resume = models.FileField(upload_to="resumes/", blank=True, null=True)
    profile_image = models.ImageField(upload_to="hero/", default="ron.jpeg", blank=True, null=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Hero Section ({self.name})"

class About(models.Model):
    title = models.CharField(max_length=255, default="📂 About Me ")
    tagline = RichTextUploadingField(max_length=255, blank=True, null=True)  # “Creative Developer • Tech Visionary”
    description_1 = RichTextUploadingField(blank=True, null=True)
    description_2 = RichTextUploadingField(blank=True, null=True)
    description_3 = RichTextUploadingField(blank=True, null=True)

    tech_stack = RichTextUploadingField(
        help_text="Enter tech stack details in plain text or HTML (e.g., <b>Frontend:</b> React, Tailwind)",
        blank=True,
        null=True
    )

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"About Section (Last updated: {self.updated_at.date()})"
class SocialLink(models.Model):
    PLATFORM_CHOICES = [
        ("facebook", "Facebook"),
        ("twitter", "Twitter"),
        ("linkedin", "LinkedIn"),
        ("github", "GitHub"),
        ("instagram", "Instagram"),
        ("youtube", "YouTube"),
    ]

    platform = models.CharField(max_length=50, choices=PLATFORM_CHOICES)
    url = models.URLField()

    def __str__(self):
        return f"{self.get_platform_display()} - {self.url}"
    
class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = RichTextUploadingField()
    image = models.ImageField(upload_to='projects/')
    technologies = models.TextField(help_text="Comma-separated list")
    repo_url = models.URLField(blank=True, null=True)
    live_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def tech_list(self):
        return [tech.strip() for tech in self.technologies.split(',')]

    def __str__(self):
        return self.title

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    excerpt = models.TextField(blank=True, null=True)
    content = RichTextUploadingField()
    image = models.ImageField(upload_to='blogs/')
    author = models.CharField(max_length=100, default="Ronny")
    created_at = models.DateField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        # auto-generate excerpt if empty
        if not self.excerpt:
            plain_text = self.content.replace("<p>", "").replace("</p>", "")  # remove HTML tags roughly
            self.excerpt = Truncator(plain_text).words(30)  # first 30 words
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Skill(models.Model):
    icon = models.CharField(max_length=10, help_text="Emoji or Icon")
    category = models.CharField(max_length=100, help_text="Category e.g. Frontend")
    stack = RichTextUploadingField(help_text="Tech stack or description")

    def __str__(self):
        return f"{self.icon} {self.category}"
    
class Comment(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # This will work for either a project or blog
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True, related_name="comments")
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE, null=True, blank=True, related_name="comments")

    def __str__(self):
        return f"Comment by {self.name}"

