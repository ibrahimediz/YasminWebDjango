from django.db import models
from django.utils import timezone

class BlogModel(models.Model):
    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Bloglar'
    title = models.CharField(max_length=200,verbose_name='Başlık')
    content = models.TextField(verbose_name='İçerik')
    created_date = models.DateTimeField(default=timezone.now,verbose_name='Oluşturulma Tarihi')
    published_date = models.DateTimeField(blank=True, null=True,verbose_name='Yayınlanma Tarihi')

    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title