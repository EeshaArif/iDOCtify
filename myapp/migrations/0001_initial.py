# Generated by Django 2.2.5 on 2019-12-07 12:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=15)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('occupation', models.CharField(blank=True, max_length=100, null=True)),
                ('presenting_complaint', models.TextField(blank=True, null=True)),
                ('past_medical_history', models.TextField(blank=True, null=True)),
                ('past_surgical_history', models.TextField(blank=True, null=True)),
                ('past_drug_history', models.TextField(blank=True, null=True)),
                ('drug_allergy', models.TextField(blank=True, null=True)),
                ('vaccination_history', models.TextField(blank=True, null=True)),
                ('personal_history', models.TextField(blank=True, null=True)),
                ('economic_status', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Presenting_Complaint_Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symptom', models.CharField(max_length=50)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Patient')),
            ],
        ),
    ]
