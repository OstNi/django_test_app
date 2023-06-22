from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response

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
from sub_app.models import Versions

from sub_app.api.exeptions import DgrCreateExc


class VersionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Versions
        fields = "__all__"


class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Divisions
        fields = "__all__"


class TyperiodSerializer(serializers.ModelSerializer):
    class Meta:
        model = TyPeriods
        fields = "__all__"


class TprChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = TprChapters
        fields = "__all__"


class WorkTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkTypes
        fields = "__all__"

class StuGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = StuGroups
        fields = "__all__"


class GroupWorkSerializer(serializers.ModelSerializer):
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
    sgr_sgr = StuGroupSerializer()
    tpr_name = serializers.SlugRelatedField(
        read_only=True,
        slug_field="name",
        many=False,
        source="tch_tch"
    )

    sgr_name = serializers.SlugRelatedField(
        read_only=True,
        slug_field="name",
        many=False,
        source="sgr_sgr"
    )

    div_name = serializers.SlugRelatedField(
        read_only=True,
        slug_field="name",
        many=False,
        source="div_div"
    )

    ver_info = serializers.SlugRelatedField(
        read_only=True,
        slug_field="info",
        many=False,
        source="ver_ver"
    )

    class Meta:
        model = DgrPeriods
        fields = "__all__"

    def create(self, validated_data):
        stu_data = validated_data.pop('sgr_sgr')
        stu_serializer = StuGroupSerializer(data=stu_data)
        stu_serializer.is_valid(raise_exception=True)
        stu_object = stu_serializer.save()
        dgr_period = DgrPeriods.objects.create(sgr_sgr=stu_object, **validated_data)
        return dgr_period

    
    # def to_internal_value(self, data):
    #     return data

    # def create(self, validated_data):
        # try:
        #     dgr = DgrPeriods(
        #         typ_typ_id=validated_data.get("typ_typ"),
        #         sgr_sgr_id=validated_data.get("sgr_sgr"),
        #         tch_tch_id=validated_data.get("tch_tch"),
        #         div_div_id=validated_data.get("div_div"),
        #         ver_ver_id=validated_data.get("ver_ver")
        #     )
        #     dgr.save()
        #     responsed_data = {
        #         "ID": dgr.dgp_id,
        #         "TPR_CHAPTER": dgr.tch_tch.name,
        #         "STU_GROUP": dgr.sgr_sgr.name,
        #         "TY_PERIOD": dgr.typ_typ.typ_id,
        #         "DIVISION": dgr.div_div.name,
        #         "VERSION": dgr.ver_ver.info
        #     }
        #     return Response(responsed_data, status=status.HTTP_201_CREATED)
        # except DgrCreateExc as e:
        #     responsed_data = {
        #         "ARGS": ' '.join(e.args)
        #     }
        #     return Response(responsed_data, status=status.HTTP_201_CREATED)
        
            
       
