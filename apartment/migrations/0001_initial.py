# Generated by Django 3.1.1 on 2021-11-12 11:28

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MaritalStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marital', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MemberType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('cell', models.BigIntegerField()),
                ('email', models.EmailField(max_length=50)),
                ('occupation', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=50)),
                ('officeaddress', ckeditor.fields.RichTextField()),
                ('ondate', models.DateField()),
                ('flatnum', models.IntegerField()),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apartment.block')),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apartment.gender')),
                ('martial_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apartment.maritalstatus')),
                ('membertype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apartment.membertype')),
            ],
        ),
    ]
