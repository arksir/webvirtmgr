from django.db import models


# Create your models here.
class SSHKey(models.Model):
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=5000, blank=True, null=True)

    def __unicode__(self):
        return self.value
