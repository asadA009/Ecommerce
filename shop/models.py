from django.db import models
class product(models.Model):
    product_id =models.AutoField
    product_name=models.CharField(max_length=20)
    category=models.CharField(max_length=100, default="")
    sub_category=models.CharField(max_length=100,default="")
    price=models.IntegerField(default=0)
    image=models.ImageField(upload_to="shop/images", default="")
    description=models.CharField(max_length=60)
    pub_date= models.DateField()

    def __str__(self):
        return self.product_name