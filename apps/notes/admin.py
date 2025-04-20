
from django.contrib import admin
from .models import Note

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):

    list_display = ('title', 'author', 'status', 'created_at', 'updated_at')

    list_filter = ('status', 'created_at', 'updated_at', 'author')
   
    search_fields = ('title', 'content', 'author__username')

    list_editable = ('status',)
    

    prepopulated_fields = {'slug': ('title',)}
    

    date_hierarchy = 'created_at'
    

    ordering = ('-created_at',)
    
  
    fieldsets = (
        ('Content', {
            'fields': ('title', 'slug', 'content')
        }),
        ('Metadata', {
            'fields': ('author', 'status'),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    

    readonly_fields = ('created_at', 'updated_at')
    

    add_fieldsets = (
        (None, {
            'fields': ('title', 'content', 'author', 'status')
        }),
    )
    

    def save_model(self, request, obj, form, change):
        if not change and not obj.author:  
            obj.author = request.user
        super().save_model(request, obj, form, change)