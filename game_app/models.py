from django.db import models

from django.db import models

class Game(models.Model):

    class Meta:
        verbose_name = "Игра"
        verbose_name_plural = "Игры"

    name = models.CharField(verbose_name="Название", max_length=100)
    price = models.IntegerField(verbose_name="Цена")
    content = models.TextField(verbose_name="Контент")
    image = models.ImageField(verbose_name="Изображение", upload_to='game_image/')
    date = models.DateTimeField(verbose_name="Дата", auto_now_add=True)
    tag = models.ManyToManyField('game_app.tag',verbose_name="Теги", blank=True, related_name="games")
    category = models.ForeignKey("game_app.category", on_delete=models.CASCADE, verbose_name="Категория", related_name="game",)
    author = models.ForeignKey('auth.User', models.CASCADE, verbose_name='автор')
    
    def __str__(self) -> str:
        return f"{self.name} - {self.date}"

class Category(models.Model):
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    name = models.CharField(verbose_name="Название", max_length=100)

    def __str__(self) -> str:
        return f"{self.name}"

    
class Tag(models.Model):
    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    name = models.CharField('Название', max_length=100)

    def __str__(self) -> str:
        return f"{self.name}"

# Create your models here.
