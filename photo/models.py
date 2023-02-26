from django.db import models

class Photo(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    image = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()


# Model 부분.
# 테이터 베이스 테이블 생성.

