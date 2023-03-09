# Generated by Django 3.2.7 on 2023-03-11 11:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_auto_20180104_1247'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelWithUuidPk',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'testapp_uuid4_model',
            },
        ),
    ]