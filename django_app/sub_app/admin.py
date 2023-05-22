from django.contrib import admin

# Register your models here.
from sub_app.models import TimeRules, TwForYears, TwBlocks, DgrPeriods


@admin.register(TimeRules)
class TimeRulesAdmin(admin.ModelAdmin):
    pass


@admin.register(TwForYears)
class TwForYearAdmin(admin.ModelAdmin):
    pass


@admin.register(TwBlocks)
class TwBlockAdmin(admin.ModelAdmin):
    pass


@admin.register(DgrPeriods)
class DgrPeriodsAdmin(admin.ModelAdmin):
    pass

