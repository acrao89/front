from django.contrib import admin
from .models import CollectEmail


class CollectEmailAdmin(admin.ModelAdmin):
	class Meta:
		model = CollectEmail
admin.site.register(CollectEmail, CollectEmailAdmin)