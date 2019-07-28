from django.db import models


# Create your models here.

class barRank(models.Model):
    title = models.CharField(max_length=50)
    # image = models.FilePathField(path="static/images", match=None ,max_length=100)
    address = models.CharField(max_length=100)
    promotion = models.TextField()

    def __str__(self):
        return self.title



class BarRankCSV(models.Model):
    title = models.CharField("title",max_length=150)
    kanaTitle = models.CharField("kanaTitle",max_length=150)
    address = models.CharField("address",max_length=200)
    promotion = models.TextField("promotion")

    def __str__(self):
        return self.title


