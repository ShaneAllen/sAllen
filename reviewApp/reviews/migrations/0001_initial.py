# Generated by Django 2.2 on 2019-04-23 16:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('brand', models.CharField(default='', max_length=255)),
                ('avg_cost', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
                ('date_released', models.TextField()),
                ('photo', models.ImageField(default='default.jpg', upload_to='product_pics')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.Category')),
            ],
        ),
        migrations.CreateModel(
            name='review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0, max_length=5)),
                ('review_text', models.TextField()),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.Product')),
            ],
        ),
    ]
