from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Enable admin
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # User urls
    url(r'^$', 'golfapp.views.home_view', name='home_view'),
    url(r'^signup/$', 'golfapp.views.signup_view', name='signup_view'),
    url(r'^login/$', 'golfapp.views.login_view', name='login_view'),
    url(r'^logout/$', 'golfapp.views.logout_view', name='logout_view'),
    url(r'^thanks/$', 'golfapp.views.show_thanks', name='show_thanks'),
    url(r'^incorrect/$', 'golfapp.views.incorrect_view', name='incorrect_view'),
    url(r'^dashboard/$', 'golfapp.views.show_dashboard', name='show_dashboard'),
    url(r'^dashboard/search/$', 'golfapp.views.search', name='search'),
    url(r'^dashboard/profile/$', 'golfapp.views.create_profile', name='create_profile'),
    url(r'^dashboard/profile/profile_view/$', 'golfapp.views.view_profile', name='view_profile'),
    url(r'^dashboard/tracker/$', 'golfapp.views.view_tracker', name='view_tracker'),
    url(r'^map/$', 'golfapp.views.show_map', name='show_map'),
    url(r'^calendar/plus/(\d+)/$', 'golfapp.views.show_cal', name='show_cal'),
    url(r'^event/$', 'golfapp.views.show_event', name='show_event'),

    #url(r'^golfapp/(?P<poll_id>\d+)/(?P<answer_id>\d+)$', 'polls.views.vote_for_answer', name='vote_for_answer')
)
