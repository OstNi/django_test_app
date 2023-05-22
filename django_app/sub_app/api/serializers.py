from rest_framework import serializers

from sub_app.models import TimeRules
from sub_app.models import TwForYears
from sub_app.models import TwBlocks
from sub_app.models import DgrPeriods


class TimeRulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeRules
        fields = "__all__"


class TwForYearsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TwForYears
        fields = "__all__"


class TwBlocksSerializer(serializers.ModelSerializer):
    class Meta:
        model = TwBlocks
        fields = "__all__"


class DgrPeriodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DgrPeriods
        fields = "__all__"