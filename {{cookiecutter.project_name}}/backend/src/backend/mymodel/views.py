from rest_framework import viewsets

import backend.mymodel.models as models
import backend.mymodel.serialisers as serialisers


class DummyViewSet(viewsets.ModelViewSet):
    queryset = models.DummyTable.objects.all().order_by("created")
    serializer_class = serialisers.DummySerialiser
