from django.db import models

class Subscriber (models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=128)

    def __str__(self):
        return "ID %s Name %s E-Mail %s" % (self.id, self.name, self.email)


    class Meta:
        verbose_name = "MySubscriber"
        verbose_name_plural = "A lot of Subscribers"