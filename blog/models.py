from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True) # 자동으로 입력 시간
    updated_at = models.DateTimeField(auto_now = True)


    def __str__(self):
        return f'[{self.pk}]{self.title}'   #pk: 각 레코드에 대한 고유의 값./ title: 제목