# Generated by Django 2.2.6 on 2020-02-28 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Project Category',
                'verbose_name_plural': 'Project Categories',
            },
        ),
        migrations.DeleteModel(
            name='ProjectListingPage',
        ),
    ]