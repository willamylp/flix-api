from django.contrib import admin


class MovieAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'genre', 
        'release_date', 'resume'
    )
