# Generated by Django 3.1.1 on 2022-01-29 04:35

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apartment', '0006_complain_complainrequest_familymember_relation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('cell', models.BigIntegerField()),
                ('addresss', models.CharField(max_length=50)),
                ('datetimein', models.DateTimeField(default=datetime.datetime.now)),
                ('datetimeout', models.DateTimeField(default=datetime.datetime(2022, 1, 29, 10, 5, 50, 189125))),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apartment.gender')),
                ('memberid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apartment.owner')),
                ('relation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apartment.relation')),
            ],
        ),
        migrations.DeleteModel(
            name='ComplainRequest',
        ),
    ]
