from django.contrib import admin

import backend.mymodel.models as models

admin.site.register(models.Tag)
admin.site.register(models.DummyTable)
