from django.contrib import admin
from .models import Shout, User
from django.utils.html import format_html

@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    def shout_list(self, obj):
        return obj.list_shouts()

    fieldsets = [
        ("User Details", {"fields": ["username", "id", "reg_date", "shout_list"]}),
        ("Social Details", {"fields": ["followers", "following"]}),
    ]

    readonly_fields = ("reg_date", "followers", "following", "id", "shout_list")
   
    list_display = ("username", "followers", "reg_date")
    list_display_links = ("username", "followers", "reg_date")
    search_fields = ("username",)
    
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

    