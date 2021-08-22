from django.db import models


class Stripe(models.Model):
    client_id = models.CharField(max_length=255, blank=True)
    secret_key = models.CharField(max_length=255)

    def __str__(self):
        return self.client_id
