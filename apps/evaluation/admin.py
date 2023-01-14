from django.contrib import admin

from apps.evaluation.models import Evaluation, Delivery, Config_Delivery_Rest, Observation, DeliveryPonderation
# Register your models here.

admin.site.register(Evaluation)
admin.site.register(Delivery)
admin.site.register(Config_Delivery_Rest)
admin.site.register(Observation)
admin.site.register(DeliveryPonderation)


