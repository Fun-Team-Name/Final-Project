# Generated by Django 2.1.1 on 2018-09-10 04:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.CharField(max_length=40, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='account',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='account',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='account',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='account',
            name='tagline',
        ),
        migrations.RemoveField(
            model_name='account',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='account',
            name='username',
        ),
        migrations.AddField(
            model_name='account',
            name='firstName',
            field=models.CharField(default='first', max_length=40),
        ),
        migrations.AddField(
            model_name='account',
            name='lastName',
            field=models.CharField(default='last', max_length=40),
        ),
        migrations.AddField(
            model_name='account',
            name='teacher',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='account',
            name='classroom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='teacher.Classroom'),
        ),
    ]
