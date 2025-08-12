from django.db import models
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
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
    excerpt = models.TextField()
    content = RichTextUploadingField()
    image = models.ImageField(upload_to='blogs/')
    author = models.CharField(max_length=100, default="Ronny")
    created_at = models.DateField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Skill(models.Model):
    icon = models.CharField(max_length=10, help_text="Emoji or Icon")
    category = models.CharField(max_length=100, help_text="Category e.g. Frontend")
    stack = models.TextField(help_text="Tech stack or description")

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

