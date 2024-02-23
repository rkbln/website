from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name='Название')
    author = models.CharField(max_length=100, null=False, blank=False, verbose_name='Автор')
    body = models.TextField(max_length=3500, null=False, blank=False, verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата и время изменения')

    def __str__(self):
        return f"{self.pk}. {self.title}"

    class Meta:
        verbose_name= 'Статья'
        verbose_name_plural = 'Статьи'