from django.db import models


class MessageFromSpace(models.Model):

    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    read = models.BooleanField(default=False)

    class Meta:
        ordering = ['date']
    
    def __str__(self):
        return 'Added ' + str(self.date)

    


