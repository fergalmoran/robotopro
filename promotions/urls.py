from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from promotions import views
from promotions.forms import PromotionWizardDetailsPage, PromotionWizardLayoutPage
from promotions.views import IndexView, PromotionList, PromotionWizard, FORMS

urlpatterns = patterns(
    '',
    url(r'^$', IndexView.as_view(), name='home'),
    
    url(r'promotions/$', login_required(PromotionList.as_view()), name='promotion-list'),
    url(r'promotions/add/$', login_required(PromotionWizard.as_view(FORMS)), name='promotion-add'),
    url(r'promotions/edit/(?P<promotion_id>[-\d]+)$', login_required(PromotionWizard.as_view(FORMS)), name='promotion-edit'),

    url( r'^audio/upload/', views.upload, name = 'audio_upload' ),
    url( r'^audio/delete/(?P<pk>\d+)$', views.upload_delete, name = 'audio_delete' ),
)