from rest_framework import viewsets

from sub_app.api.serializers import TimeRulesSerializer
from sub_app.api.serializers import TwForYearsSerializer
from sub_app.api.serializers import TwBlocksSerializer
from sub_app.api.serializers import DgrPeriodsSerializer

from sub_app.models import TimeRules
from sub_app.models import TwForYears
from sub_app.models import TwBlocks
from sub_app.models import DgrPeriods


class DgrPeriodsViewSet(viewsets.ModelViewSet):
    queryset = DgrPeriods.objects.all()
    serializer_class = DgrPeriodsSerializer


class TimeRulesViewSet(viewsets.ModelViewSet):
    queryset = TimeRules.objects.all()
    serializer_class = TimeRulesSerializer


class TwForYearsViewSet(viewsets.ModelViewSet):
    queryset = TwForYears.objects.all()
    serializer_class = TwForYearsSerializer


class TwBlocksViewSet(viewsets.ModelViewSet):
    queryset = TwBlocks.objects.all()
    serializer_class = TwBlocksSerializer