from rest_framework import viewsets

from .models import (
    ProductType, Location, ProductCategory, Product,
    AddressType, Vendor, StockMove, InventorySnapshot
)
from .serializers import (
    ProductTypeSerializer, LocationSerializer, ProductCategorySerializer, ProductSerializer,
    AddressTypeSerializer, VendorSerializer, StockMoveSerializer, InventorySnapshotSerializer
)


class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class AddressTypeViewSet(viewsets.ModelViewSet):
    queryset = AddressType.objects.all()
    serializer_class = AddressTypeSerializer


class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class StockMoveViewSet(viewsets.ModelViewSet):
    queryset = StockMove.objects.all()
    serializer_class = StockMoveSerializer


class InventorySnapshotViewSet(viewsets.ModelViewSet):
    queryset = InventorySnapshot.objects.all()
    serializer_class = InventorySnapshotSerializer
