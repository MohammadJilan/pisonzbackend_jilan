from django.contrib import admin
from .models import MyUser, TokenTest
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin

# Customizing the Admin site View, Edit, and Add form.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm  # Form used to create users in admin
    form = CustomUserChangeForm  # Form used to edit users in admin
    model = MyUser

    list_display = ('email', 'username', 'date_joined', 'balance', 'profile_pic', 'is_staff', 'is_active')  # Fields displayed in the list view
    list_filter = ('is_staff', 'is_active')
    search_fields = ('email', 'username')
    ordering = ('email',)


    # Edit Form
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password','date_joined', 'balance', 'profile_pic')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )


    # Add Form
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2','date_joined', 'balance', 'profile_pic', 'is_staff', 'is_active'),
        }),
    )



# Register your models here.
admin.site.register(MyUser, CustomUserAdmin)
admin.site.register(TokenTest)