# Generated by Django 5.0.1 on 2024-01-17 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RepSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rep', models.CharField(choices=[('R', 'Reps'), ('S', 'Sets')], default='R', max_length=99)),
                ('set', models.CharField(choices=[('R', 'Reps'), ('S', 'Sets')], default='Sets', max_length=99)),
            ],
        ),
    ]