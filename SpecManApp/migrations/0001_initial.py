# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='InterestedAffected',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('FirstName', models.CharField(max_length=60)),
                ('LastName', models.CharField(max_length=60)),
                ('PostalAddress', models.CharField(max_length=60)),
                ('CityTown', models.CharField(max_length=100)),
                ('PostalCode', models.IntegerField()),
                ('CellphoneNumber', models.IntegerField()),
                ('Landline', models.IntegerField()),
                ('Fax', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
                ('StatusRelation', models.CharField(max_length=50)),
                ('CommunicationMethod', models.CharField(max_length=50)),
                ('Other', models.CharField(max_length=50)),
                ('AdvantageArea', models.CharField(max_length=100)),
                ('AffectedParty', models.CharField(max_length=100)),
                ('PhysicalAddress', models.CharField(max_length=100)),
                ('PropertyFarm', models.CharField(max_length=50)),
                ('DeedNumber', models.CharField(max_length=30)),
                ('FarmName', models.CharField(max_length=50)),
                ('Radio', models.CharField(max_length=60)),
                ('Radio_Other', models.CharField(max_length=60)),
                ('TVSignal', models.CharField(max_length=30)),
                ('OtherTV', models.CharField(max_length=100)),
                ('TVLicence', models.CharField(max_length=30)),
                ('ElectronicComm', models.CharField(max_length=50)),
                ('IcasaLicence', models.CharField(max_length=50)),
                ('OtherElectronicComm', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=30)),
                ('OtherInterest', models.CharField(max_length=100)),
                ('AdditionalInfo', models.CharField(max_length=150)),
                ('Certify', models.CharField(max_length=15)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('FullNames', models.CharField(max_length=60)),
                ('PostalAddress', models.CharField(max_length=100)),
                ('CellphoneNumber', models.IntegerField()),
                ('TelNumber', models.IntegerField()),
                ('YearSubmitted', models.IntegerField()),
                ('CommunicationMethod', models.CharField(max_length=10)),
                ('picture', models.ImageField(upload_to=b'profile_images', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'userprofile',
            },
        ),
    ]
