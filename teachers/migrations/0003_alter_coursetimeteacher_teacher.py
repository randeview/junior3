# Generated by Django 3.2 on 2021-04-18 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_auto_20210418_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursetimeteacher',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_time', to='teachers.teacher'),
        ),
    ]