# Generated by Django 4.1.5 on 2023-01-13 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logindash', '0003_cryptocurrency_delete_bitcoin_delete_news_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(default='Contact us from telegram @maeybeyes')),
            ],
        ),
        migrations.RemoveField(
            model_name='cryptocurrency',
            name='note',
        ),
    ]
