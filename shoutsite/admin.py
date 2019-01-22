from django.contrib import admin
from .models import Shout
from django.utils.html import format_html

@admin.register(Shout)
class ShoutAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Shout Details", {"fields": ["shout_text", "user", "pub_date", "id"]}),
        ("Social Details", {"fields": ["likes"]}),
    ]

    readonly_fields = ("pub_date", "user", "likes", "id")

    list_display = ("id", "user", "likes", "pub_date")
    list_display_links = ("id", "user", "likes", "pub_date")
    search_fields = ("user__username",)
