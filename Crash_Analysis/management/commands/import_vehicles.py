from django.core.management.base import BaseCommand, CommandError
from Crash_Analysis.models import Accident, Vehicle
import argparse
import pandas as pd
from django.contrib.gis.geos import Point



class Command(BaseCommand):
    help = "Imports vehicle.sas7bdat files"

    def add_arguments(self, parser):
        parser.add_argument("vehicle_file", nargs="+", type=str)
        parser.add_argument("year", nargs="+", type=int)

    def handle(self, *args, **options):
        print("Importing " + options["vehicle_file"][0])
        # Read the SAS file into a pandas DataFrame
        df = pd.read_sas(options["vehicle_file"][0], format='sas7bdat')
        print(f"Columns in the file: {list(df.columns)}")

        # Iterate over each row and create Accident objects
        for _, row in df.iterrows():
            # Find the matching Accident
            try:
                accident = Accident.objects.get(st_case=int(row['ST_CASE']), datetime__year=options["year"][0])
            except Accident.DoesNotExist:
                print(f"No Accident found for st_case={int(row['ST_CASE'])}, year={options['year'][0]}")
                continue
            # print(f"Adding {int(row['ST_CASE'])}")
            row['VIN'] = '' if pd.isna(row['VIN']) else bytes(row['VIN']).decode('utf-8')
            row['TRLR1VIN'] = '' if pd.isna(row['TRLR1VIN']) else bytes(row['TRLR1VIN']).decode('utf-8')
            row['TRLR2VIN'] = '' if pd.isna(row['TRLR2VIN']) else bytes(row['TRLR2VIN']).decode('utf-8')
            row['TRLR3VIN'] = '' if pd.isna(row['TRLR3VIN']) else bytes(row['TRLR3VIN']).decode('utf-8')
            row['MCARR_ID'] = '' if pd.isna(row['MCARR_ID']) else bytes(row['MCARR_ID']).decode('utf-8')
            # with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
            #     print(row)
            v = Vehicle(
                st_case=accident,
                veh_no=row['VEH_NO'],
                numoccs=row['NUMOCCS'],
                unittype=row['UNITTYPE'],
                hit_run=row['HIT_RUN'],
                reg_stat=row['REG_STAT'],
                owner=row['OWNER'],
                make=row['MAKE'],
                model=row['MODEL'],
                body_typ=row['BODY_TYP'],
                mod_year=row['MOD_YEAR'],
                vin=row['VIN'],
                tow_veh=row['TOW_VEH'],
                j_knife=row['J_KNIFE'],
                mcarr_id=row['MCARR_ID'],
                v_config=row['V_CONFIG'],
                cargo_bt=row['CARGO_BT'],
                haz_inv=row['HAZ_INV'],
                haz_plac=row['HAZ_PLAC'],
                haz_id=row['HAZ_ID'],
                haz_cno=row['HAZ_CNO'],
                haz_rel=row['HAZ_REL'],
                bus_use=row['BUS_USE'],
                spec_use=row['SPEC_USE'],
                emer_use=row['EMER_USE'],
                trav_sp=row['TRAV_SP'],
                underoverride=row['UNDEROVERRIDE'],
                rollover=row['ROLLOVER'],
                rolinloc=row['ROLINLOC'],
                impact1=row['IMPACT1'],
                deformed=row['DEFORMED'],
                towed=row['TOWED'],
                m_harm=row['M_HARM'],
                fire_exp=row['FIRE_EXP'],
                dr_pres=row['DR_PRES'],
                l_state=row['L_STATE'],
                dr_zip=row['DR_ZIP'],
                l_status=row['L_STATUS'],
                l_type=row['L_TYPE'],
                cdl_stat=row['CDL_STAT'],
                l_endors=row['L_ENDORS'],
                l_compl=row['L_COMPL'],
                l_restri=row['L_RESTRI'],
                dr_hgt=row['DR_HGT'],
                dr_wgt=row['DR_WGT'],
                prev_acc=row['PREV_ACC'],
                prev_sus1=row['PREV_SUS1'],
                prev_sus2=row['PREV_SUS2'],
                prev_sus3=row['PREV_SUS3'],
                prev_dwi=row['PREV_DWI'],
                prev_spd=row['PREV_SPD'],
                prev_oth=row['PREV_OTH'],
                first_mo=row['FIRST_MO'],
                first_yr=row['FIRST_YR'],
                last_mo=row['LAST_MO'],
                last_yr=row['LAST_YR'],
                speedrel=row['SPEEDREL'],
                vtrafway=row['VTRAFWAY'],
                vnum_lan=row['VNUM_LAN'],
                vspd_lim=row['VSPD_LIM'],
                valign=row['VALIGN'],
                vprofile=row['VPROFILE'],
                vpavetyp=row['VPAVETYP'],
                vsurcond=row['VSURCOND'],
                vtrafcon=row['VTRAFCON'],
                vtcont_f=row['VTCONT_F'],
                p_crash1=row['P_CRASH1'],
                p_crash2=row['P_CRASH2'],
                p_crash3=row['P_CRASH3'],
                pcrash4=row['PCRASH4'],
                pcrash5=row['PCRASH5'],
                acc_type=row['ACC_TYPE'],
                trlr1vin=row['TRLR1VIN'],
                trlr2vin=row['TRLR2VIN'],
                # trlr3vin=row['TRLR3VIN'],
                deaths=row['DEATHS'],
                dr_drink=row['DR_DRINK'],
                vpicmake=row['VPICMAKE'],
                vpicmodel=row['VPICMODEL'],
                vpicbodyclass=row['VPICBODYCLASS'],
                icfinalbody=row['ICFINALBODY'],
                gvwr_from=row['GVWR_FROM'],
                gvwr_to=row['GVWR_TO'],
                trlr1gvwr=row['TRLR1GVWR'],
                trlr2gvwr=row['TRLR2GVWR'],
                trlr3gvwr=row['TRLR3GVWR']
            )
            v.save()
            print(f"Added {int(row['ST_CASE'])}")
        print("Import completed successfully.")
