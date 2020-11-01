# Generated by Django 3.0.4 on 2020-10-11 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classroomtime_at', models.DateTimeField(null=True)),
                ('state', models.IntegerField(choices=[(0, 'Waiting Confirmation by teacher'), (1, 'Confirmed by teacher'), (2, 'Waiting Confirmation by student'), (3, 'Confirmed by student')], default=0)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classroom_student', to='account.Student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classroom_teacher', to='account.Teacher')),
            ],
        ),
    ]