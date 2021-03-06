# Generated by Django 2.0.2 on 2018-02-08 14:40

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
            name='Meetings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meetings_text', models.CharField(max_length=100)),
                ('venue', models.SmallIntegerField(choices=[(1, 'homer'), (2, 'plato'), (3, 'jarvis'), (4, 'friday')], default=1)),
                ('start_time', models.DateTimeField(help_text='Start time of the meeting')),
                ('end_time', models.DateTimeField(help_text='End time of the meeting')),
                ('moderator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=300)),
                ('anon_status', models.SmallIntegerField(choices=[(1, 'yes'), (2, 'no')], default=2)),
                ('asker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('meeting_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QueAns.Meetings')),
            ],
        ),
        migrations.CreateModel(
            name='Satisfaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('satisf_status', models.BooleanField(choices=[(1, 'yes'), (2, 'no')], default=1)),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QueAns.Question')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Voting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.SmallIntegerField(choices=[(1, 'Upvote'), (2, 'Downvote'), (3, 'None')], default=3)),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QueAns.Question')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
