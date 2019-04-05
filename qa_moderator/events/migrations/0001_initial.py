# Generated by Django 2.2 on 2019-04-04 15:16

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=60, verbose_name='name')),
                ('title', models.CharField(max_length=60, verbose_name='title')),
                ('event_date', models.DateField(verbose_name='event date')),
                ('office_name', models.CharField(max_length=80, verbose_name='office name')),
                ('fiscal_year', models.IntegerField(verbose_name='fiscal year')),
                ('start_availability', models.DateTimeField(null=True, verbose_name='start availability')),
                ('end_availability', models.DateTimeField(null=True, verbose_name='end availability')),
                ('active', models.BooleanField(default=True, verbose_name='active')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]