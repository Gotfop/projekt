from django.db import models

# Create your models here.

class Tomat(models.Model):
    color = models.CharField(max_length=12)
    sort = models.CharField(max_length=20, null=True, blank=True)
    weight = models.FloatField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    photo = models.ImageField(null=True, blank=True)

    def __str__(self):
        sort = self.sort or ''
        return f'{sort}, {self.color}'

class Plate(models.Model):
    radius = models.IntegerField(max_length=12)
    color = models.CharField(max_length=12)
    tomat_id = models.ForeignKey(Tomat, on_delete=models.CASCADE)
    

class Client(models.Model):
    class Meta:
        verbose_name= 'Клиент'
        verbose_name_plural = 'Клиенты'
    name = models.CharField(max_length=15)
    phone = models.CharField(max_length=10)
    email = models.CharField()
    addres = models.CharField()

    def __str__(self):
        return self.name


class Oder(models.Model):
    STATUS = [('NEW','Новый'),
              ('IN_WORK','В обработке'),
              ('FINISH','Готов')
              ]
    number_order = models.CharField(verbose_name='Номер заказа')
    client_id = models.ForeignKey(Client, on_delete=models.PROTECT,verbose_name='Заказчик')
    tomats = models.ManyToManyField(Tomat,verbose_name='Товар')
    date = models.DateField(auto_now_add= True)
    status = models.CharField(choices=STATUS,default='NEW',)