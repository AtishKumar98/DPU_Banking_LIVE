# Generated by Django 4.0.5 on 2022-06-12 09:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('CustomerFeedback', '0008_rename_phone_no_customerfeedback_phone_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerfeedback',
            name='comment_Title',
            field=models.CharField(choices=[('Compliment', 'Compliment'), ('Complaint', 'Complaint')], default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
    ]