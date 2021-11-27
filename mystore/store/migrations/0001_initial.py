# Generated by Django 3.2.8 on 2021-11-27 20:28

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=20, unique=True)),
                ('image', models.ImageField(upload_to='profile_pics')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('qty', models.PositiveSmallIntegerField(default=1, help_text='Customer quantity initialization')),
                ('inventory', models.PositiveSmallIntegerField()),
                ('description', models.TextField(max_length=200)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('one', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('two', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('three', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('four', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('five', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating', to='store.product')),
            ],
            options={
                'ordering': ['product'],
            },
        ),
    ]
