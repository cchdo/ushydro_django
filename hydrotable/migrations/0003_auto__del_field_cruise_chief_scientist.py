# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Cruise.chief_scientist'
        db.delete_column(u'hydrotable_cruise', 'chief_scientist')

        # Adding M2M table for field chief_scientist on 'Cruise'
        m2m_table_name = db.shorten_name(u'hydrotable_cruise_chief_scientist')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('cruise', models.ForeignKey(orm[u'hydrotable.cruise'], null=False)),
            ('pi', models.ForeignKey(orm[u'hydrotable.pi'], null=False))
        ))
        db.create_unique(m2m_table_name, ['cruise_id', 'pi_id'])


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Cruise.chief_scientist'
        raise RuntimeError("Cannot reverse this migration. 'Cruise.chief_scientist' and its values cannot be restored.")
        # Removing M2M table for field chief_scientist on 'Cruise'
        db.delete_table(db.shorten_name(u'hydrotable_cruise_chief_scientist'))


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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_data': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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