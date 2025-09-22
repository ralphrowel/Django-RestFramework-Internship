from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Person


class PersonInline(admin.StackedInline):
    model = Person
    can_delete = False
    fk_name = "user"


class UserAdmin(BaseUserAdmin):
    inlines = (PersonInline,)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return []
        return super().get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("user","person_firstname", "person_lastname", "person_contact")
