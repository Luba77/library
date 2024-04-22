# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library', '0002_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookCopy',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, primary_key=True)),
                ('publisher_info', models.CharField(max_length=200)),
                ('due_back', models.DateField(null=True, blank=True)),
                ('status', models.CharField(default=b'd', max_length=1, blank=True, choices=[(b'un', b'Under maintenance'), (b'ch', b'Checked out'), (b'av', b'Available'), (b're', b'Reserved')])),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='library.Book', null=True)),
                ('borrower', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ['due_back'],
                'db_table': 'bookcopy',
            },
        ),
    ]
