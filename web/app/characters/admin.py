from django.contrib import admin

from .models import Character, CharacterImage, Banner, BotUser

admin.site.register(CharacterImage)


@admin.register(BotUser)
class BotUserAdmin(admin.ModelAdmin):
    filter_horizontal = ("characters",)


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    filter_horizontal = ("characters",)


class CharacterImageInline(admin.StackedInline):
    model = CharacterImage
    extra = 2


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    inlines = [CharacterImageInline]
    search_fields = ("name",)
    list_filter = ("rarity",)
