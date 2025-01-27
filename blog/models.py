from django.db import models
from django.urls import reverse

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Author")
        verbose_name_plural = ("Authors")

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Tag(models.Model):
    caption = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Tag")
        verbose_name_plural = ("Tags")

    def __str__(self):
        return self.caption


class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=500)
    image_name = models.CharField(max_length=100)
    date = models.DateField(auto_now=False, auto_now_add=False)
    slug = models.SlugField(max_length=100, default='', blank=True, null=False)
    content = models.CharField(max_length=1000)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=True, related_name='posts')
    tags = models.ManyToManyField(Tag, blank=True)

    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"slug": self.slug})
