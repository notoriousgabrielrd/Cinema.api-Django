from addresses.serializers import AddressSerializer
from rest_framework import serializers
from addresses.models import Address
from cinemas.models import Cinema
        

class CinemaSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    class Meta:
        model = Cinema
        fields = "__all__"
        read_only_fields = ["user"]

    def create(self, validated_data):
        address_instance = Address.objects.create(**validated_data.pop("address"))
        return Cinema.objects.create(**validated_data, address=address_instance)
