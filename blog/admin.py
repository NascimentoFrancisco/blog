from django.contrib import admin
from blog.models import Posts

@admin.register(Posts)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at',)
    search_fields = ('title',)
    readonly_fields = ('created_at', 'updated_at')

