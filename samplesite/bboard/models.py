from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30, verbose_name="Имя")
    last_name = models.CharField(max_length=30, verbose_name="Фамилия")
    date_of_birth = models.DateField(verbose_name="Дата рождения")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Человек"
        verbose_name_plural = "Люди"
        ordering = ['last_name', 'first_name']

class Child(Person):
    parent = models.ForeignKey(Person, related_name='children', on_delete=models.CASCADE, verbose_name="Родитель")

    def __str__(self):
        return f"{self.first_name} {self.last_name} (Ребенок)"

    class Meta:
        verbose_name = "Ребенок"
        verbose_name_plural = "Дети"
        ordering = ['last_name', 'first_name']





class IceCream(models.Model):
    flavor = models.CharField(max_length=50, verbose_name="Вкус")
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Цена")
    quantity_kg = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Количество в кг")

    def __str__(self):
        return self.flavor

    class Meta:
        verbose_name = "Мороженое"
        verbose_name_plural = "Мороженое"
        ordering = ['flavor']

class IceCreamStand(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    location = models.CharField(max_length=200, verbose_name="Местоположение")
    ice_creams = models.ManyToManyField(IceCream, related_name='stands', verbose_name="Мороженое")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Киоск с мороженым"
        verbose_name_plural = "Киоски с мороженым"
        ordering = ['name']


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']

class Bb(models.Model):
    rubric = models.ForeignKey(Rubric, null=True, on_delete=models.PROTECT, verbose_name='Рубрика')
    title = models.CharField(max_length=50, verbose_name='Товар')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    published = models.DateTimeField(verbose_name='Опубликованно')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['published']
