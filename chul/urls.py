from django.conf.urls import url, patterns

from .views import(
    CommunityHealthUnitListView,
    CommunityHealthUnitDetailView,
    CommunityHealthWorkerListView,
    CommunityHealthWorkerDetailView,
    CommunityHealthWorkerContactListView,
    CommunityHealthWorkerContactDetailView,
    StatusListView,
    StatusDetailView,
    CommunityHealthUnitContactListView,
    CommunityHealthUnitContactDetailView,
    CHUServiceListView,
    CHUServiceDetailView,
    CHURatingDetailView,
    CHURatingListView,
    ChuUpdateBufferListView,
    ChuUpdateBufferDetailView
)


urlpatterns = patterns(
    '',

    url(r'^updates/$', ChuUpdateBufferListView.as_view(),
        name='chu_updatebufers_list'),

    url(r'^updates/(?P<pk>[^/]+)/$',
        ChuUpdateBufferDetailView.as_view(),
        name="chu_updatebuffer_detail"),

    url(r'^services/$', CHUServiceListView.as_view(),
        name='chu_services_list'),
    url(r'^services/(?P<pk>[^/]+)/$',
        CHUServiceDetailView.as_view(),
        name="chu_service_detail"),

    url(r'^statuses/$', StatusListView.as_view(),
        name='statuses_list'),
    url(r'^statuses/(?P<pk>[^/]+)/$',
        StatusDetailView.as_view(),
        name="status_detail"),

    url(r'^unit_contacts/$', CommunityHealthUnitContactListView.as_view(),
        name='community_health_unit_contacts_list'),
    url(r'^unit_contacts/(?P<pk>[^/]+)/$',
        CommunityHealthUnitContactDetailView.as_view(),
        name="community_health_unit_contact_detail"),

    url(r'^workers/$', CommunityHealthWorkerListView.as_view(),
        name='community_health_workers_list'),
    url(r'^workers/(?P<pk>[^/]+)/$',
        CommunityHealthWorkerDetailView.as_view(),
        name="community_health_worker_detail"),


    url(r'^workers_contacts/$', CommunityHealthWorkerContactListView.as_view(),
        name='community_health_worker_contacts_list'),
    url(r'^workers_contacts/(?P<pk>[^/]+)/$',
        CommunityHealthWorkerContactDetailView.as_view(),
        name="community_health_worker_contact_detail"),


    url(r'^units/$', CommunityHealthUnitListView.as_view(),
        name='community_health_units_list'),
    url(r'^units/(?P<pk>[^/]+)/$',
        CommunityHealthUnitDetailView.as_view(),
        name='community_health_unit_detail'),

    url(r'^chu_ratings/$', CHURatingListView.as_view(), name='chu_ratings'),
    url(r'^chu_ratings/(?P<pk>[a-z0-9\-]{32,32})/$',
        CHURatingDetailView.as_view(), name='chu_rating_detail')
)
