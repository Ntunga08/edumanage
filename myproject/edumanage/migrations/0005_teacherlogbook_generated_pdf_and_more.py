# Generated by Django 5.2.4 on 2025-07-21 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edumanage', '0004_teacherlogbook_teacherworkplan'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacherlogbook',
            name='generated_pdf',
            field=models.FileField(blank=True, help_text='System-generated PDF of your logbook (auto-filled)', null=True, upload_to='logbooks/generated/'),
        ),
        migrations.AddField(
            model_name='teacherlogbook',
            name='pdf_upload',
            field=models.FileField(blank=True, help_text='Upload a PDF of your logbook (optional)', null=True, upload_to='logbooks/uploaded/'),
        ),
    ]
