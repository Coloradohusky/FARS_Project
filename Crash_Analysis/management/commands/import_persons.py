from django.core.management.base import BaseCommand, CommandError
from Crash_Analysis.models import Accident, Vehicle, Person
import argparse
import pandas as pd
from django.contrib.gis.geos import Point


def return_datetime(row):
    try:
        return pd.to_datetime(
            f"{int(row['DEATH_YR'])}-{int(row['DEATH_MO']):02}-{int(row['DEATH_DA']):02} {int(row['DEATH_HR']):02}:{int(row['DEATH_MN']):02}"
        )
    except pd._libs.tslibs.parsing.DateParseError:
        return None


class Command(BaseCommand):
    help = "Imports person.sas7bdat files"

    def add_arguments(self, parser):
        parser.add_argument("person_file", nargs="+", type=str)
        parser.add_argument("year", nargs="+", type=int)

    def handle(self, *args, **options):
        print("Importing " + options["person_file"][0])
        # Read the SAS file into a pandas DataFrame
        df = pd.read_sas(options["person_file"][0], format='sas7bdat')
        print(f"Columns in the file: {list(df.columns)}")
        # Iterate over each row and create Accident objects
        for _, row in df.iterrows():
            try:
                accident = Accident.objects.get(st_case=int(row['ST_CASE']), datetime__year=options["year"][0])
            except Accident.DoesNotExist:
                print(f"No Accident found for st_case={int(row['ST_CASE'])}, year={options['year'][0]}")
                continue
            try:
                vehicle = Vehicle.objects.get(st_case__st_case=int(row['ST_CASE']), st_case__datetime__year=options["year"][0], veh_no=int(row["VEH_NO"]))
            except Vehicle.DoesNotExist:
                print(f"No Accident found for st_case={int(row['ST_CASE'])}, year={options['year'][0]}, veh_no={int(row['VEH_NO'])}")
                vehicle = None
            # with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
            #     print(row)
            p = Person(
                st_case=accident,
                veh_no=vehicle,
                age=row['AGE'],
                sex=row['SEX'],
                per_typ=row['PER_TYP'],
                inj_sev=row['INJ_SEV'],
                seat_pos=row['SEAT_POS'],
                rest_use=row['REST_USE'],
                rest_mis=row['REST_MIS'],
                helm_use=row['HELM_USE'],
                helm_mis=row['HELM_MIS'],
                air_bag=row['AIR_BAG'],
                ejection=row['EJECTION'],
                ej_path=row['EJ_PATH'],
                extricat=row['EXTRICAT'],
                drinking=row['DRINKING'],
                alc_status=row['ALC_STATUS'],
                atst_typ=row['ATST_TYP'],
                alc_res=row['ALC_RES'],
                drugs=row['DRUGS'],
                dstatus=row['DSTATUS'],
                hospital=row['HOSPITAL'],
                doa=row['DOA'],
                death_datetime=return_datetime(row),
                lag_hrs=row['LAG_HRS'],
                lag_mins=row['LAG_MINS'],
                str_veh=row['STR_VEH'],
                location=row['LOCATION'],
                work_inj=row['WORK_INJ'],
                hispanic=row['HISPANIC'],
                devtype=row['DEVTYPE'] if str(row['DEVTYPE']) != 'nan' else None,
                devmotor=row['DEVMOTOR'] if str(row['DEVMOTOR']) != 'nan' else None,
            )
            p.save()
            print(f"Added st_case={int(row['ST_CASE'])}, year={options['year'][0]}, veh_no={int(row['VEH_NO'])}")
        print("Import completed successfully.")
