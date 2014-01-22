# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserInfo'
        db.create_table(u'golfapp_userinfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('birth_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('skill_level', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('industry', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('occupation', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('company', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('education', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('degree', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('from_date_ed', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('to_date_ed', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('organization', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('org_location', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('about_me', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('from_date_org', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('to_date_org', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'golfapp', ['UserInfo'])

        # Adding M2M table for field buddies on 'UserInfo'
        m2m_table_name = db.shorten_name(u'golfapp_userinfo_buddies')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_userinfo', models.ForeignKey(orm[u'golfapp.userinfo'], null=False)),
            ('to_userinfo', models.ForeignKey(orm[u'golfapp.userinfo'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_userinfo_id', 'to_userinfo_id'])

        # Adding model 'Course'
        db.create_table(u'golfapp_course', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('course_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('zip', self.gf('django.db.models.fields.IntegerField')(max_length=5)),
        ))
        db.send_create_signal(u'golfapp', ['Course'])

        # Adding model 'Course_Score'
        db.create_table(u'golfapp_course_score', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('golfcourse_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['golfapp.Course'])),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('hole_01', self.gf('django.db.models.fields.IntegerField')(max_length=2)),
            ('hole_02', self.gf('django.db.models.fields.IntegerField')(max_length=2)),
            ('hole_03', self.gf('django.db.models.fields.IntegerField')(max_length=2)),
            ('hole_04', self.gf('django.db.models.fields.IntegerField')(max_length=2)),
            ('hole_05', self.gf('django.db.models.fields.IntegerField')(max_length=2)),
            ('hole_06', self.gf('django.db.models.fields.IntegerField')(max_length=2)),
            ('hole_07', self.gf('django.db.models.fields.IntegerField')(max_length=2)),
            ('hole_08', self.gf('django.db.models.fields.IntegerField')(max_length=2)),
            ('hole_09', self.gf('django.db.models.fields.IntegerField')(max_length=2)),
            ('hole_10', self.gf('django.db.models.fields.IntegerField')(max_length=2)),
            ('hole_11', self.gf('django.db.models.fields.IntegerField')(max_length=2)),
            ('hole_12', self.gf('django.db.models.fields.IntegerField')(max_length=2)),
            ('hole_13', self.gf('django.db.models.fields.IntegerField')(max_length=2)),
            ('hole_14', self.gf('django.db.models.fields.IntegerField')(max_length=2)),
            ('hole_15', self.gf('django.db.models.fields.IntegerField')(max_length=2)),
            ('hole_16', self.gf('django.db.models.fields.IntegerField')(max_length=2)),
            ('hole_17', self.gf('django.db.models.fields.IntegerField')(max_length=2)),
            ('hole_18', self.gf('django.db.models.fields.IntegerField')(max_length=2)),
        ))
        db.send_create_signal(u'golfapp', ['Course_Score'])

        # Adding M2M table for field courses on 'Course_Score'
        m2m_table_name = db.shorten_name(u'golfapp_course_score_courses')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_course_score', models.ForeignKey(orm[u'golfapp.course_score'], null=False)),
            ('to_course_score', models.ForeignKey(orm[u'golfapp.course_score'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_course_score_id', 'to_course_score_id'])

        # Adding model 'Game'
        db.create_table(u'golfapp_game', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('time', self.gf('django.db.models.fields.DateTimeField')()),
            ('golfcourse_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['golfapp.Course'])),
        ))
        db.send_create_signal(u'golfapp', ['Game'])

        # Adding M2M table for field user_id1 on 'Game'
        m2m_table_name = db.shorten_name(u'golfapp_game_user_id1')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('game', models.ForeignKey(orm[u'golfapp.game'], null=False)),
            ('user', models.ForeignKey(orm[u'auth.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['game_id', 'user_id'])

        # Adding M2M table for field user_id2 on 'Game'
        m2m_table_name = db.shorten_name(u'golfapp_game_user_id2')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('game', models.ForeignKey(orm[u'golfapp.game'], null=False)),
            ('user', models.ForeignKey(orm[u'auth.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['game_id', 'user_id'])

        # Adding M2M table for field user_id3 on 'Game'
        m2m_table_name = db.shorten_name(u'golfapp_game_user_id3')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('game', models.ForeignKey(orm[u'golfapp.game'], null=False)),
            ('user', models.ForeignKey(orm[u'auth.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['game_id', 'user_id'])

        # Adding M2M table for field user_id4 on 'Game'
        m2m_table_name = db.shorten_name(u'golfapp_game_user_id4')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('game', models.ForeignKey(orm[u'golfapp.game'], null=False)),
            ('user', models.ForeignKey(orm[u'auth.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['game_id', 'user_id'])

        # Adding model 'Game_Invite'
        db.create_table(u'golfapp_game_invite', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('game_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['golfapp.Game'])),
            ('hostuser_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'golfapp', ['Game_Invite'])

        # Adding model 'Game_Holes'
        db.create_table(u'golfapp_game_holes', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'golfapp', ['Game_Holes'])

        # Adding M2M table for field user_id1 on 'Game_Holes'
        m2m_table_name = db.shorten_name(u'golfapp_game_holes_user_id1')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('game_holes', models.ForeignKey(orm[u'golfapp.game_holes'], null=False)),
            ('game', models.ForeignKey(orm[u'golfapp.game'], null=False))
        ))
        db.create_unique(m2m_table_name, ['game_holes_id', 'game_id'])

        # Adding M2M table for field user_id2 on 'Game_Holes'
        m2m_table_name = db.shorten_name(u'golfapp_game_holes_user_id2')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('game_holes', models.ForeignKey(orm[u'golfapp.game_holes'], null=False)),
            ('game', models.ForeignKey(orm[u'golfapp.game'], null=False))
        ))
        db.create_unique(m2m_table_name, ['game_holes_id', 'game_id'])

        # Adding M2M table for field user_id3 on 'Game_Holes'
        m2m_table_name = db.shorten_name(u'golfapp_game_holes_user_id3')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('game_holes', models.ForeignKey(orm[u'golfapp.game_holes'], null=False)),
            ('game', models.ForeignKey(orm[u'golfapp.game'], null=False))
        ))
        db.create_unique(m2m_table_name, ['game_holes_id', 'game_id'])

        # Adding M2M table for field user_id4 on 'Game_Holes'
        m2m_table_name = db.shorten_name(u'golfapp_game_holes_user_id4')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('game_holes', models.ForeignKey(orm[u'golfapp.game_holes'], null=False)),
            ('game', models.ForeignKey(orm[u'golfapp.game'], null=False))
        ))
        db.create_unique(m2m_table_name, ['game_holes_id', 'game_id'])

        # Adding model 'Feed'
        db.create_table(u'golfapp_feed', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('feed', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
        ))
        db.send_create_signal(u'golfapp', ['Feed'])


    def backwards(self, orm):
        # Deleting model 'UserInfo'
        db.delete_table(u'golfapp_userinfo')

        # Removing M2M table for field buddies on 'UserInfo'
        db.delete_table(db.shorten_name(u'golfapp_userinfo_buddies'))

        # Deleting model 'Course'
        db.delete_table(u'golfapp_course')

        # Deleting model 'Course_Score'
        db.delete_table(u'golfapp_course_score')

        # Removing M2M table for field courses on 'Course_Score'
        db.delete_table(db.shorten_name(u'golfapp_course_score_courses'))

        # Deleting model 'Game'
        db.delete_table(u'golfapp_game')

        # Removing M2M table for field user_id1 on 'Game'
        db.delete_table(db.shorten_name(u'golfapp_game_user_id1'))

        # Removing M2M table for field user_id2 on 'Game'
        db.delete_table(db.shorten_name(u'golfapp_game_user_id2'))

        # Removing M2M table for field user_id3 on 'Game'
        db.delete_table(db.shorten_name(u'golfapp_game_user_id3'))

        # Removing M2M table for field user_id4 on 'Game'
        db.delete_table(db.shorten_name(u'golfapp_game_user_id4'))

        # Deleting model 'Game_Invite'
        db.delete_table(u'golfapp_game_invite')

        # Deleting model 'Game_Holes'
        db.delete_table(u'golfapp_game_holes')

        # Removing M2M table for field user_id1 on 'Game_Holes'
        db.delete_table(db.shorten_name(u'golfapp_game_holes_user_id1'))

        # Removing M2M table for field user_id2 on 'Game_Holes'
        db.delete_table(db.shorten_name(u'golfapp_game_holes_user_id2'))

        # Removing M2M table for field user_id3 on 'Game_Holes'
        db.delete_table(db.shorten_name(u'golfapp_game_holes_user_id3'))

        # Removing M2M table for field user_id4 on 'Game_Holes'
        db.delete_table(db.shorten_name(u'golfapp_game_holes_user_id4'))

        # Deleting model 'Feed'
        db.delete_table(u'golfapp_feed')


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
        u'golfapp.feed': {
            'Meta': {'object_name': 'Feed'},
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'feed': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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
        u'golfapp.game_invite': {
            'Meta': {'object_name': 'Game_Invite'},
            'game_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['golfapp.Game']"}),
            'hostuser_id': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '30'})
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
            'skill_level': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'to_date_ed': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'to_date_org': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['golfapp']