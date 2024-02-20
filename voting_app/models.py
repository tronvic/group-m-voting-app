from django.contrib.auth.models import User
from django.db import models
# Create your models here.


positions = [
    ('president', 'President'),
    ('vice_president', 'President'),
    ('secretary', 'Secretary'),
    ('Clerk', 'Clerk'),
]


class Candidate(models.Model):
    name = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='candidates_pictures/')
    position = models.CharField(max_length=30, choices=positions)

    def __str__(self):
        return f"{self.name} vying for {self.position} position"



class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    voted_at = models.DateTimeField(auto_now_add=True)


