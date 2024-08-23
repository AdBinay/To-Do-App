from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_completed', 'due_date', 'priority', 'created_at')
    list_filter = ('is_completed', 'priority', 'due_date')
    search_fields = ('title',)

admin.site.register(Todo, TodoAdmin)
