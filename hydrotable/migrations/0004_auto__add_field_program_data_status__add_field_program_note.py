# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Program.data_status'
        db.add_column(u'hydrotable_program', 'data_status',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'Program.note'
        db.add_column(u'hydrotable_program', 'note',
                      self.gf('django.db.models.fields.TextField')(null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Program.data_status'
        db.delete_column(u'hydrotable_program', 'data_status')

        # Deleting field 'Program.note'
        db.delete_column(u'hydrotable_program', 'note')


    models = {
        u'hydrotable.cruise': {
            'Meta': {'object_name': 'Cruise'},
            'chief_scientist': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['hydrotable.PI']", 'symmetrical': 'False'}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'end_port': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'expocode': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'expocode_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ship': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hydrotable.Ship']"}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'start_port': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'stations': ('django.db.models.fields.IntegerField', [], {})
        },
        u'hydrotable.institution': {
            'Meta': {'object_name': 'Institution'},
            'abrev': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'hydrotable.parameter': {
            'Meta': {'ordering': "('order',)", 'object_name': 'Parameter'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'hydrotable.pi': {
            'Meta': {'object_name': 'PI'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institution': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hydrotable.Institution']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'hydrotable.program': {
            'Meta': {'object_name': 'Program'},
            'cruise': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hydrotable.Cruise']"}),
            'data_status': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_data': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'note': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'parameter': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hydrotable.Parameter']"}),
            'pi': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hydrotable.PI']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'hydrotable.ship': {
            'Meta': {'object_name': 'Ship'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['hydrotable']