# Create your views here.
import os

from django.contrib.auth.decorators import login_required
from django.contrib.formtools.wizard.views import SessionWizardView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView, ListView
from jfu.http import upload_receive, UploadResponse, JFUResponse

from rbp import settings
from promotions.forms import PromotionWizardDetailsPage, PromotionWizardLayoutPage
from promotions.models import PromotionAudioItem, Promotion

FORMS = [
    ("details", PromotionWizardDetailsPage),
    ("layout", PromotionWizardLayoutPage),
]
TEMPLATES = {"details": "promotions/_wizard_details.html",
             "layout": "promotions/_wizard_layout.html",
             "cc": "checkout/creditcard.html",
             "confirmation": "checkout/confirmation.html"}


class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        context = {
            'content': 'Hello Sailor'
        }
        return self.render_to_response(context)


class PromotionWizard(SessionWizardView):
    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def get_form_initial(self, step):
        if 'promotion_id' in self.kwargs and step == 'details':
            promotion_id = self.kwargs['promotion_id']
            promotion = Promotion.objects.get(id=promotion_id)
            from django.forms.models import model_to_dict
            project_dict = model_to_dict(promotion)
            return project_dict
        else:
            return self.initial_dict.get(step, {})

    def done(self, form_list, **kwargs):
        instance = Promotion()
        instance.user = self.request.user
        for form in form_list:
            for field, value in form.cleaned_data.iteritems():
                setattr(instance, field, value)
        instance.save()

        return HttpResponseRedirect(reverse('promotion-list'))


class PromotionList(ListView):
    model = Promotion
    template_name = 'promotions/list.html'

    def get_queryset(self):
        return Promotion.objects.filter(user=self.request.user)


@require_POST
@login_required
def upload(request):
    # The assumption here is that jQuery File Upload
    # has been configured to send files one at a time.
    # If multiple files can be uploaded simulatenously,
    # 'file' may be a list of files.

    file = upload_receive(request)

    instance = PromotionAudioItem(file_field=file)
    instance.save()

    basename = os.path.basename(instance.file_field.file.name)
    file_dict = {
        'name': basename,
        'size': instance.file_field.file.size,

        # The assumption is that file_field is a FileField that saves to
        # the 'media' directory.
        'url': settings.MEDIA_URL + basename,
        'thumbnail_url': settings.MEDIA_URL + basename,


        'delete_url': reverse('audio_delete', kwargs={'pk': instance.pk}),
        'delete_type': 'POST',
    }

    return UploadResponse(request, file_dict)


@require_POST
@login_required
def upload_delete(request, pk):
    # An example implementation.
    success = True
    try:
        instance = PromotionAudioItem.objects.get(pk=pk)
        os.unlink(instance.file_field.file.name)
        instance.delete()
    except PromotionAudioItem.DoesNotExist:
        success = False

    return JFUResponse(request, success)
