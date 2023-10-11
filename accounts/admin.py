
# Register your models here.
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin


from .models import Hired, User,Engineer,Labour
from .forms import UserAdminCreationForm, UserAdminChangeForm

class CustomUserAdmin(UserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    model=User

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.

    # """Define admin model for custom User model with no username field."""
    fieldsets = (
        (None, {'fields': ('full_name','email','phone_no', 'password')}),
        # (_('Personal info'), {'fields': ('first_name', 'last_name','email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser','is_labour','is_engineer',
                                       )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_no', 'email','password1', 'password2'),
        }),
    )
    list_display = ('phone_no','email', 'full_name','is_superuser')
    list_filter = ('is_superuser', 'is_staff', 'is_active')
    search_fields = ('phone_no',)
    ordering = ('phone_no',)
    filter_horizontal = ()
#Engineer
class EngineerInline(admin.TabularInline):
    model = Hired
    # extra = 10
class EngineerAdmin(admin.ModelAdmin):
    inlines = [EngineerInline]

#Labour
# class LabourInline(admin.TabularInline):
#     model = Labour
#     # extra = 10
# class LabourAdmin(admin.ModelAdmin):
#     inlines = [LabourInline] 

#Models Register
admin.site.register(User,CustomUserAdmin)
admin.site.register(Labour)
admin.site.register(Engineer,EngineerAdmin)
# admin.site.register(Hired)
