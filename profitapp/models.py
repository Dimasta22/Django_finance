from django.db import models


# Create your models here.
class Category(models.Model):
    value = models.CharField(max_length=25, null=False)
    type = models.CharField(max_length=25, null=False)

    def __str__(self):
        return f'{self.value}: {self.type}'


class Profit(models.Model):
    value = models.FloatField(null=False)
    date = models.DateTimeField(null=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.value}: {self.date}: {self.category_id}'


class Expenses(models.Model):
    value = models.FloatField(null=False)
    date = models.DateTimeField(null=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.value}: {self.date}: {self.category_id}'
