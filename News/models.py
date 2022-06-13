from django.db import models


class News(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='News/%d', blank=True)
    pub_date = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=100)
    watch = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.author} - {self.title}'


class Category(models.Model):
    title = models.CharField(max_length=40)

    def __str__(self):
        return self.title


class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.author
