from typing import Match
from rest_framework import serializers
from gale.models import *


class MatchesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Matches
        fields = "__all__"
