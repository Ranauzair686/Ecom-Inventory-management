# Generated by Django 5.1.4 on 2025-01-02 15:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('InventoryServices', '0001_initial'),
        ('OrderServices', '0001_initial'),
        ('ProductServices', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='added_by_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='added_by_user_id_inventory', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='inventory',
            name='domain_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='domain_user_id_inventory', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='inventory',
            name='product_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ProductServices.products'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='purchase_order_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='OrderServices.purchaseorder'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='purchase_order_item_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='OrderServices.purchaseorderitems'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='purchase_order_item_inwarded_item_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='purchase_order_item_inwarded_item_id', to='OrderServices.purchaseorderiteminwardedlog'),
        ),
        migrations.AddField(
            model_name='inventrylog',
            name='added_by_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='added_by_user_id_inventry_log', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='inventrylog',
            name='domain_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='domain_user_id_idinventry_log', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='inventrylog',
            name='inventory_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='InventoryServices.inventory'),
        ),
        migrations.AddField(
            model_name='inventrylog',
            name='po_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='po_id_inventorylog', to='OrderServices.purchaseorder'),
        ),
        migrations.AddField(
            model_name='inventrylog',
            name='so_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='so_id_inventorylog', to='OrderServices.salesorder'),
        ),
        migrations.AddField(
            model_name='rackandshelvesandfloor',
            name='added_by_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='added_by_user_id_rack_shelf_floor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rackandshelvesandfloor',
            name='domain_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='domain_user_id_rack_shelf_floor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='inventrylog',
            name='rack_shelf_floor_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='InventoryServices.rackandshelvesandfloor'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='rack_shelf_floor_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='InventoryServices.rackandshelvesandfloor'),
        ),
        migrations.AddField(
            model_name='warehouse',
            name='added_by_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='added_by_user_id_warehouse', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='warehouse',
            name='domain_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='domain_user_id_warehouse', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='warehouse',
            name='warehouse_manger',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='warehouse_manger_id', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rackandshelvesandfloor',
            name='warehouse_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='warehouse_id_rack_shelf_floor', to='InventoryServices.warehouse'),
        ),
        migrations.AddField(
            model_name='inventrylog',
            name='Warehouse_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Warehouse_id_inventorylog', to='InventoryServices.warehouse'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='warehouse_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='warehouse_id_inventory', to='InventoryServices.warehouse'),
        ),
    ]