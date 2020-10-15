from django.contrib import admin

from .models import Follower, ContCreator


class FollowerList(admin.ModelAdmin):
    list_display = ('f_name', 'phone_number')
    list_filter = ('f_name',)
    search_fields = ('f_name',)
    ordering = ['f_name']


admin.site.register(Follower)

class CreatorList(admin.ModelAdmin):
    list_display = ('cc_name', 'phone_number')
    list_filter = ('cc_name',)
    search_fields = ('cc_name',)
    ordering = ['cc_name']


admin.site.register(ContCreator)
