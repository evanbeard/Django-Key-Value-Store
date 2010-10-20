from django.db import models

class KeyValueStore(models.Model):
    key = models.CharField(max_length=250, primary_key=True)
    value = models.TextField()

    def __unicode__(self):
        return "%s:%s" % (self.key, self.value)
