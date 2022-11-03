# Generated by Django 4.1.2 on 2022-11-03 11:39

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
            name='subjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('subject_id', models.CharField(blank=True, max_length=10, null=True)),
                ('stream', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('hod_name', models.CharField(default='', max_length=100)),
                ('students_no', models.CharField(default='', max_length=100)),
                ('phone', models.CharField(default='', max_length=100)),
                ('email', models.CharField(max_length=100, null=True)),
                ('date_created', models.DateField(auto_now_add=True, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='schooluserprofile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standard', models.CharField(blank=True, max_length=100, null=True)),
                ('classroom_id', models.CharField(blank=True, max_length=10, null=True)),
                ('section', models.CharField(blank=True, max_length=100, null=True)),
                ('school_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='school.school')),
                ('subject_list', models.ManyToManyField(blank=True, null=True, related_name='subjectmodel', to='school.subjects')),
            ],
        ),
    ]
