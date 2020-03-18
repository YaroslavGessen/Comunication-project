from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customers(models.Model):
    author = models.ForeignKey(User, on_delete= models.CASCADE, blank=True, null=True)
    create_date = models.DateTimeField(auto_now=True)
    customer_id = models.IntegerField(auto_created=True)
    name = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return "%s: %s" % (self.customer_id, self.name)

    class Meta:
        verbose_name = ("Customer")
        verbose_name_plural = ("Customers")