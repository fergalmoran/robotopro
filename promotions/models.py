from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from rbp.settings import MEDIA_ROOT
from django.db import models


class Promotion(models.Model):
    user = models.ForeignKey(User)

    description = models.CharField(max_length=250)
    body_text = models.TextField(blank=True, null=True)
    date_created = models.DateField(auto_now=True)

    start_date = models.DateField()
    end_date = models.DateField()
    active = models.BooleanField()

    def get_absolute_url(self):
        return reverse('promo_update', kwargs={'pk': self.pk})


class PromotionAudioItem(models.Model):
    description = models.CharField(max_length=250)
    file_field = models.FileField(upload_to=MEDIA_ROOT)
    date_created = models.DateField(auto_now=True)

