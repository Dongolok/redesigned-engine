from rest_framework import serializers
from .models import *


class DepartmentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Departments
        fields = '__all__'


class MealCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealCategories
        fields = ['name', 'department']


class MealsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meals
        fields = ['id', 'name', 'category', 'price', 'description']


class ServicePercentageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicePercentage
        fields = '__all__'


class TablesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tables
        fields = ['id', 'name']


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['id', 'isitready']


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'

    # def create(self, validated_data):
    #     existing_user = validated_data.pop('user')
    #     primary_status = validated_data('status')
    #     number_of_table = validated_data('table')
    #
    #     orders = Orders.objects.create(**validated_data)
    #
    #     for new_user in existing_user:
    #         Users.objects.create(orders=orders, **new_user)
    #
    #         return orders
    #
    #     for new_status


class MealsToOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealsToOrder
        fields = '__all__'


class CheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Check
        fields = '__all__'
