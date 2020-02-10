# Generated by Django 3.0.3 on 2020-02-10 11:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0008_post_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL, verbose_name='autor'),
        ),
        migrations.AlterField(
            model_name='post',
            name='imagem',
            field=models.ImageField(upload_to='posts/'),
        ),
    ]
