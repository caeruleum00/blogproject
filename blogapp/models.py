from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):      #self를 인자로 받아서 title로 보여주기
        return self.title

    def summary(self):
        return self.body[:100]