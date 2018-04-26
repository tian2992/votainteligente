from django.conf.urls import url
from backend_citizen.views import (IndexView,
                                   MyProposalsView,
                                   PopularProposalTemporaryDataUpdateView,
                                   UpdateUserView,
                                   DoYouBelongToAnOrgView,
                                   GroupRegistrationView,
                                   UpdateSubscription,
                                   AlreadyUnsubscribed,
                                   MySupportsView,
                                   MyStats,
                                   AddActivityToUserView,
                                   MyActivitiesListView,
                                   AllActivitiesListView,
                                   )
from django.contrib.auth.views import password_reset


urlpatterns = [
                        url(r'^$',
                           IndexView.as_view(),
                           name='index'),
                       url(r'^mis_propuestas/$',
                           MyProposalsView.as_view(),
                           name='my_proposals'),
                       url(r'^create_group/?$',
                           GroupRegistrationView.as_view(),
                           name='create_group'),
                       url(r'^add_activity/?$',
                           AddActivityToUserView.as_view(),
                           name='add_activity'),
                       url(r'^all_my_activities/?$',
                           MyActivitiesListView.as_view(),
                           name='all_my_activities'),
                       url(r'^all_activities/?$',
                           AllActivitiesListView.as_view(),
                           name='all_activities'),
                       url(r'^subscription/(?P<token>[-\w]+)/?$',
                           UpdateSubscription.as_view(),
                           name='unsuscribe'),
                       url(r'^already_unsuscribed/(?P<token>[-\w]+)/?$',
                           AlreadyUnsubscribed.as_view(),
                           name='already_unsuscribed'),
                       url(r'^update/?$',
                           UpdateUserView.as_view(),
                           name='update_my_profile'),
                       url(r'^my_supports/?$',
                           MySupportsView.as_view(),
                           name='my_supports'),
                       url(r'^stats/?$',
                           MyStats.as_view(),
                           name='stats'),
                       url(r'^do_you_belong_to_an_org/?$',
                           DoYouBelongToAnOrgView.as_view(),
                           name='do_you_belong_to_an_org'),
                       url(r'^update_temporary_data/(?P<pk>[\d]+)/?$',
                           PopularProposalTemporaryDataUpdateView.as_view(),
                           name='temporary_data_update'),
]
