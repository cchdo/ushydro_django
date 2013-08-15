# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Ship'
        db.create_table(u'hydrotable_ship', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'hydrotable', ['Ship'])

        # Adding model 'Cruise'
        db.create_table(u'hydrotable_cruise', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
            ('expocode', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('stations', self.gf('django.db.models.fields.IntegerField')()),
            ('start_port', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('end_port', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('chief_scientist', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('ship', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hydrotable.Ship'])),
            ('expocode_link', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'hydrotable', ['Cruise'])

        # Adding model 'Parameter'
        db.create_table(u'hydrotable_parameter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'hydrotable', ['Parameter'])

        # Adding model 'Institution'
        db.create_table(u'hydrotable_institution', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('abrev', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'hydrotable', ['Institution'])

        # Adding model 'PI'
        db.create_table(u'hydrotable_pi', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('institution', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hydrotable.Institution'])),
        ))
        db.send_create_signal(u'hydrotable', ['PI'])

        # Adding model 'Program'
        db.create_table(u'hydrotable_program', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cruise', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hydrotable.Cruise'])),
            ('parameter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hydrotable.Parameter'])),
            ('pi', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hydrotable.PI'])),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'hydrotable', ['Program'])


    def backwards(self, orm):
        # Deleting model 'Ship'
        db.delete_table(u'hydrotable_ship')

        # Deleting model 'Cruise'
        db.delete_table(u'hydrotable_cruise')

        # Deleting model 'Parameter'
        db.delete_table(u'hydrotable_parameter')

        # Deleting model 'Institution'
        db.delete_table(u'hydrotable_institution')

        # Deleting model 'PI'
        db.delete_table(u'hydrotable_pi')

        # Deleting model 'Program'
        db.delete_table(u'hydrotable_program')


    models = {
        u'hydrotable.cruise': {
            'Meta': {'object_name': 'Cruise'},
            'chief_scientist': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
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