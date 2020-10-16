from django.contrib import admin

from .models import Follower, ContCreator, Post, Books, Genre


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


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)


class Book(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Books)


class BookGenre(admin.ModelAdmin):
    list_display = 'name'


admin.site.register(Genre)
