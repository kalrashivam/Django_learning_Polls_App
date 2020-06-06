from django.contrib import admin

import polls.models as models

admin.site.register(models.Question)
admin.site.register(models.Choice)
