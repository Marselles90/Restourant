from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 null=True)
    img = models.ImageField(upload_to='foods/')
    desc = models.CharField(max_length=255)
    price = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Блюда'
        verbose_name_plural = 'Блюда'

    def __str__(self):
        return self.name


class Table(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name='Стол'
        verbose_name_plural='Стол'

    def __str__(self):
        return self.name


class BookTable(models.Model):
    name = models.CharField(max_length=255)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    date = models.DateTimeField()
    persons = models.IntegerField()
    message = models.TextField()

    class Meta:    
        verbose_name = 'Бронирование столиков'
        verbose_name_plural = 'Бронирование столиков'

    def __str__(self):
        return f"Клиент {self.name} забронировал столик {self.table.name}"


class Response(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    subjects = models.CharField(max_length=255)
    message = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Ответы'
        verbose_name_plural = 'Ответы'
        
    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='events/')
    index = models.CharField(max_length=10)
    title = models.CharField(max_length=50)
    text1 = models.CharField(max_length=50)
    text2 = models.CharField(max_length=50)
    text3 = models.CharField(max_length=50)
    desc = models.TextField()

    class Meta:
        verbose_name = 'Cобытия'
        verbose_name_plural = 'Cобытия'
    
    def __str__(self):
        return self.name

