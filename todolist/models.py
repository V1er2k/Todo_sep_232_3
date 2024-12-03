from django.db import models
from datetime import datetime

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def str(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class TodoList(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    due_time = models.DateTimeField(default=datetime.now())

    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def str(self):
        return self.title

    class Meta:
        ordering = ['-created']
# Create your models here.
