from django.db import models
from django.utils import timezone


class Post(models.Model):
    Status_of_work = (
        ('C', 'Completed'),
        ('I', 'InProgress'),
        ('N', 'NotStarted'),
    )
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    todays_Accomplishment = models.CharField(max_length=200)
    Activities_in_progress = models.CharField(max_length=200)
    status = models.CharField(max_length=1, choices=Status_of_work)
    problems = models.CharField(max_length=200)
    
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
