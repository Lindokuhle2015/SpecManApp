# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SpecManApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interestedaffected',
            name='user',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='AdditionalInfo',
            field=models.CharField(default='Additional', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='AdvantageArea',
            field=models.CharField(default='Karoo', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='AffectedParty',
            field=models.CharField(default='Farmer', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='Certify',
            field=models.CharField(default='yes', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='CityTown',
            field=models.CharField(default='Carnavon', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='DeedNumber',
            field=models.CharField(default='Deed01', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='ElectronicComm',
            field=models.CharField(default='email', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='FarmName',
            field=models.CharField(default='farmname', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='Fax',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='IcasaLicence',
            field=models.CharField(default='Licence', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='Landline',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='Other',
            field=models.CharField(default='Other', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='OtherElectronicComm',
            field=models.CharField(default='Other', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='OtherInterest',
            field=models.CharField(default='Other', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='OtherTV',
            field=models.CharField(default='OtherTV', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='PhysicalAddress',
            field=models.CharField(default='Karoo', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='PostalCode',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='PropertyFarm',
            field=models.CharField(default='farm', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='Radio',
            field=models.CharField(default='radio', max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='Radio_Other',
            field=models.CharField(default='radio_other', max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='StatusRelation',
            field=models.CharField(default='relation', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='TVLicence',
            field=models.CharField(default='TVLicence', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='TVSignal',
            field=models.CharField(default='TVSignal', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='state',
            field=models.CharField(default='state', max_length=30),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='InterestedAffected',
        ),
    ]
