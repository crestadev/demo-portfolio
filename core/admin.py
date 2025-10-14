from django.contrib import admin
from .models import Testimonial, ContactMessage

from .models import Profile

from django.contrib import admin
from .models import Profile, Skill, Experience, Education, ContactMessage, Testimonial

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'title', 'email', 'location')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'profile')
    list_filter = ('profile',)
    search_fields = ('name',)

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('position', 'company', 'start_year', 'end_year', 'profile')
    list_filter = ('profile',)

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'year', 'profile')
    list_filter = ('profile',)
    
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'role', 'created_at')
    search_fields = ('client_name', 'role')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')