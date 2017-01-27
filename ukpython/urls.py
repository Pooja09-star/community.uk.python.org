from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^groups/$', views.user_groups, name='user-groups'),
    url(r'^groups/(?P<key>[\w-]+)/$', views.user_group, name='user-group'),
    url(r'events/$', views.future_events, name='future-events'),
    url(r'^groups-with-no-events-scheduled/(?P<year>\d+)/(?P<month>\d+)/$', views.user_groups_with_no_events_scheduled, name='user-groups-with-no-events-scheduled'),
]
