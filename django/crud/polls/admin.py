from django.contrib import admin
from .models import Questions, Choices

admin.site.site_header = "Pollster Admin"
admin.site.site_title = "Pollster"
admin.site.index_title = "Welcome To Pollster"

class ChoiceInline(admin.TabularInline):
    model = Choices
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['Questions_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Questions, QuestionAdmin)
