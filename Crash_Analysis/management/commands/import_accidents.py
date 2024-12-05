from django.core.management.base import BaseCommand, CommandError
from Crash_Analysis.models import Accident
import argparse
import pandas as pd
from django.contrib.gis.geos import Point


def return_datetime(row):
    try:
        return pd.to_datetime(
            f"{int(row['YEAR'])}-{int(row['MONTH']):02}-{int(row['DAY']):02} {int(row['HOUR']):02}:{int(row['MINUTE']):02}"
        )
    except pd._libs.tslibs.parsing.DateParseError:
        return pd.to_datetime(
            f"{int(row['YEAR'])}-{int(row['MONTH']):02}-{int(row['DAY']):02} 23:59:59" # the seconds place indicates invalid input
        )


class Command(BaseCommand):
    help = "Imports accident.sas7bdat files"

    def add_arguments(self, parser):
        parser.add_argument("accident_file", nargs="+", type=str)

    def handle(self, *args, **options):
        print("Importing " + options["accident_file"][0])
        # Read the SAS file into a pandas DataFrame
        df = pd.read_sas(options["accident_file"][0], format='sas7bdat')
        print(f"Columns in the file: {list(df.columns)}")
        # Iterate over each row and create Accident objects
        for _, row in df.iterrows():
            row['TWAY_ID'] = '' if pd.isna(row['TWAY_ID']) else bytes(row['TWAY_ID']).decode('utf-8')
            row['TWAY_ID2'] = '' if pd.isna(row['TWAY_ID2']) else bytes(row['TWAY_ID2']).decode('utf-8')
            row['RAIL'] = '' if pd.isna(row['RAIL']) else bytes(row['RAIL']).decode('utf-8')
            # with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
            #     print(row)
            a = Accident(
                state=row['STATE'],
                st_case=row['ST_CASE'],
                peds=row['PEDS'],
                pernotmvit=row['PERNOTMVIT'],
                ve_total=row['VE_TOTAL'],
                ve_forms=row['VE_FORMS'],
                pvh_invl=row['PVH_INVL'],
                persons=row['PERSONS'],
                permvit=row['PERMVIT'],
                county=row['COUNTY'],
                city=row['CITY'],
                datetime=return_datetime(row),
                tway_id=row['TWAY_ID'],
                tway_id2=row['TWAY_ID2'],
                route=row['ROUTE'],
                rur_urb=row['RUR_URB'],
                func_sys=row['FUNC_SYS'],
                rd_owner=row['RD_OWNER'],
                nhs=row['NHS'],
                sp_jur=row['SP_JUR'],
                milept=row['MILEPT'],
                # latitude=row['LATITUDE'],
                # longitud=row['LONGITUD'],
                location=Point(row['LONGITUD'], row['LATITUDE']),
                harm_ev=row['HARM_EV'],
                man_coll=row['MAN_COLL'],
                reljct1=row['RELJCT1'],
                reljct2=row['RELJCT2'],
                typ_int=row['TYP_INT'],
                rel_road=row['REL_ROAD'],
                wrk_zone=row['WRK_ZONE'],
                lgt_cond=row['LGT_COND'],
                weather=row['WEATHER'],
                sch_bus=row['SCH_BUS'],
                rail=row['RAIL'],
                not_hour=row['NOT_HOUR'],
                not_min=row['NOT_MIN'],
                # not_time=pd.to_datetime(
                #     f"{row['NOT_HOUR']:02}:{row['NOT_MIN']:02}"
                # ).time(),
                arr_hour=row['ARR_HOUR'],
                arr_min=row['ARR_MIN'],
                # arr_time=pd.to_datetime(
                #     f"{row['ARR_HOUR']:02}:{row['ARR_MIN']:02}"
                # ).time(),
                hosp_hr=row['HOSP_HR'],
                hosp_mn=row['HOSP_MN'],
                # hosp_time=pd.to_datetime(
                #     f"{row['HOSP_HR']:02}:{row['HOSP_MN']:02}"
                # ).time(),
                fatals=row['FATALS']
            )
            a.save()
            print(f"Added {int(row['ST_CASE'])}")
        print("Import completed successfully.")
