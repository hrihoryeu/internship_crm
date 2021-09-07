# Generated by Django 3.2.7 on 2021-09-06 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
        ('provider', '0001_initial'),
        ('car_showroom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carshowroomsale',
            name='cars_list',
            field=models.ManyToManyField(to='provider.Car'),
        ),
        migrations.AddField(
            model_name='carshowroomcustomer',
            name='car_showroom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_showroom.carshowroom'),
        ),
        migrations.AddField(
            model_name='carshowroomcustomer',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer'),
        ),
        migrations.AddField(
            model_name='carshowroomcar',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='provider.car'),
        ),
        migrations.AddField(
            model_name='carshowroomcar',
            name='car_showroom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_showroom.carshowroom'),
        ),
        migrations.AddField(
            model_name='carshowroom',
            name='car_list',
            field=models.ManyToManyField(through='car_showroom.CarShowroomCar', to='provider.Car'),
        ),
        migrations.AddField(
            model_name='carshowroom',
            name='customers_list',
            field=models.ManyToManyField(through='car_showroom.CarShowroomCustomer', to='customer.Customer'),
        ),
    ]