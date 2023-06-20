from django.db import models



def user_directory_path(instance, filename):
    return '{0}/{1}'.format("product_photos",filename)

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.FileField(upload_to=user_directory_path, null=True, verbose_name="")

    def __str__(self):
        return self.name
