# Generated by Django 4.0.5 on 2022-06-17 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CandidateSkills',
            new_name='CandidateSkill',
        ),
    ]