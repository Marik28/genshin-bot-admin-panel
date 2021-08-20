from django.contrib import admin

from .models import Character, CharacterImage, Banner

admin.site.register(CharacterImage)
admin.site.register(Banner)


class CharacterImageInline(admin.StackedInline):
    model = CharacterImage
    extra = 2


@admin.register(Character)
class Character(admin.ModelAdmin):
    inlines = [CharacterImageInline]
