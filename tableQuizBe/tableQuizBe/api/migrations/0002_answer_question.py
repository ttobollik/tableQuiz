# Generated by Django 3.1.3 on 2020-11-22 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questionId', models.CharField(max_length=256)),
                ('answerText', models.CharField(max_length=255)),
                ('answerTrue', models.BooleanField(default=False)),
                ('answerFiftyFifty', models.BooleanField(default=False)),
                ('picture', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(max_length=32)),
                ('questionText', models.CharField(max_length=256)),
                ('picture', models.CharField(max_length=32)),
            ],
        ),
    ]
