from django.db import models

class ProductsDetails(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=True,blank=True)
    price = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
      db_table = "products_details"  

class ProductLogs(models.Model):
    product = models.ForeignKey(ProductsDetails,on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "logs_of_viewed_product"