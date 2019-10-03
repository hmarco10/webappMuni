# Generated by Django 2.2.5 on 2019-10-02 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nichos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('number_credits', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('subject_student', models.ManyToManyField(to='nichos.Subject')),
            ],
        ),
    ]
