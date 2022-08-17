from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username",'first_name','last_name','email','is_staff')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("productid","productcode", "name", "price", "img", "description","stock","createdate","brandname")

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ("orderid", "orderaddress", "username", "orderdate", "orderstatus","total")

class OrderdetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orderdetails
        fields = ("orderid","productid", "quantity")

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ("id","brandname", "branddes","img")


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ("cartid", "username", "carttotal","cartnum","typecart")

class CartdetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartdetails
        fields = ("productid", "quantity")

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("username","img","defaultaddress","phonenum")

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ("__all__")