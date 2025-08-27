from django.db import models
from django.db.models import Q, F
from django.utils import timezone
from django_softdelete.models import SoftDeleteModel


# Create your models here.

class ProductType(SoftDeleteModel, models.Model):
    code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.code})"


class Location(SoftDeleteModel, models.Model):
    code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.code} - {self.name}"


class ProductCategory(SoftDeleteModel, models.Model):
    code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class Meta:
        verbose_name_plural = "Product Categories"

    def __str__(self):
        if self.parent:
            return f"{self.parent} / {self.name}"
        return self.name


class Product(SoftDeleteModel, models.Model):
    favorite = models.BooleanField(default=False)
    name = models.CharField(max_length=255)
    internal_reference = models.CharField(max_length=100, unique=True, null=True, blank=True)
    responsible = models.CharField(max_length=255, blank=True)
    barcode = models.CharField(max_length=255, blank=True)
    sales_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    product_category = models.ForeignKey('ProductCategory', on_delete=models.PROTECT, related_name='products',
                                         null=True, blank=True)
    product_type = models.ForeignKey(ProductType, on_delete=models.PROTECT, related_name="products")
    quantity_on_hand = models.IntegerField(default=0)
    forecasted_quantity = models.IntegerField(default=0)
    activity_exception_decoration = models.CharField(max_length=255, blank=True)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.internal_reference})"


class AddressType(SoftDeleteModel, models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Vendor(SoftDeleteModel, models.Model):
    name = models.CharField(max_length=255)
    is_company = models.BooleanField(default=False)
    related_company = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True,
                                        related_name='contacts')
    address_type = models.ForeignKey(AddressType, on_delete=models.SET_NULL, null=True, blank=True)
    street = models.CharField(max_length=255, blank=True)
    zip_code = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class StockMove(SoftDeleteModel, models.Model):
    MOVE_TYPES = [
        ("INBOUND", "Inbound"),
        ("OUTBOUND", "Outbound"),
        ("TRANSFER", "Transfer"),
    ]
    move_type = models.CharField(max_length=20, choices=MOVE_TYPES)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    from_location = models.ForeignKey(Location, related_name="outgoing_moves",on_delete=models.SET_NULL, null=True, blank=True)
    to_location = models.ForeignKey(Location, related_name="incoming_moves",on_delete=models.SET_NULL, null=True, blank=True)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.CheckConstraint(name="outbound_requires_from",
                                   check=~Q(move_type="OUTBOUND") | Q(from_location__isnull=False), ),
            models.CheckConstraint(name="transfer_requires_both", check=~Q(move_type="TRANSFER") | (
                    Q(from_location__isnull=False) & Q(to_location__isnull=False) & ~Q(
                from_location=F("to_location"))), ),
        ]

    def __str__(self):
        return f"{self.move_type} {self.quantity} {self.product}"


class InventorySnapshot(SoftDeleteModel, models.Model):
    product = models.ForeignKey( Product, on_delete=models.CASCADE,related_name="inventory_snapshots")
    location = models.ForeignKey(Location,on_delete=models.CASCADE,related_name="inventory_snapshots")
    quantity = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('product', 'location')
        verbose_name_plural = "Inventory Snapshots"

    def __str__(self):
        return f"{self.product.name} @ {self.location.code}: {self.quantity}"