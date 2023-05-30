from django.urls import path, include

from rest_framework import routers
from sub_app.api.views import DgrPeriodsViewSet
from sub_app.api.views import TimeRulesViewSet
from sub_app.api.views import TwBlocksViewSet
from sub_app.api.views import TwForYearsViewSet
from sub_app.api.views import StuGroupViewSet
from sub_app.api.views import GroupWorkViewSet
from sub_app.api.views import DivisionViewSet
from sub_app.api.views import WorkTypeViewSet
from sub_app.api.views import TyPeriodViewSet
from sub_app.api.views import TprChapterViewSet
from sub_app.api.views import VersionViewSet



# api route
router = routers.DefaultRouter()
router.register(r'dgr_periods', DgrPeriodsViewSet,  basename='DgrPeriods')
router.register(r'time_rules', TimeRulesViewSet, basename='TimeRules')
router.register(r'tw_blocks', TwBlocksViewSet, basename='TwBlocks')
router.register(r'tw_for_years', TwForYearsViewSet, basename='TwForYears')
router.register(r'stu_groups', StuGroupViewSet, basename='StuGroups')
router.register(r'group_works', GroupWorkViewSet, basename='GroupWorks')
router.register(r'divisions', DivisionViewSet, basename='Divisions')
router.register(r'tpr_chapters', TprChapterViewSet, basename='TprChapters')
router.register(r'work_types', WorkTypeViewSet, basename='WorkTypes')
router.register(r'ty_periods', TyPeriodViewSet, basename='TyPeriods')
router.register(r'versions', VersionViewSet, basename='Versions')


urlpatterns = [
    path("api/", include(router.urls)),
]