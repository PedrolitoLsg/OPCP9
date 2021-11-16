# Generated by Django 3.2.9 on 2021-11-15 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='date',
        ),
        migrations.AddField(
            model_name='product',
            name='publication_year',
            field=models.DateField(default=999999),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticket',
            name='creationdate',
            field=models.DateTimeField(auto_now=True),
        ),
    ]