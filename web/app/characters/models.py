from django.db import models


class Character(models.Model):
    name = models.CharField(max_length=50)
    rarity = models.IntegerField()
    element = models.CharField(max_length=15)
    weapon = models.CharField(max_length=20)
    sex = models.CharField(max_length=15)
    area = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} ({self.rarity})"

    class Meta:
        verbose_name = "Персонаж"
        verbose_name_plural = "Персонажи"
        ordering = ["name"]
        db_table = "characters"


class Banner(models.Model):
    name = models.CharField(max_length=255)
    characters = models.ManyToManyField(Character, db_table="banner_and_character_association")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннеры"
        db_table = "banners"


class CharacterImage(models.Model):
    link = models.URLField(max_length=255)
    character = models.ForeignKey(Character, on_delete=models.RESTRICT)

    def __str__(self):
        return f"Изображение персонажа {self.character.name}"

    class Meta:
        verbose_name = "Изображение персонажа"
        verbose_name_plural = "Изображения персонажей"
        db_table = "character_images"
