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
    num_hired = models.IntegerField()
    new_hires = models.ManyToMany(User)
    
    def __str__(self):
            return f"{self.uid} | {self.name} | {self.num_hired}"

class Application(models.Model):
    user_created = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="User that created application",
    )
    done_interview = models.BooleanField()
    resume = models.CharField(max_length=100)
    transcript = models.CharField(max_length=100)

    def __str__(self):
        return f" {self.user_created} | {self.done_interview} "