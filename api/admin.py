from django.contrib import admin
from .models import Video, User, Profile, Message, FriendRequest
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _


# adminサイトでのuserのオーバーライド
class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'password']  # adminサイトのUsersの部分
    fieldsets = (  # adminサイトのChange userの部分
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('username',)}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (  # adminサイトの　Add userの部分
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )


admin.site.register(User, UserAdmin)
admin.site.register(Video)
admin.site.register(Profile)
admin.site.register(Message)
admin.site.register(FriendRequest)
