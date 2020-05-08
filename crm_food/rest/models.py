from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings
import datetime
from datetime import timedelta
import jwt
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Roles(models.Model):
    ROLES_CHOICES = [(1, 'Waiter'),
                     (2, 'Admin'),
                     (3, 'Chef')]
    name = models.IntegerField(choices=ROLES_CHOICES)

    def __str__(self):
        return '%s' % self.name


class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None, **kwargs):
        if username is None:
            raise ValueError('User must have a username')
        if email is None:
            raise ValueError('Users must have email')

        user = self.model(username=username,
                          email=self.normalize_email(email),
                          **kwargs
                          )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **kwargs):
        if password is None:
            raise ValueError('Users must have password')

        user = self.create_user(username=username,
                                password=password,
                                email=self.normalize_email(email),
                                **kwargs
                                )
        user.is_superuser = True
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class Users(AbstractUser):
    name = models.CharField(max_length=120, unique=True, default='some name')
    surname = models.CharField(max_length=120)
    email = models.EmailField(max_length=120, unique=True)
    password = models.CharField(max_length=1000, default=1234)
    role = models.ForeignKey(Roles, on_delete=models.CASCADE, default='3')
    phone = models.CharField(max_length=120)
    date = models.DateTimeField(auto_now_add=True, null=True)
    username = models.CharField(max_length=100, unique=True, blank=False)
    REQUIRED_FIELDS = ['name', 'surname', 'email', 'password', 'phone', 'role']
    USERNAME_FIELD = 'username'
    objects = UserManager()

    def __str__(self):
        return self.surname

    def _generate_jwt_token(self):
        day = datetime.now() + timedelta(days=60)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(day.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')


class Departments(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class MealCategories(models.Model):
    name = models.CharField(max_length=120)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Meals(models.Model):
    name = models.CharField(max_length=120)
    category = models.ForeignKey(MealCategories, on_delete=models.CASCADE)
    price = models.CharField(max_length=10)
    description = models.TextField(null=True, default='Some description', max_length=120)

    def __str__(self):
        return self.name


class ServicePercentage(models.Model):
    percentage = models.IntegerField()


class Tables(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Status(models.Model):
    isitready = models.CharField(max_length=20)

    def __str__(self):
        return '%s' % self.isitready


class Orders(models.Model):
    client = models.CharField(max_length=120)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, default=4 )
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default=1)
    table = models.ForeignKey(Tables, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, null=True)
    isitopen = models.BooleanField(default=False)


class MealsToOrder(models.Model):
    orders = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name='orders_to_make', default=1)
    count = models.IntegerField()
    meals = models.ForeignKey(Meals, on_delete=models.CASCADE, related_name='order_meals', default=1)

    def __str__(self):
        return '%s' % self.orders

    def save(self, *args, **kwargs):
            counting = 0
            self.count = int(counting)
            super(MealsToOrder, self).save(*args, **kwargs)

    def sum(self):
        count = self.count
        meal_id = self.meals
        in_sum = MealsToOrder.objects.filter(meals=meal_id)
        # return count * sum(in_sum)

        return sum(item.get_count() for item in MealsToOrder.objects.filter(meals=meal_id))


class Check(models.Model):
    percentage = models.OneToOneField(ServicePercentage, on_delete=models.CASCADE, default=15, related_name='percentage_check')
    order = models.OneToOneField(Orders, on_delete=models.CASCADE, default=1, related_name='orders_made')
    date = models.DateTimeField(auto_now_add=True, null=True)

    def total_sum(self):
        percentage = self.percentage
        regular_sum = MealsToOrder.sum(self)
        return int(percentage) * regular_sum + regular_sum

