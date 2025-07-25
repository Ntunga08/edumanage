# Generated by Django 5.2.4 on 2025-07-20 03:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edumanage', '0003_subject_exam_class_subjects_result'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherLogbook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_type', models.CharField(choices=[('daily', 'Daily Report'), ('weekly', 'Weekly Report'), ('monthly', 'Monthly Report')], default='daily', max_length=20)),
                ('report_date', models.DateField()),
                ('academic_year', models.CharField(default='2024-2025', max_length=9)),
                ('term', models.CharField(default='Term 1', max_length=20)),
                ('topics_covered', models.TextField(help_text='Topics covered in this period')),
                ('activities_conducted', models.TextField(help_text='Activities and exercises conducted')),
                ('student_participation', models.TextField(help_text='Student participation and engagement')),
                ('challenges_faced', models.TextField(help_text='Challenges or problems encountered')),
                ('solutions_implemented', models.TextField(help_text='Solutions or strategies implemented')),
                ('next_lesson_plan', models.TextField(help_text='Plan for next lesson/period')),
                ('additional_notes', models.TextField(blank=True, help_text='Any additional notes or observations')),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('submitted', 'Submitted'), ('reviewed', 'Reviewed'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='draft', max_length=20)),
                ('submitted_at', models.DateTimeField(blank=True, null=True)),
                ('reviewed_at', models.DateTimeField(blank=True, null=True)),
                ('review_comments', models.TextField(blank=True, help_text='Comments from academic master')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('class_obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logbooks', to='edumanage.class')),
                ('reviewed_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviewed_logbooks', to=settings.AUTH_USER_MODEL)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logbooks', to='edumanage.subject')),
                ('submitted_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='received_logbooks', to=settings.AUTH_USER_MODEL)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logbooks', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Teacher Logbooks',
                'ordering': ['-report_date', '-created_at'],
            },
        ),
        migrations.CreateModel(
            name='TeacherWorkplan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_type', models.CharField(choices=[('beginning_term', 'Beginning of Term'), ('end_term', 'End of Term'), ('mid_term', 'Mid Term')], max_length=20)),
                ('academic_year', models.CharField(default='2024-2025', max_length=9)),
                ('term', models.CharField(default='Term 1', max_length=20)),
                ('learning_objectives', models.TextField(help_text='Learning objectives for the term')),
                ('topics_to_cover', models.TextField(help_text='Topics to be covered during the term')),
                ('teaching_methods', models.TextField(help_text='Teaching methods and strategies to be used')),
                ('assessment_methods', models.TextField(help_text='Assessment methods and evaluation criteria')),
                ('resources_needed', models.TextField(help_text='Resources and materials needed')),
                ('timeline', models.TextField(help_text='Timeline and schedule for topics')),
                ('achievements', models.TextField(blank=True, help_text='Achievements and successes (for end of term)')),
                ('challenges_encountered', models.TextField(blank=True, help_text='Challenges and problems encountered (for end of term)')),
                ('solutions_applied', models.TextField(blank=True, help_text='Solutions and strategies applied (for end of term)')),
                ('student_performance_analysis', models.TextField(blank=True, help_text='Analysis of student performance (for end of term)')),
                ('recommendations', models.TextField(blank=True, help_text='Recommendations for improvement (for end of term)')),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('submitted', 'Submitted'), ('reviewed', 'Reviewed'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='draft', max_length=20)),
                ('submitted_at', models.DateTimeField(blank=True, null=True)),
                ('reviewed_at', models.DateTimeField(blank=True, null=True)),
                ('review_comments', models.TextField(blank=True, help_text='Comments from academic master')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('class_obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workplans', to='edumanage.class')),
                ('reviewed_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviewed_workplans', to=settings.AUTH_USER_MODEL)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workplans', to='edumanage.subject')),
                ('submitted_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='received_workplans', to=settings.AUTH_USER_MODEL)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workplans', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Teacher Workplans',
                'ordering': ['-created_at'],
            },
        ),
    ]
