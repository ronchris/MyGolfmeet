# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Event.owner'
        db.delete_column(u'golfapp_event', 'owner_id')


    def backwards(self, orm):
        # Adding field 'Event.owner'
        db.add_column(u'golfapp_event', 'owner',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, on_delete=models.SET_NULL, blank=True),
                      keep_default=False)


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'golfapp.course': {
            'Meta': {'object_name': 'Course'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'course_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'zip': ('django.db.models.fields.IntegerField', [], {'max_length': '5'})
        },
        u'golfapp.course_score': {
            'Meta': {'object_name': 'Course_Score'},
            'courses': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'courses_rel_+'", 'blank': 'True', 'to': u"orm['golfapp.Course_Score']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'golfcourse_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['golfapp.Course']"}),
            'hole_01': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'hole_02': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'hole_03': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'hole_04': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'hole_05': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'hole_06': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'hole_07': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'hole_08': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'hole_09': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'hole_10': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'hole_11': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'hole_12': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'hole_13': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'hole_14': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'hole_15': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'hole_16': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'hole_17': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'hole_18': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'golfapp.event': {
            'Meta': {'object_name': 'Event'},
            'attendees': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['golfapp.UserInfo']", 'null': 'True', 'blank': 'True'}),
            'course': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'golfapp.feed': {
            'Meta': {'object_name': 'Feed'},
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'feed': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'golfapp.friendship': {
            'Meta': {'unique_together': "(('to_friend', 'from_friend'),)", 'object_name': 'Friendship'},
            'from_friend': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'friend_set'", 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'to_friend': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'to_friend_set'", 'to': u"orm['auth.User']"})
        },
        u'golfapp.game': {
            'Meta': {'object_name': 'Game'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'golfcourse_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['golfapp.Course']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'user_id1': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'player1'", 'symmetrical': 'False', 'to': u"orm['auth.User']"}),
            'user_id2': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'player2'", 'symmetrical': 'False', 'to': u"orm['auth.User']"}),
            'user_id3': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'player3'", 'symmetrical': 'False', 'to': u"orm['auth.User']"}),
            'user_id4': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'player4'", 'symmetrical': 'False', 'to': u"orm['auth.User']"})
        },
        u'golfapp.game_holes': {
            'Meta': {'object_name': 'Game_Holes'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user_id1': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'player1'", 'symmetrical': 'False', 'to': u"orm['golfapp.Game']"}),
            'user_id2': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'player2'", 'symmetrical': 'False', 'to': u"orm['golfapp.Game']"}),
            'user_id3': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'player3'", 'symmetrical': 'False', 'to': u"orm['golfapp.Game']"}),
            'user_id4': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'player4'", 'symmetrical': 'False', 'to': u"orm['golfapp.Game']"})
        },
        u'golfapp.userinfo': {
            'Meta': {'object_name': 'UserInfo'},
            'about_me': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'birth_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'buddies': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'buddies_rel_+'", 'blank': 'True', 'to': u"orm['golfapp.UserInfo']"}),
            'company': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'degree': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'education': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'from_date_ed': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'from_date_org': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'industry': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'occupation': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'org_location': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'organization': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'skill_level': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'to_date_ed': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'to_date_org': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'info'", 'unique': 'True', 'to': u"orm['auth.User']"}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['golfapp']