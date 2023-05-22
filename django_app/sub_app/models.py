# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DgrPeriods(models.Model):
    dgp_id = models.AutoField(primary_key=True)
    tch_tch = models.ForeignKey('TprChapters', models.DO_NOTHING)
    ver_ver = models.ForeignKey('Versions', models.DO_NOTHING)
    sgr_sgr = models.ForeignKey('StuGroups', models.DO_NOTHING)
    typ_typ = models.ForeignKey('TyPeriods', models.DO_NOTHING)
    div_div = models.ForeignKey('Divisions', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'dgr_periods'
        unique_together = (('div_div', 'sgr_sgr', 'tch_tch', 'typ_typ', 'ver_ver'),)


class Disciplines(models.Model):
    dis_id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=500, db_comment='Название дисциплины')

    class Meta:
        managed = False
        db_table = 'disciplines'


class Divisions(models.Model):
    div_id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=500, db_comment='название подразделения')
    short = models.CharField(max_length=255)
    faculty = models.CharField(max_length=1, db_comment='является факультетом')
    chair = models.CharField(max_length=1, db_comment='является кафедрой')
    div_div = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'divisions'


class EduForms(models.Model):
    efo_id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=500, db_comment='Название формы обучения')
    short = models.CharField(unique=True, max_length=3, db_comment='Краткое обозначение')

    class Meta:
        managed = False
        db_table = 'edu_forms'


class EduLevels(models.Model):
    ele_id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=500, db_comment='Название')
    short = models.CharField(unique=True, max_length=5, blank=True, null=True, db_comment='Краткое обозначение')
    srt = models.IntegerField(blank=True, null=True, db_comment='Сортировка')

    class Meta:
        managed = False
        db_table = 'edu_levels'


class ExamType(models.Model):
    ext_id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=255, db_comment='название типа контроля (экзамен, зачёт)')
    short = models.CharField(unique=True, max_length=20, db_comment='краткое обозначение')

    class Meta:
        managed = False
        db_table = 'exam_type'


class GroupFaculties(models.Model):
    grf_id = models.AutoField(primary_key=True)
    stu_count = models.IntegerField(db_comment='Количество студентов')
    num_course = models.IntegerField(db_comment='Номер курса')
    ele_ele = models.ForeignKey(EduLevels, models.DO_NOTHING)
    efo_efo = models.ForeignKey(EduForms, models.DO_NOTHING)
    div_div = models.ForeignKey(Divisions, models.DO_NOTHING)
    sgr_sgr = models.ForeignKey('StuGroups', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'group_faculties'
        unique_together = (('ele_ele', 'efo_efo', 'sgr_sgr', 'div_div', 'num_course'),)


class GroupJoints(models.Model):
    grj_id = models.IntegerField(primary_key=True)
    sgr_sgr = models.ForeignKey('StuGroups', models.DO_NOTHING)
    ngr_ngr = models.ForeignKey('NrGroups', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'group_joints'
        unique_together = (('ngr_ngr', 'sgr_sgr'),)


class GroupWorks(models.Model):
    grw_id = models.AutoField(primary_key=True)
    sgr_sgr = models.ForeignKey('StuGroups', models.DO_NOTHING)
    wt_wot = models.ForeignKey('WorkTypes', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'group_works'
        unique_together = (('sgr_sgr', 'wt_wot'),)


class NrGroups(models.Model):
    ngr_id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'nr_groups'


class StuGroups(models.Model):
    sgr_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=500, db_comment='Имя группы')
    dgr_id = models.IntegerField(blank=True, null=True, db_comment='DIS_GROUPS из ЕТИС')
    info = models.CharField(max_length=1000, blank=True, null=True, db_comment='Комментарий')
    sgr_sgr = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stu_groups'


class TcTimes(models.Model):
    tim_id = models.AutoField(primary_key=True)
    val = models.IntegerField(db_comment='трудоёмкость (объём работы) в часах')
    ctl_count = models.IntegerField(db_comment='количество точек контроля')
    wt_wot = models.ForeignKey('WorkTypes', models.DO_NOTHING)
    tch_tch = models.ForeignKey('TprChapters', models.DO_NOTHING)
    totc_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tc_times'
        unique_together = (('wt_wot', 'tch_tch'),)


class TeachProgTypes(models.Model):
    tpt_id = models.IntegerField(primary_key=True)
    tp_type = models.CharField(max_length=255, db_comment='Тип учебной программы')
    type_info = models.CharField(max_length=240, blank=True, null=True, db_comment='Краткое описание')

    class Meta:
        managed = False
        db_table = 'teach_prog_types'


class TeachPrograms(models.Model):
    tpr_id = models.IntegerField(primary_key=True)
    confirm_date = models.DateField(blank=True, null=True, db_comment='дата утверждения')
    status = models.CharField(max_length=1, db_comment='статус программы дисциплины')
    protocol = models.CharField(max_length=255, blank=True, null=True, db_comment='номер протокола')
    practice_form = models.CharField(max_length=255, blank=True, null=True, db_comment='сопособ проведения практики (стационарная, выездная)')
    practice_schedule = models.CharField(max_length=25, blank=True, null=True, db_comment='вид проведения практики по отношению к графику (непрерывная, дискретная)')
    info = models.CharField(max_length=4000, blank=True, null=True, db_comment='предназначение')
    dis_dis = models.ForeignKey(Disciplines, models.DO_NOTHING)
    tpt_tpt = models.ForeignKey(TeachProgTypes, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'teach_programs'


class TeachYears(models.Model):
    ty_id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=255, db_comment='название (напр. "2002-2003")')
    start_date = models.DateField(unique=True, db_comment='дата начала учебного года')
    end_date = models.DateField(db_comment='дата оканчания учебного года')

    class Meta:
        managed = False
        db_table = 'teach_years'


class TimeRules(models.Model):
    tr_id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=1000, db_comment='Текстовая формулировка')
    info = models.CharField(max_length=1000, blank=True, null=True, db_comment='Примечания')
    value = models.IntegerField(db_comment='Значение нормы')
    degree = models.IntegerField(blank=True, null=True, db_comment='Порядок, степень 10, на который умножается VALUE')
    prorate_ctrl_cnt = models.CharField(max_length=1, db_comment='Пропорционально количеству точек контроля раздела')
    prorate_tc_val = models.CharField(max_length=1, db_comment='Пропорционально общей нагрузке отдела')
    prorate_tc_eval = models.CharField(max_length=1, db_comment='Пропорционально зачтенным часам')
    prorate_tc_aud = models.CharField(max_length=1, db_comment='Пропорционально аудиторной нагрузке раздела')
    prorate_st_cnt = models.CharField(max_length=1, db_comment='Пропорционально количеству судентов')
    norm_ctrl_cnt = models.CharField(max_length=1, db_comment='Нормировать к суммарному количеству точек контроля')
    norm_tpr_val = models.CharField(max_length=1, db_comment='Нормировать к суммарной нагрузке УМК')
    forward_aud_toe = models.CharField(max_length=1, db_comment='Отчетность в следующих по ауд нагрузке в семестрах')
    tgc_rec_cnt = models.IntegerField(blank=True, null=True, db_comment='Количество записей нормы при раздаче нагрузки')
    tr_tr_id = models.IntegerField(blank=True, null=True)
    tpt_tpt = models.ForeignKey(TeachProgTypes, models.DO_NOTHING, blank=True, null=True)
    ver_ver = models.ForeignKey('Versions', models.DO_NOTHING)
    ext_ext = models.ForeignKey(ExamType, models.DO_NOTHING, blank=True, null=True)
    twfy_twfy = models.ForeignKey('TwForYears', models.DO_NOTHING)
    wt_wot = models.ForeignKey('WorkTypes', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'time_rules'


class TpDeliveries(models.Model):
    tpdl_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    tpr_tpr = models.ForeignKey(TeachPrograms, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tp_deliveries'
        unique_together = (('name', 'tpr_tpr'),)


class TprChapters(models.Model):
    tch_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500, db_comment='Название раздела')
    srt = models.IntegerField(db_comment='Порядок сортировки')
    info = models.CharField(max_length=1000, blank=True, null=True, db_comment='Комментарий')
    ext_ext = models.ForeignKey(ExamType, models.DO_NOTHING, blank=True, null=True)
    tpdl_tpdl = models.ForeignKey(TpDeliveries, models.DO_NOTHING)
    tc_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tpr_chapters'


class TwBlocks(models.Model):
    twb_id = models.AutoField(primary_key=True)
    val = models.IntegerField(db_comment='размер работы в часах астрономические')
    conv_value = models.IntegerField(db_comment='размер в общепринятых часы')
    wt_wot = models.ForeignKey('WorkTypes', models.DO_NOTHING)
    dgp_dgp = models.ForeignKey(DgrPeriods, models.DO_NOTHING)
    wt_wot_id_initialized_by = models.ForeignKey('WorkTypes', models.DO_NOTHING, db_column='wt_wot_id_initialized_by', related_name='twblocks_wt_wot_id_initialized_by_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tw_blocks'
        unique_together = (('dgp_dgp', 'wt_wot', 'wt_wot_id_initialized_by'),)


class TwForYears(models.Model):
    twfy_id = models.AutoField(primary_key=True)
    ty_ty = models.ForeignKey(TeachYears, models.DO_NOTHING)
    wt_wot = models.ForeignKey('WorkTypes', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tw_for_years'


class TyPeriods(models.Model):
    typ_id = models.IntegerField(primary_key=True)
    num = models.IntegerField(db_comment='Номер триместра')
    start_date = models.DateField(blank=True, null=True, db_comment='Начало учебного периода по унифицированному графику')
    end_date = models.DateField(blank=True, null=True, db_comment='Конец учебного периода по унифицированному графику')
    period_type = models.CharField(max_length=255, db_comment='название учебного периода (триместр и семестр)')
    ty_ty = models.ForeignKey(TeachYears, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ty_periods'
        unique_together = (('ty_ty', 'num'),)


class Versions(models.Model):
    ver_id = models.AutoField(primary_key=True)
    calc_date = models.DateField(unique=True, db_comment='дата расчета')
    info = models.CharField(max_length=4000, blank=True, null=True, db_comment='описание')

    class Meta:
        managed = False
        db_table = 'versions'


class WorkTypes(models.Model):
    wot_id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=500, db_comment='Название')
    short = models.CharField(max_length=255, db_comment='Короткое название')
    aud = models.CharField(max_length=3, blank=True, null=True, db_comment='Включать в аудиторные часы?')
    include_in_tpd = models.CharField(max_length=3, blank=True, null=True, db_comment='доступен ли для включения в учебную программу?')
    oneday = models.CharField(max_length=1, db_comment='Вся работа в один день')
    srt = models.IntegerField(blank=True, null=True, db_comment='Порядок сортировки')

    class Meta:
        managed = False
        db_table = 'work_types'
