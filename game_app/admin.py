from django.contrib import admin
from django.utils.safestring import mark_safe
from game_app.models import *

@admin.register(Game)
class adminCar(admin.ModelAdmin):
    list_display = ("id", "name", "date", "category", "make_image")
    list_display_links = ("id", "name")
    search_fields = ("name", "content", "id")
    list_filter = ("category", "date")
    filter_horizontal = ('tag',)
    readonly_fields = ("make_full_image",)

    def make_image(self, game):
        if game.image:
            return mark_safe(f'<img width="180px" height="auto" src="{game.image.url}" alt="" />')
        return None
    
    @admin.display(description="Изображение")
    def make_full_image(self, game):
        if game.image:
            return mark_safe(f'<img width="100%" height="auto" src="{game.image.url}" alt="" />')
        return None

admin.site.register(Category)
admin.site.register(Tag)
# Register your models here.