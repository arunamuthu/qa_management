# Generated by Django 3.0.4 on 2020-05-04 04:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('skill', '0001_initial'),
        ('user', '0007_remove_user_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to='user.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionSkill',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('question', models.ForeignKey(db_column='question_id', on_delete=django.db.models.deletion.CASCADE, to='question.Question')),
                ('skill', models.ForeignKey(db_column='skill_id', on_delete=django.db.models.deletion.CASCADE, to='skill.SkillSet')),
            ],
        ),
    ]