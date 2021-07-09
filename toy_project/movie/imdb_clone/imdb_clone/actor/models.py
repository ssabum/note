from django.db import models
from django.utils.text import slugify
from django.urls import reverse


# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=70, unique=True)
    picture = models.ImageField(blank=True)
    # 일반적으로 이미 확보된 데이터로부터 유효한 URL을 만드는 방법
    slug = models.SlugField(null=True, unique=True)
    movies = models.ManyToManyField('movie.Movie')

    def get_absolute_url(self):
        return reverse('actors', args=[self.slug])
    

    def __str__(self):
        return self.name
    
    # slug를 사용하여 보기 좋은 url을 만드는 동시에 제목과 동일하게 맞춰주어 검색엔진 최적화에도 좋음
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
