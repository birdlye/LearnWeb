# Generated by Django 2.2 on 2019-05-04 01:19

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, max_length=50)),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('markdown_content', models.TextField()),
                ('html_content', models.TextField(editable=False)),
                ('status', models.IntegerField(choices=[(1, 'Needs edits'), (2, 'Needs Approval'), (3, 'Published'), (4, 'Achived')], default=1)),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
                ('modified', models.DateTimeField(default=datetime.datetime.now)),
                ('category', models.ForeignKey(on_delete=True, to='cms.Category')),
                ('owner', models.ForeignKey(on_delete=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'stories',
                'ordering': ['modified'],
            },
        ),
    ]
