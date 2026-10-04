from django.db import models

# Abstract Model inheritance 

class BasePerson(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    join_date = models.DateField()

    class Meta:
        abstract = True

class Student(BasePerson):
    fees = models.IntegerField()
    join_date = None


class Teacher(BasePerson):
    salary = models.IntegerField()
    


class Contractor(BasePerson):
    payment = models.IntegerField()
    join_date = models.DateTimeField()


# Multi-table inheritance 

class ExamCenter(models.Model):
    center_name = models.CharField(max_length=255)
    center_city = models.CharField(max_length=255)

class Candidate(ExamCenter):
    name = models.CharField(max_length=255)
    roll = models.IntegerField()

# Proxy model inheritance 

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    stock = models.IntegerField()

class DiscountedProduct(Product):
    class Meta:
        proxy = True
        ordering = ['id']