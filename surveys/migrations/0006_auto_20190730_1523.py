# Generated by Django 2.2.3 on 2019-07-30 15:23

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager

def add_default_survey(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Survey = apps.get_model("surveys", "Survey")
    Survey.objects.create(slug='default_Survey')


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0005_question_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=20)),
                ('start_date', models.DateField(default=datetime.date.today, help_text='First day of the survey')),
                ('end_date', models.DateField(default=datetime.date.today, help_text='Last day of the survey')),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.RunPython(add_default_survey),
        migrations.AlterModelManagers(
            name='choice',
            managers=[
                ('active_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='survey',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='surveys.Survey'),
            preserve_default=False,
        ),
    ]