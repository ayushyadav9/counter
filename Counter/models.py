from django.db import models
# Create your models here.

class WordsModel(models.Model):
    method=models.CharField(blank=True,max_length=101,choices=[("With Spaces","With Spaces"),("Without Spaces","Without Spaces"),("Characteres","Characteres"),("Words","Words"),("Sentences","Sentences")])
    text=models.TextField(blank=True)
    result=models.CharField(blank=True,max_length=100)

class ChangeModel(models.Model):
    method2=models.CharField(blank=True,max_length=100,choices=[("All upper","All upper"),("All lower","All lower"),("Capitalize first only","Capitalize first only")])
    input=models.TextField(blank=True)
    output=models.TextField(blank=True)

class FindModel(models.Model):
    method3=models.CharField(blank=True,max_length=100,choices=[('Case Sensitive','Case Sensitive'),('Case invariant','Case invariant')])
    word_to_find=models.CharField(blank=True,max_length=100)
    paragraph=models.TextField(blank=True)
    occurances=models.CharField(blank=True,max_length=100)
