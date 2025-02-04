# Generated by Django 3.0 on 2025-02-04 20:00

import companies.managers.company_manager
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('person_in_charge', models.CharField(blank=True, default='', max_length=256, null=True, verbose_name='Person in charge')),
                ('id_person_in_charge', models.CharField(blank=True, default='', max_length=256, null=True, verbose_name='Id person in charge')),
                ('name_company', models.CharField(blank=True, default='', max_length=256, null=True, verbose_name='name_company')),
                ('phone', models.CharField(blank=True, default='', max_length=16, null=True, verbose_name='phone')),
                ('address', models.CharField(blank=True, max_length=500, null=True, verbose_name='Address')),
                ('nit', models.CharField(blank=True, max_length=14, null=True, verbose_name='Nit')),
                ('dv', models.CharField(blank=True, max_length=1, null=True, verbose_name='DV')),
                ('rut', models.CharField(blank=True, max_length=14, null=True, verbose_name='Rut')),
                ('contributory_regime', models.CharField(blank=True, max_length=256, null=True, verbose_name='Contributory regime')),
                ('is_responsible_for_iva', models.BooleanField(default=False, verbose_name='Is responsible for iva')),
                ('city', models.CharField(blank=True, max_length=256, null=True, verbose_name='City')),
                ('department', models.CharField(blank=True, max_length=256, null=True, verbose_name='Department')),
                ('info_bank', models.CharField(blank=True, max_length=256, null=True, verbose_name='Info bank')),
                ('activity_economic', models.CharField(blank=True, max_length=256, null=True, verbose_name='Economic activity')),
                ('token', models.CharField(blank=True, max_length=255, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
            },
            managers=[
                ('objects', companies.managers.company_manager.CompanyManager()),
            ],
        ),
    ]
