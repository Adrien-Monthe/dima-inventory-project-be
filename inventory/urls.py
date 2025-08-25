from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    ProductTypeViewSet, LocationViewSet, ProductCategoryViewSet, ProductViewSet,
    AddressTypeViewSet, VendorViewSet, StockMoveViewSet, InventorySnapshotViewSet
)

router = DefaultRouter(trailing_slash=False)  # no trailing slash
router.register(r'product-types', ProductTypeViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'product-categories', ProductCategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'address-types', AddressTypeViewSet)
router.register(r'vendors', VendorViewSet)
router.register(r'stock-moves', StockMoveViewSet)
router.register(r'inventory-snapshots', InventorySnapshotViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
