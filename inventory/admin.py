from django.contrib import admin

from inventory.models import Location, ProductType, ProductCategory, Product, AddressType, Vendor, StockMove, \
    InventorySnapshot

# Register your models here.
admin.site.site_header = "MS Inventory Administration"

admin.site.register(Location)
admin.site.register(ProductType)
admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(AddressType)
admin.site.register(Vendor)
admin.site.register(StockMove)
admin.site.register(InventorySnapshot)
