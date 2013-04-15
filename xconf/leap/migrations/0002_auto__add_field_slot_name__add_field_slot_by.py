# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Slot.name'
        db.add_column(u'leap_slot', 'name',
                      self.gf('django.db.models.fields.CharField')(default='Slot', max_length=300),
                      keep_default=False)

        # Adding field 'Slot.by'
        db.add_column(u'leap_slot', 'by',
                      self.gf('django.db.models.fields.CharField')(default='admin', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Slot.name'
        db.delete_column(u'leap_slot', 'name')

        # Deleting field 'Slot.by'
        db.delete_column(u'leap_slot', 'by')


    models = {
        u'leap.schedule': {
            'Meta': {'object_name': 'Schedule'},
            'conference': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'leap.slot': {
            'Meta': {'object_name': 'Slot'},
            'by': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'start_time': ('django.db.models.fields.TimeField', [], {}),
            'track': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'slots'", 'to': u"orm['leap.Track']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'slots'", 'to': u"orm['leap.Type']"})
        },
        u'leap.track': {
            'Meta': {'object_name': 'Track'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'schedule': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tracks'", 'to': u"orm['leap.Schedule']"})
        },
        u'leap.type': {
            'Meta': {'object_name': 'Type'},
            'duration': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['leap']