# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=1000)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='library.Author', null=True)),
                ('genre', models.ManyToManyField(help_text=b'Select a genre for this book', to='library.Genre')),
            ],
            options={
                'ordering': ['title', 'author'],
                'db_table': 'book',
            },
        ),
    ]
