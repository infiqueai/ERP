# Generated by Django 4.2.4 on 2023-12-18 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountDetails',
            fields=[
                ('S_no', models.AutoField(default=1000, primary_key=True, serialize=False)),
                ('Session', models.CharField(blank=True, default='', max_length=100)),
                ('Class', models.CharField(blank=True, default='', max_length=100)),
                ('StudentName', models.CharField(blank=True, default='', max_length=100)),
                ('AdmissionNo', models.CharField(blank=True, default='', max_length=255)),
                ('Fee', models.CharField(blank=True, default='', max_length=255)),
                ('Receipts', models.IntegerField(default='')),
                ('TotalPaid', models.DateField(default='', max_length=255)),
                ('Amount', models.CharField(default='', max_length=100)),
                ('Status', models.CharField(default='', max_length=10)),
            ],
            options={
                'db_table': 'account_details',
            },
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiptno', models.CharField(max_length=50)),
                ('studentname', models.CharField(max_length=45)),
                ('studentclass', models.CharField(max_length=45)),
                ('session', models.CharField(max_length=45)),
                ('amountpaid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('totalfees', models.DecimalField(decimal_places=2, max_digits=10)),
                ('modeofpayment', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'receipt',
            },
        ),
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='stdInsert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentname', models.CharField(max_length=100)),
                ('fathername', models.CharField(max_length=100)),
                ('mothername', models.CharField(max_length=100)),
                ('Class', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=100)),
                ('mobilenumber', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'admission',
            },
        ),
        migrations.CreateModel(
            name='StudentDetails',
            fields=[
                ('S_no', models.AutoField(default=1000, primary_key=True, serialize=False)),
                ('Session', models.CharField(blank=True, default='', max_length=100)),
                ('Class', models.CharField(blank=True, default='', max_length=100)),
                ('Group', models.CharField(blank=True, default='', max_length=100)),
                ('Name', models.CharField(blank=True, default='', max_length=255)),
                ('Father_name', models.CharField(blank=True, default='', max_length=255)),
                ('Mother_name', models.CharField(blank=True, default='', max_length=255)),
                ('sr_no', models.IntegerField(default='')),
                ('Birth_date', models.DateField(default='', max_length=255)),
                ('Category', models.CharField(default='', max_length=100)),
                ('Gender', models.CharField(default='', max_length=10)),
                ('Primary_parent_mobile_no', models.CharField(default='', max_length=15)),
                ('Mother_mobile', models.CharField(default='', max_length=15)),
                ('Address', models.TextField(blank=True, default='')),
            ],
            options={
                'db_table': 'details_student',
            },
        ),
    ]