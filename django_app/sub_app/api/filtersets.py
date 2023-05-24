from django_filters import FilterSet, CharFilter

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


class StuGroupFilterSet(FilterSet):
    name__icontains = CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = StuGroups
        fields = "__all__"


class DivisionFilterSet(FilterSet):
    name__icontains = CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = Divisions
        fields = ["div_id", "name"] 


class TprChapterFilterSet(FilterSet):
    name__icontains = CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = TprChapters
        fields = ["tch_id", "name"] 


class WorkTypeFilterSet(FilterSet):
    name__icontains = CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = WorkTypes
        fields = ["wot_id", "name"] 