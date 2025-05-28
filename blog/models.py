from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок поста")
    content = models.TextField(verbose_name="Содержимое поста")
    preview_image = models.ImageField(upload_to="catalog/foto", blank=True, null=True, verbose_name="Изображение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации", null=True)
    is_published = models.BooleanField(default=False, verbose_name="Опубликована?")
    views_count = models.PositiveIntegerField(default=0, verbose_name="Количество просмотров")

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __str__(self):
        return self.title
