# Generated by Django 3.2.5 on 2023-03-03 05:43

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apartment', '0008_auto_20220129_1009'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amenities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookedfor', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TimingSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ontime', models.TimeField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='association',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='block',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='complain',
            name='complaintype',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='complain',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='designation',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='familymember',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='gender',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='maritalstatus',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='membertype',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='officeaddress',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='relation',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='addresss',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='datetimeout',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 3, 11, 13, 45, 476269)),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.CreateModel(
            name='RegularVisitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('cell', models.BigIntegerField()),
                ('addresss', models.CharField(max_length=150)),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apartment.gender')),
                ('memberid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apartment.owner')),
                ('relation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apartment.relation')),
            ],
        ),
        migrations.CreateModel(
            name='ComplainRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('flatno', models.IntegerField()),
                ('complaintdesc', models.CharField(max_length=50)),
                ('serviceprovider', models.CharField(max_length=50)),
                ('blockid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apartment.block')),
                ('complaintype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apartment.complain')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ondate', models.DateField()),
                ('status', models.CharField(max_length=50)),
                ('bookedforid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apartment.amenities')),
                ('memberid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apartment.owner')),
                ('ontimeid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apartment.timingslot')),
            ],
        ),
    ]
