from django.contrib import admin
from .models import Blog #같은 폴더에 있는 models.py로 부터 Blog라고 하는 class 가져오기

admin.site.register(Blog)

