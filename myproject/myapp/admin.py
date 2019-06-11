from django.contrib import admin
from .models import Post, Comment
# from .models import Post = import models.Post
# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)

# .models에서 .은 같은 라인의 다른 파일 의미, ..은 상위폴더 의미