# Generated by Django 5.1.4 on 2025-01-02 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('mrp', models.CharField(blank=True, max_length=50, null=True)),
                ('batch_number', models.CharField(blank=True, max_length=50, null=True)),
                ('discount_type', models.CharField(blank=True, choices=[('PERCENTAGE', 'PERCENTAGE'), ('AMOUNT', 'AMOUNT')], max_length=50, null=True)),
                ('discount_value', models.CharField(blank=True, max_length=50, null=True)),
                ('discount_amount', models.CharField(blank=True, max_length=50, null=True)),
                ('sr_no', models.CharField(blank=True, max_length=50, null=True)),
                ('mfg_date', models.DateField(blank=True, null=True)),
                ('uom', models.CharField(blank=True, max_length=50, null=True)),
                ('ptr', models.CharField(blank=True, max_length=50, null=True)),
                ('recieved_date', models.DateField(blank=True, null=True)),
                ('expiry_date', models.DateField(blank=True, null=True)),
                ('quqantity_inwarded', models.IntegerField()),
                ('buy_price', models.CharField(blank=True, max_length=50, null=True)),
                ('sell_price', models.CharField(blank=True, max_length=50, null=True)),
                ('tax_percentage', models.CharField(blank=True, max_length=50, null=True)),
                ('stock_status', models.CharField(blank=True, choices=[('IN_STOCK', 'IN_STOCK'), ('OUT_OF_STOCK', 'OUT_OF_STOCK'), ('DAMAGED', 'DAMAGED'), ('LOST', 'LOST')], max_length=50, null=True)),
                ('inward_type', models.CharField(blank=True, choices=[('PURCHASE', 'PURCHASE'), ('RETURN', 'RETURN')], max_length=50, null=True)),
                ('addititon_details', models.JSONField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='InventryLog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('status', models.CharField(blank=True, choices=[('INWARD', 'INWARD'), ('OUTWARD', 'OUTWARD'), ('DAMAGED', 'DAMAGED'), ('LOST', 'LOST'), ('EXPIRED', 'EXPIRED'), ('RETURN', 'RETURN'), ('ADJUSTMENT', 'ADJUSTMENT'), ('WAREHOUSE TRANSFER', 'WAREHOUSE TRANSFER')], max_length=50, null=True)),
                ('additional_details', models.JSONField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='RackAndShelvesAndFloor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('rack', models.CharField(blank=True, max_length=50, null=True)),
                ('shelf', models.CharField(blank=True, max_length=50, null=True)),
                ('floor', models.CharField(blank=True, max_length=50, null=True)),
                ('additional_details', models.JSONField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('address', models.TextField()),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('pincode', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('status', models.CharField(blank=True, choices=[('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE')], max_length=50, null=True)),
                ('size', models.CharField(blank=True, choices=[('SMALL', 'SMALL'), ('MEDIUM', 'MEDIUM'), ('LARGE', 'LARGE')], max_length=50, null=True)),
                ('capacity', models.CharField(blank=True, choices=[('SMALL', 'SMALL'), ('MEDIUM', 'MEDIUM'), ('LARGE', 'LARGE')], max_length=50, null=True)),
                ('warehouse_type', models.CharField(blank=True, choices=[('OWNED', 'OWNED'), ('LEASED', 'LEASED')], max_length=50, null=True)),
                ('additional_details', models.JSONField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
