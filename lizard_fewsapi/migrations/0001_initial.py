# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FewsInstance'
        db.create_table('lizard_fewsapi_fewsinstance', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=255)),
        ))
        db.send_create_signal('lizard_fewsapi', ['FewsInstance'])


    def backwards(self, orm):
        # Deleting model 'FewsInstance'
        db.delete_table('lizard_fewsapi_fewsinstance')


    models = {
        'lizard_fewsapi.fewsinstance': {
            'Meta': {'ordering': "[u'url']", 'object_name': 'FewsInstance'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['lizard_fewsapi']