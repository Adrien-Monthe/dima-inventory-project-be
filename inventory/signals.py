from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import StockMove, InventorySnapshot


@receiver(post_save, sender=StockMove)
def update_inventory_snapshot(sender, instance, created, **kwargs):
    if not created:
        return

    product = instance.product

    snapshot, _ = InventorySnapshot.objects.get_or_create(
        product=product,
        location=instance.to_location or instance.from_location,
        defaults={"quantity": 0}
    )

    if instance.move_type == "INBOUND":
        snapshot.quantity += instance.quantity
    elif instance.move_type == "OUTBOUND":
        snapshot.quantity -= instance.quantity
    elif instance.move_type == "TRANSFER":
        if instance.from_location:
            from_snap, _ = InventorySnapshot.objects.get_or_create(product=product, location=instance.from_location,
                                                                   defaults={"quantity": 0})
            from_snap.quantity -= instance.quantity
            from_snap.save()

        if instance.to_location:
            to_snap, _ = InventorySnapshot.objects.get_or_create(product=product, location=instance.to_location,
                                                                 defaults={"quantity": 0})
            to_snap.quantity += instance.quantity
            to_snap.save()
        return

    snapshot.save()
