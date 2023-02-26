from django.contrib import admin
from .models import Photo

# Register your models here.
admin.site.register(Photo)

# 모델에 적용한 클래스를 admin에 추가. 