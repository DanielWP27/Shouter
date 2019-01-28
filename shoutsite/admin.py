from django.contrib import admin
from .models import Shout, Profile
from django.utils.html import format_html

@admin.register(Shout)
class ShoutAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Shout Details", {"fields": ["shout_text", "user", "pub_date", "id"]}),
        ("Social Details", {"fields": ["likes"]}),
    ]

    readonly_fields = ("pub_date", "user", "id")

    list_display = ("id", "user", "likes", "pub_date")
    list_display_links = ("id", "user", "likes", "pub_date")
    search_fields = ("user__username",)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Profile Details", {"fields": ["owner", "following"]}),
        ("Social Details", {"fields": ["total_likes", "followers"]}),
    ]

    readonly_fields = ("following", "total_likes", "followers")

    list_display = ("owner", "total_likes", "followers")
    list_display_links = ("owner", "total_likes", "followers")
