from django.contrib import admin
from .models import Project, BlogPost, SocialLink, Skill, About, Hero

@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ("name", "headline", "updated_at")
    ordering = ("-updated_at",)
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    prepopulated_fields = {"slug": ("title",)}

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_at")
    prepopulated_fields = {"slug": ("title",)}

@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ("platform", "url")

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("title", "updated_at")
    ordering = ("-updated_at",)

admin.site.register(Skill)

