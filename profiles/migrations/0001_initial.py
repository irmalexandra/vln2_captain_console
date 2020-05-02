# Generated by Django 3.0.5 on 2020-05-02 13:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('carts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_1', models.CharField(max_length=255)),
                ('address_2', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('postcode', models.IntegerField()),
                ('country', models.CharField(max_length=255)),
                ('profile_image', models.CharField(max_length=999)),
                ('payment_information_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carts.ShippingInformation')),
                ('shipping_information_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carts.PaymentInformation')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SearchHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search', models.TextField()),
                ('profileID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('feedback', models.CharField(max_length=999)),
                ('datetime', models.DateTimeField()),
                ('profileID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='OrderHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carts.Order')),
                ('profileID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='GameReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gameID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.Game')),
                ('reviewID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Review')),
            ],
        ),
    ]
