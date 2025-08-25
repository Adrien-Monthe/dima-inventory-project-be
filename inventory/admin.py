from django.contrib import admin

from inventory.models import Location, ProductType, ProductCategory, Product, AddressType, Vendor

# Register your models here.
admin.site.register(Location)
admin.site.register(ProductType)
admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(AddressType)
admin.site.site_header = "MS Inventory Administration"
admin.site.register(Vendor)
