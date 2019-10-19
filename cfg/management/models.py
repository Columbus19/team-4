from django.db import models

# Create your models here.
class User(models.Model):
    uid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    applied = models.BooleanField()

    def __str__(self):
        return f"{self.uid} | {self.name} | {self.applied}"

class Corporation(models.Model):
    uid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    hired = models.IntegerField()

    def __str__(self):
            return f"{self.uid} | {self.name} | {self.hired}"

class Application(models.Model):
    student = models.CharField(max_length=45)
    done_interview = models.BooleanField()
    resume = models.CharField(max_length=100)
    transcript = models.CharField(max_length=100)

    def __str__(self):
        return f" {self.student} | {self.done_interview} "