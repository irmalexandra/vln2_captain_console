# Generated by Django 3.0.5 on 2020-05-12 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('consoles', '0005_initial'),
        ('main', '0005_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.Product')),
                ('rating', models.IntegerField(default=0)),
                ('console_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='consoles.Console')),
                ('genres', models.ManyToManyField(to='games.Genre')),
            ],
            bases=('main.product',),
        ),
    ]
