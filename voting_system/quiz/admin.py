from django.contrib import admin

import quiz.models as models
import polls.models

admin.site.register(models.Quiz)
