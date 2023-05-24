from rest_framework import viewsets

from sub_app.api.serializers import TimeRuleSerializer
from sub_app.api.serializers import TwForYearSerializer
from sub_app.api.serializers import TwBlockSerializer
from sub_app.api.serializers import DgrPeriodSerializer
from sub_app.api.serializers import StuGroupSerializer
from sub_app.api.serializers import GroupWorkSerializer
from sub_app.api.serializers import DivisionSerializer
from sub_app.api.serializers import TprChapterSerializer
from sub_app.api.serializers import TyperiodSerializer
from sub_app.api.serializers import WorkTypeSerializer


from sub_app.api.filtersets import StuGroupFilterSet
from sub_app.api.filtersets import DivisionFilterSet
from sub_app.api.filtersets import TprChapterFilterSet
from sub_app.api.filtersets import WorkTypeFilterSet


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



class StuGroupViewSet(viewsets.ModelViewSet):
    queryset = StuGroups.objects.all()
    serializer_class = StuGroupSerializer
    filterset_class = StuGroupFilterSet


class DivisionViewSet(viewsets.ModelViewSet):
    queryset = Divisions.objects.all()
    serializer_class = DivisionSerializer
    filterset_class = DivisionFilterSet


class WorkTypeViewSet(viewsets.ModelViewSet):
    queryset = WorkTypes.objects.all()
    serializer_class = WorkTypeSerializer
    filterset_class = WorkTypeFilterSet


class TyPeriodViewSet(viewsets.ModelViewSet):
    queryset = TyPeriods.objects.all()
    serializer_class = TyperiodSerializer


class TprChapterViewSet(viewsets.ModelViewSet):
    queryset = TprChapters.objects.all()
    serializer_class = TprChapterSerializer
    filterset_class = TprChapterFilterSet


class GroupWorkViewSet(viewsets.ModelViewSet):
    queryset = GroupWorks.objects.all()
    serializer_class = GroupWorkSerializer    


class DgrPeriodsViewSet(viewsets.ModelViewSet):
    queryset = DgrPeriods.objects.all()
    serializer_class = DgrPeriodSerializer


class TimeRulesViewSet(viewsets.ModelViewSet):
    queryset = TimeRules.objects.all()
    serializer_class = TimeRuleSerializer


class TwForYearsViewSet(viewsets.ModelViewSet):
    queryset = TwForYears.objects.all()
    serializer_class = TwForYearSerializer


class TwBlocksViewSet(viewsets.ModelViewSet):
    queryset = TwBlocks.objects.all()
    serializer_class = TwBlockSerializer