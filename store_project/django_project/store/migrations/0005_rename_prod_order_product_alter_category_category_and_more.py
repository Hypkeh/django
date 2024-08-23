# Generated by Django 5.0.4 on 2024-06-20 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_remove_cereals_product_remove_dairy_product_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='prod',
            new_name='product',
        ),
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(choices=[('Dairy', 'Молочные продукты'), ('Bread', 'Хлебные изделия'), ('Meat', 'Мясные продукты'), ('Fish/Seafood', 'Морепродукты'), ('Drinks', 'Напитки'), ('Snacks', 'Закуски, снеки'), ('Tea/Coffee', 'Кофе/Чай'), ('Species/Sauces', 'Специи/Соусы'), ('Ceareals', 'Хлопья/Крупы')], max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
