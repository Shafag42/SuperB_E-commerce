from rest_framework import serializers

from order.models import WishList

class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishList
        fields = ['user', 'item']