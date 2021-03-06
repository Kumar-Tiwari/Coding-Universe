# Generated by Django 3.0.5 on 2020-04-14 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_auto_20200414_2239'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='question_1_sample_2',
            field=models.CharField(default='C', max_length=500),
        ),
        migrations.AddField(
            model_name='questions',
            name='question_1_sample_3',
            field=models.CharField(default='G', max_length=500),
        ),
        migrations.AddField(
            model_name='questions',
            name='question_1_sample_explain',
            field=models.CharField(blank=True, default='In Sample case #1, the combo for C-Major Chord is displayed according to gradual increase in note according to given pattern.', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='questions',
            name='question_1_sample_output_2',
            field=models.CharField(default='C,E,G', max_length=10),
        ),
        migrations.AddField(
            model_name='questions',
            name='question_1_sample_output_3',
            field=models.CharField(default='G,B,D', max_length=10),
        ),
    ]
