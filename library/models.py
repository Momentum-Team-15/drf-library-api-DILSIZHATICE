from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass



class Books(models.Model):
    author = models.CharField(max_length=500, blank=True, default='')
    title = models.CharField(max_length=500, blank=True, default='')
    pub_date = models.DateField(blank=True, null=True)
    genre = models.CharField(max_length=500)
    featured_field = models.BooleanField(default=False)
    user = models.ForeignKey('User', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.title} by {self.author}"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['author', 'title'], name='books')
        ]


class Tracking(models.Model):
    pass


class Note(models.Model):
    note_name = models.CharField(max_length=500, default='notename')
    note = models.TextField(max_length=500, null=True, blank=True)
    date = models.DateField(blank=True, null=True)
    book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name="booknotes", null=True, blank=True)
   

    def __str__(self):
        return self.note_name

   
        