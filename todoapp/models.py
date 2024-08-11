from django.db import models
from django.utils import timezone


class work(models.Model): 
    task = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "%s %s %s" % (self.task, self.status, self.date)


    



    
