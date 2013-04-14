# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Schedule'
        db.create_table(u'leap_schedule', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('conference', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'leap', ['Schedule'])

        # Adding model 'Track'
        db.create_table(u'leap_track', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('schedule', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tracks', to=orm['leap.Schedule'])),
        ))
        db.send_create_signal(u'leap', ['Track'])

        # Adding model 'Type'
        db.create_table(u'leap_type', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('duration', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'leap', ['Type'])

        # Adding model 'Slot'
        db.create_table(u'leap_slot', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('track', self.gf('django.db.models.fields.related.ForeignKey')(related_name='slots', to=orm['leap.Track'])),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='slots', to=orm['leap.Type'])),
            ('start_time', self.gf('django.db.models.fields.TimeField')()),
        ))
        db.send_create_signal(u'leap', ['Slot'])


    def backwards(self, orm):
        # Deleting model 'Schedule'
        db.delete_table(u'leap_schedule')

        # Deleting model 'Track'
        db.delete_table(u'leap_track')

        # Deleting model 'Type'
        db.delete_table(u'leap_type')

        # Deleting model 'Slot'
        db.delete_table(u'leap_slot')


    models = {
        u'leap.schedule': {
            'Meta': {'object_name': 'Schedule'},
            'conference': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'leap.slot': {
            'Meta': {'object_name': 'Slot'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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