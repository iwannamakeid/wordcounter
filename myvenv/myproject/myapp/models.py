from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    pub_data = models.DateTimeField() 
    # pub-data: 날짜였구나~ 올올오로ㅗㅗㄹ
