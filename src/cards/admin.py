from django.contrib import admin
from cards.models import Card


class CardAdmin(admin.ModelAdmin):
    model = Card


admin.site.register(Card, CardAdmin)
