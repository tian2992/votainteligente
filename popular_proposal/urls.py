from django.conf.urls import patterns, url
from popular_proposal.views import (ProposalCreationView,
                                    ThanksForProposingView,
                                    SubscriptionView,
                                    HomeView,
                                    PopularProposalDetailView,
                                    PopularProposalUpdateView,
                                    ProposalWizard,
                                    ProposalWizardFull,
                                    UnlikeProposalView,
                                    )

urlpatterns = patterns('',
    url(r'^$',
        HomeView.as_view(),
        name='home'),
    url(r'^create_wizard/(?P<slug>[-\w]+)/?$',
        ProposalWizard.as_view(),
        name='propose_wizard'),
    url(r'^create_wizard_full/?$',
        ProposalWizardFull.as_view(),
        name='propose_wizard_full'),
    url(r'^detail/(?P<slug>[-\w]+)/?$',
        PopularProposalDetailView.as_view(),
        name='detail'),
    url(r'^unlike/(?P<pk>\d+)/?$',
        UnlikeProposalView.as_view(),
        name='unlike_proposal'),
    url(r'^actualizar/(?P<slug>[-\w]+)/?$',
        PopularProposalUpdateView.as_view(),
        name='citizen_update'),
    url(r'^(?P<slug>[-\w]+)/?$',
        ProposalCreationView.as_view(),
        name='propose'),
    url(r'^(?P<pk>[-\w]+)/gracias/?$',
        ThanksForProposingView.as_view(),
        name='thanks'),
    url(r'^(?P<pk>[-\w]+)/subscribe/?$',
        SubscriptionView.as_view(),
        name='like_a_proposal'),
)
