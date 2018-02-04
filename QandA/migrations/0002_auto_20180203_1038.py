# Generated by Django 2.0.2 on 2018-02-03 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QandA', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetings',
            name='meeting_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='meetings',
            name='venue',
            field=models.CharField(choices=[('H', 'homer'), ('P', 'plato'), ('J', 'jarvis'), ('F', 'friday')], default='J', max_length=50),
        ),
        migrations.AlterField(
            model_name='question',
            name='anon_status',
            field=models.CharField(choices=[('Y', 'yes'), ('N', 'no')], default='N', max_length=3),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='satisfaction',
            name='satisf_status',
            field=models.CharField(choices=[('Y', 'yes'), ('N', 'no')], default='Y', max_length=5),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]