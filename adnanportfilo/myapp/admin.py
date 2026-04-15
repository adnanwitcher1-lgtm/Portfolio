from django.contrib import admin
from .models import Project, ProfilePicture, ContactMessage

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    # 'url' ko hata kar naye fields 'github_url' aur 'live_url' add kiye hain
    list_display = ('title', 'github_url', 'live_url') 
    search_fields = ('title', 'description')

@admin.register(ProfilePicture)
class ProfilePictureAdmin(admin.ModelAdmin):
    list_display = ('id', 'image')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    # readonly_fields se messages ko admin panel mein sirf read kiya ja sakega, edit nahi
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('created_at',)