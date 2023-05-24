from rest_framework import serializers

from sub_app.models import TimeRules
from sub_app.models import TwForYears
from sub_app.models import TwBlocks
from sub_app.models import DgrPeriods
from sub_app.models import StuGroups
from sub_app.models import GroupWorks
from sub_app.models import WorkTypes
from sub_app.models import TyPeriods
from sub_app.models import Divisions
from sub_app.models import TprChapters


class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Divisions
        fields = ["div_id", "name"]


class TyperiodSerializer(serializers.ModelSerializer):
    class Meta:
        model = TyPeriods
        fields = ["typ_id"]


class TprChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = TprChapters
        fields = ["tch_id", "name"]


class WorkTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkTypes
        fields = ["wot_id", "name"]

class StuGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = StuGroups
        fields = "__all__"


class GroupWorkSerializer(serializers.ModelSerializer):
    sgr_sgr = StuGroupSerializer()
    wt_wot = WorkTypeSerializer()
    class Meta:
        model = GroupWorks
        fields = "__all__"


class TimeRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeRules
        fields = "__all__"


class TwForYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = TwForYears
        fields = "__all__"


class TwBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = TwBlocks
        fields = "__all__"


class DgrPeriodSerializer(serializers.ModelSerializer):
    tch_tch = TprChapterSerializer()
    sgr_sgr = StuGroupSerializer()
    typ_typ = TyperiodSerializer()
    div_div = DivisionSerializer()
    class Meta:
        model = DgrPeriods
        fields = "__all__"