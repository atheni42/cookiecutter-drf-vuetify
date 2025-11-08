from rest_framework import serializers

import backend.mymodel.models as models


class TagSerialiser(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = "__all__"


class DummySerialiser(serializers.ModelSerializer):
    tags = TagSerialiser(many=True)

    class Meta:
        model = models.DummyTable
        fields = "__all__"
