from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    class Meta:
        db_table = 'menu'
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'
    def __str__(self):
        return self.name