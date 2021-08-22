from django.contrib import admin
from .models import Stripe


class StripeAdmin(admin.ModelAdmin):
    list_display = ('client_id', 'secret_key')


admin.site.register(Stripe, StripeAdmin)