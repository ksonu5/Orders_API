from django.db import models


class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

