from rest_framework import serializers

from .models import (
    ProductType, Location, ProductCategory, Product,
    AddressType, Vendor, StockMove, InventorySnapshot
)


class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class AddressTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressType
        fields = '__all__'


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'


class StockMoveSerializer(serializers.ModelSerializer):
    from_location_name = serializers.CharField(source='from_location.name', read_only=True)
    to_location_name = serializers.CharField(source='to_location.name', read_only=True)
    product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = StockMove
        fields = [
            'id', 'move_type', 'product', 'quantity', 'from_location', 'to_location',
            'from_location_name', 'to_location_name', 'product_name'
        ]


class InventorySnapshotSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name", read_only=True)
    location_name = serializers.CharField(source="location.name", read_only=True)

    class Meta:
        model = InventorySnapshot
        fields = '__all__'  # keep all existing fields
        extra_fields = ['product_name', 'location_name']

    def get_field_names(self, declared_fields, info):
        """
        Override to ensure extra_fields are included even when fields='__all__'
        """
        expanded_fields = super().get_field_names(declared_fields, info)
        return expanded_fields + getattr(self.Meta, 'extra_fields', [])
