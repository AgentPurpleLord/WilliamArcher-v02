# Generated by Django 3.0.3 on 2020-03-01 00:15

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_auto_20200301_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectdetailpage',
            name='categories',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='project.ProjectCategory'),
        ),
        migrations.DeleteModel(
            name='ProjectCategoryOrderable',
        ),
    ]
