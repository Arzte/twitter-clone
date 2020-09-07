from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from twitteruser.models import TwitterUser


class MyUserAdmin(UserAdmin):
    model = TwitterUser

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('following', 'followers',)}),
    )


admin.site.register(TwitterUser, MyUserAdmin)
