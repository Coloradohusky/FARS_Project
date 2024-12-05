from django.contrib.gis.db import models

from .dicts import *

# Ensures that get_FOO_display always wraps the field in str()
# nvm this doesn't work
class CustomBaseModel(models.Model):
    class Meta:
        abstract = True
    def __getattr__(self, name):
        if name.startswith('get_') and name.endswith('_display'):
            field_name = name[4:-8]
            try:
                choices = self._meta.get_field(field_name).choices
                value = super().__getattr__(field_name)
                return dict(choices).get(str(value), "Unknown")
            except Exception:
                pass
        return super().__getattr__(name)


class Accident(CustomBaseModel):
    state = models.PositiveSmallIntegerField("State", choices=STATE)
    # state = models.PositiveSmallIntegerField()
    st_case = models.PositiveIntegerField("Case Number")
    peds = models.PositiveSmallIntegerField("Number of Forms Submitted for Persons Not in Motor Vehicles")
    pernotmvit = models.PositiveSmallIntegerField("Number of Persons Not in Motor Vehicles In-Transport")
    ve_total = models.PositiveSmallIntegerField("Number of Vehicle Forms Submitted - All")
    ve_forms = models.PositiveSmallIntegerField("Number of Motor Vehicles In-Transport")
    pvh_invl = models.PositiveSmallIntegerField("Number of Parked/Working Vehicles")
    persons = models.PositiveSmallIntegerField("Number of Person Forms Submitted")
    permvit = models.PositiveSmallIntegerField("Number of Persons in Motor Vehicles In-Transport")
    county = models.PositiveSmallIntegerField("County")
    city = models.PositiveSmallIntegerField("City")
    # month = models.PositiveSmallIntegerField()
    # day = models.PositiveSmallIntegerField()
    # day_week = models.PositiveSmallIntegerField()
    # year = models.PositiveSmallIntegerField()
    # hour = models.PositiveSmallIntegerField()
    # minute = models.PositiveSmallIntegerField()
    datetime = models.DateTimeField("Crash Date/Time (Local)")
    tway_id = models.CharField("Trafficway Identifier 1")
    tway_id2 = models.CharField("Trafficway Identifier 2")
    route = models.PositiveSmallIntegerField("Route Signing", choices=ROUTE)
    rur_urb = models.PositiveSmallIntegerField("Land Use", choices=RUR_URB)
    func_sys = models.PositiveSmallIntegerField("Functional System", choices=FUNC_SYS)
    rd_owner = models.PositiveSmallIntegerField("Ownership", choices=RD_OWNER)
    nhs = models.PositiveSmallIntegerField("National Highway System", choices=NHS)
    sp_jur = models.PositiveSmallIntegerField("Special Jurisdiction", choices=SP_JUR)
    milept = models.PositiveIntegerField("Milepoint")
    # latitude = models.FloatField()
    # longitud = models.FloatField()
    location = models.PointField("Global Position")
    harm_ev = models.PositiveSmallIntegerField("First Harmful Event", choices=HARM_EV[0][1]) # todo: change to reflect datetime.year
    man_coll = models.PositiveSmallIntegerField("Manner of Collision of the First Harmful Event", choices=MAN_COLL[0][1]) # todo: change to reflect datetime.year
    reljct1 = models.PositiveSmallIntegerField("Relation to Junction - Within Interchange Area", choices=RELJCT1[0][1]) # todo: change to reflect datetime.year
    reljct2 = models.PositiveSmallIntegerField("Relation to Junction - Specific Location", choices=RELJCT2[0][1]) # todo: change to reflect datetime.year
    typ_int = models.PositiveSmallIntegerField("Type of Intersection", choices=TYP_INT[0][1]) # todo: change to reflect datetime.year
    rel_road = models.PositiveSmallIntegerField("Relation to Trafficway", choices=REL_ROAD[0][1]) # todo: change to reflect datetime.year
    wrk_zone = models.PositiveSmallIntegerField("Work Zone", choices=WRK_ZONE[0][1]) # todo: change to reflect datetime.year
    lgt_cond = models.PositiveSmallIntegerField("Light Condition", choices=LGT_COND[0][1]) # todo: change to reflect datetime.year
    weather = models.PositiveSmallIntegerField("Atmospheric Conditions", choices=WEATHER[0][1]) # todo: change to reflect datetime.year
    sch_bus = models.PositiveSmallIntegerField("School Bus Related", choices=SCH_BUS)
    rail = models.CharField("Rail Grade Crossing Identifier")
    not_hour = models.PositiveSmallIntegerField("Hour of Notification")
    not_min = models.PositiveSmallIntegerField("Minute of Notification")
    not_time = models.TimeField("Notification Time EMS", null = True, blank = True)
    arr_hour = models.PositiveSmallIntegerField("Hour of Arrival at Scene")
    arr_min = models.PositiveSmallIntegerField("Minute of Arrival at Scene")
    arr_time = models.TimeField("Arrival Time EMS", null = True, blank = True)
    hosp_hr = models.PositiveSmallIntegerField("Hour of EMS Arrival at Hospital")
    hosp_mn = models.PositiveSmallIntegerField("Minute of EMS Arrival at Hospital")
    hosp_time = models.TimeField("EMS Time at Hospital", null = True, blank = True)
    fatals = models.PositiveSmallIntegerField("Fatalities")
    def get_absolute_url(self):
        return "/accidents/%i/%i/" % (self.datetime.year, self.st_case)

class Vehicle(CustomBaseModel):
    st_case = models.ForeignKey(
        Accident,
        verbose_name = "Case Number",
        on_delete = models.CASCADE
    )
    veh_no = models.PositiveSmallIntegerField("Vehicle Number")
    numoccs = models.PositiveSmallIntegerField("Number of Occupants") # 99 = unknown
    unittype = models.PositiveSmallIntegerField("Unit Type", choices=UNITTYPE)
    hit_run = models.PositiveSmallIntegerField("Hit-and-Run", choices=HIT_RUN)
    reg_stat = models.PositiveSmallIntegerField("Registration State", choices=REG_STAT)
    owner = models.PositiveSmallIntegerField("Registered Vehicle Owner", choices=OWNER)
    make = models.PositiveSmallIntegerField("NSCA Make", choices=MAKE)
    model = models.PositiveSmallIntegerField("NSCA Model") # todo
    # mak_mod = models.PositiveIntegerField()
    body_typ = models.PositiveSmallIntegerField("NSCA Body Type", choices=BODY_TYP[0][1])
    mod_year = models.PositiveSmallIntegerField("Vehicle Model Year")
    vin = models.CharField("Vehicle Identification Number")
    tow_veh = models.PositiveSmallIntegerField("Vehicle Trailing", choices=TOW_VEH[0][1])
    j_knife = models.PositiveSmallIntegerField("Jackknife", choices=J_KNIFE)
    # mcarr_i1 = models.PositiveSmallIntegerField()
    # mcarr_i2 = models.PositiveIntegerField()
    mcarr_id = models.CharField("Motor Carrier Identification Number")
    v_config = models.PositiveSmallIntegerField("Vehicle Configuration", choices=V_CONFIG)
    cargo_bt = models.PositiveSmallIntegerField("Cargo Body Type", choices=CARGO_BT)
    haz_inv = models.PositiveSmallIntegerField("Hazardous Material Involvement", choices=HAZ_INV)
    haz_plac = models.PositiveSmallIntegerField("Hazardous Material Placard", choices=HAZ_PLAC)
    haz_id = models.PositiveSmallIntegerField()
    haz_cno = models.PositiveSmallIntegerField()
    haz_rel = models.PositiveSmallIntegerField()
    bus_use = models.PositiveSmallIntegerField()
    spec_use = models.PositiveSmallIntegerField()
    emer_use = models.PositiveSmallIntegerField()
    trav_sp = models.PositiveSmallIntegerField()
    underoverride = models.PositiveSmallIntegerField()
    rollover = models.PositiveSmallIntegerField()
    rolinloc = models.PositiveSmallIntegerField()
    impact1 = models.PositiveSmallIntegerField()
    deformed = models.PositiveSmallIntegerField()
    towed = models.PositiveSmallIntegerField()
    m_harm = models.PositiveSmallIntegerField()
    fire_exp = models.PositiveSmallIntegerField()
    dr_pres = models.PositiveSmallIntegerField()
    l_state = models.PositiveSmallIntegerField()
    dr_zip = models.PositiveIntegerField()
    l_status = models.PositiveSmallIntegerField()
    l_type = models.PositiveSmallIntegerField()
    cdl_stat = models.PositiveSmallIntegerField()
    l_endors = models.PositiveSmallIntegerField()
    l_compl = models.PositiveSmallIntegerField()
    l_restri = models.PositiveSmallIntegerField()
    dr_hgt = models.PositiveSmallIntegerField()
    dr_wgt = models.PositiveSmallIntegerField()
    prev_acc = models.PositiveSmallIntegerField()
    prev_sus1 = models.PositiveSmallIntegerField()
    prev_sus2 = models.PositiveSmallIntegerField()
    prev_sus3 = models.PositiveSmallIntegerField()
    prev_dwi = models.PositiveSmallIntegerField()
    prev_spd = models.PositiveSmallIntegerField()
    prev_oth = models.PositiveSmallIntegerField()
    first_mo = models.PositiveSmallIntegerField()
    first_yr = models.PositiveSmallIntegerField()
    last_mo = models.PositiveSmallIntegerField()
    last_yr = models.PositiveSmallIntegerField()
    speedrel = models.PositiveSmallIntegerField()
    vtrafway = models.PositiveSmallIntegerField()
    vnum_lan = models.PositiveSmallIntegerField()
    vspd_lim = models.PositiveSmallIntegerField()
    valign = models.PositiveSmallIntegerField()
    vprofile = models.PositiveSmallIntegerField()
    vpavetyp = models.PositiveSmallIntegerField()
    vsurcond = models.PositiveSmallIntegerField()
    vtrafcon = models.PositiveSmallIntegerField()
    vtcont_f = models.PositiveSmallIntegerField()
    p_crash1 = models.PositiveSmallIntegerField()
    p_crash2 = models.PositiveSmallIntegerField()
    p_crash3 = models.PositiveSmallIntegerField()
    pcrash4 = models.PositiveSmallIntegerField()
    pcrash5 = models.PositiveSmallIntegerField()
    acc_type = models.PositiveSmallIntegerField()
    trlr1vin = models.CharField()
    trlr2vin = models.CharField()
    trlr3vin = models.CharField()
    deaths = models.PositiveSmallIntegerField()
    dr_drink = models.PositiveSmallIntegerField()
    vpicmake = models.PositiveIntegerField("vPIC Model")
    vpicmodel = models.PositiveIntegerField("vPIC Make")
    vpicbodyclass = models.PositiveSmallIntegerField("vPIC Body Class", choices=VPICBODYCLASS)
    icfinalbody = models.PositiveSmallIntegerField("Final Stage Body Class", choices=ICFINALBODY)
    gvwr_from = models.PositiveSmallIntegerField("Power Unit Gross Vehicle Weight Rating - Lowest", choices=GVWR)
    gvwr_to = models.PositiveSmallIntegerField("Power Unit Gross Vehicle Weight Rating - Highest", choices=GVWR)
    trlr1gvwr = models.PositiveSmallIntegerField("Trailer Gross Vehicle Weight Rating 1", choices=GVWR)
    trlr2gvwr = models.PositiveSmallIntegerField("Trailer Gross Vehicle Weight Rating 2", choices=GVWR)
    trlr3gvwr = models.PositiveSmallIntegerField("Trailer Gross Vehicle Weight Rating 3", choices=GVWR)
    def get_make_display(self):
        return dict(MAKE).get(str(self.make), self.make)

class Person(CustomBaseModel):
    st_case = models.ForeignKey(
        Accident,
        verbose_name = "Case Number",
        on_delete = models.CASCADE
    )
    veh_no = models.ForeignKey(
        Vehicle,
        verbose_name = "Vehicle",
        on_delete = models.CASCADE,
        blank=True,
        null=True,
    )
    age = models.PositiveSmallIntegerField("Age")
    sex = models.PositiveSmallIntegerField("Sex/Gender", choices=SEX)
    per_typ = models.PositiveSmallIntegerField("Person Type", choices=PER_TYP[0][1])
    inj_sev = models.PositiveSmallIntegerField("Injury Severity", choices=INJ_SEV[0][1])
    seat_pos = models.PositiveSmallIntegerField("Seating Position", choices=SEAT_POS)
    rest_use = models.PositiveSmallIntegerField("Restraint System Use", choices=REST_USE[0][1])
    rest_mis = models.PositiveSmallIntegerField()
    helm_use = models.PositiveSmallIntegerField()
    helm_mis = models.PositiveSmallIntegerField()
    air_bag = models.PositiveSmallIntegerField()
    ejection = models.PositiveSmallIntegerField()
    ej_path = models.PositiveSmallIntegerField()
    extricat = models.PositiveSmallIntegerField()
    drinking = models.PositiveSmallIntegerField()
    alc_status = models.PositiveSmallIntegerField()
    atst_typ = models.PositiveSmallIntegerField()
    alc_res = models.PositiveSmallIntegerField()
    drugs = models.PositiveSmallIntegerField()
    dstatus = models.PositiveSmallIntegerField()
    hospital = models.PositiveSmallIntegerField(choices=HOSPITAL)
    doa = models.PositiveSmallIntegerField()
    death_datetime = models.DateTimeField(null = True, blank=True)
    lag_hrs = models.PositiveSmallIntegerField()
    lag_mins = models.PositiveSmallIntegerField()
    str_veh = models.PositiveSmallIntegerField()
    location = models.PositiveSmallIntegerField()
    work_inj = models.PositiveSmallIntegerField()
    hispanic = models.PositiveSmallIntegerField()
    devtype = models.PositiveSmallIntegerField(null = True, blank=True)
    devmotor = models.PositiveSmallIntegerField(null = True, blank=True)
    def get_sex_display(self):
        return dict(SEX).get(str(self.sex), self.sex)
    def get_per_typ_display(self):
        return dict(PER_TYP[0][1]).get(str(self.per_typ), self.per_typ)
    def get_inj_sev_display(self):
        return dict(INJ_SEV[0][1]).get(str(self.inj_sev), self.inj_sev)

