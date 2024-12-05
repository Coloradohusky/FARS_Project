STATE = [
    ("1", "Alabama"),
    ("2", "Alaska"),
    ("4", "Arizona"),
    ("5", "Arkansas"),
    ("6", "California"),
    ("8", "Colorado"),
    ("9", "Connecticut"),
    ("10", "Delaware"),
    ("11", "District of Columbia"),
    ("12", "Florida"),
    ("13", "Georgia"),
    ("15", "Hawaii"),
    ("16", "Idaho"),
    ("17", "Illinois"),
    ("18", "Indiana"),
    ("19", "Iowa"),
    ("20", "Kansas"),
    ("21", "Kentucky"),
    ("22", "Louisiana"),
    ("23", "Maine"),
    ("24", "Maryland"),
    ("25", "Massachusetts"),
    ("26", "Michigan"),
    ("27", "Minnesota"),
    ("28", "Mississippi"),
    ("29", "Missouri"),
    ("30", "Montana"),
    ("31", "Nebraska"),
    ("32", "Nevada"),
    ("33", "New Hampshire"),
    ("34", "New Jersey"),
    ("35", "New Mexico"),
    ("36", "New York"),
    ("37", "North Carolina"),
    ("38", "North Dakota"),
    ("39", "Ohio"),
    ("40", "Oklahoma"),
    ("41", "Oregon"),
    ("42", "Pennsylvania"),
    ("43", "Puerto Rico"),
    ("44", "Rhode Island"),
    ("45", "South Carolina"),
    ("46", "South Dakota"),
    ("47", "Tennessee"),
    ("48", "Texas"),
    ("49", "Utah"),
    ("50", "Vermont"),
    ("51", "Virginia"),
    ("52", "Virgin Islands"),
    ("53", "Washington"),
    ("54", "West Virginia"),
    ("55", "Wisconsin"),
    ("56", "Wyoming"),
]


def GET_STATE():
    return STATE


# with open(
#     ("gsa_codes_nov2024.csv"
# ) as file:
#     COUNTY = []
#     for line in file.readlines():
#         line = line.replace("\n"), "")
#         line = line.split("),")
#         if line[0] not in COUNTY:
#             COUNTY[line[0]] = []
#         COUNTY[line[0]][line[1]] = line[2]


# def GET_COUNTY():
#     return COUNTY


# with open(
#     ("C:/Users/Riley/Desktop/websiteThing/python map scripts/gsa_codes.txt"
# ) as file:
#     CITY = []
#     for line in file.readlines():
#         line = line.replace("\n"), "")
#         line = line.split("),")
#         if line[0] not in CITY:
#             CITY[line[0]] = []
#         CITY[line[0]][line[1]] = line[2]


# def GET_CITY():
#     return CITY


MONTH = [
    ("1", "January"),
    ("2", "February"),
    ("3", "March"),
    ("4", "April"),
    ("5", "May"),
    ("6", "June"),
    ("7", "July"),
    ("8", "August"),
    ("9", "September"),
    ("10", "October"),
    ("11", "November"),
    ("12", "December"),
]


def GET_MONTH():
    return MONTH


HARM_EV = [
    ("2018-Later", [
        ("1", "Rollover/Overturn"),
        ("2", "Fire/Explosion"),
        ("3", "Immersion"),
        ("4", "Gas Inhalation"),
        ("5", "Fell/Jumped from Vehicle"),
        ("6", "Injured in Vehicle (Non-Collision)"),
        ("7", "Other Non-Collision"),
        ("8", "Pedestrian"),
        ("9", "Pedalcyclist"),
        ("10", "Railway Vehicle"),
        ("11", "Live Animal"),
        ("12", "Motor Vehicle in Transport"),
        ("14", "Parked Motor Vehicle (Not in Transport)"),
        ("15", "Non-Motorist on Personal Conveyance"),
        ("16", "Thrown or Falling Object"),
        ("17", "Boulder"),
        ("18", "Other Object (Not Fixed)"),
        ("19", "Building"),
        ("20", "Impact Attenuator/Crash Cushion"),
        ("21", "Bridge Pier or Support"),
        ("23", "Bridge Rail (Includes Parapet)"),
        ("24", "Guardrail Face"),
        ("25", "Concrete Traffic Barrier"),
        ("26", "Other Traffic Barrier"),
        ("30", "Utility Pole/Light Support"),
        ("31", "Post, Pole, or Other Supports"),
        ("32", "Culvert"),
        ("33", "Curb"),
        ("34", "Ditch"),
        ("35", "Embankment"),
        ("38", "Fence"),
        ("39", "Wall"),
        ("40", "Fire Hydrant"),
        ("41", "Shrubbery"),
        ("42", "Tree (Standing Only)"),
        ("43", "Other Fixed Object"),
        ("44", "Pavement Surface Irregularity (Ruts, Potholes, Grates, etc.)"),
        ("45", "Working Motor Vehicle"),
        ("46", "Traffic Signal Support"),
        ("48", "Snow Bank"),
        ("49", "Ridden Animal or Animal-Drawn Conveyance"),
        ("50", "Bridge Overhead Structure"),
        ("51", "Jackknife (Harmful to This Vehicle)"),
        ("52", "Guardrail End"),
        ("53", "Mail Box"),
        ("54", "Motor Vehicle In-Transport Strikes or is Struck by Cargo, Persons or Objects Set-in-Motion from/by Another Motor Vehicle In-Transport"),
        ("55", "Motor Vehicle in Motion Outside the Trafficway"),
        ("57", "Cable Barrier"),
        ("58", "Ground"),
        ("59", "Traffic Sign Support"),
        ("72", "Cargo/Equipment Loss or Shift (Harmful)"),
        ("73", "Object That Had Fallen From Motor Vehicle In-Transport"),
        ("74", "Road Vehicle on Rails"),
        ("91", "Unknown Object Not Fixed"),
        ("93", "Unknown Fixed Object"),
        ("99", "Reported as Unknown"),
    ]),
    ("2017", [
        ("1", "Rollover/Overturn"),
        ("2", "Fire/Explosion"),
        ("3", "Immersion"),
        ("4", "Gas Inhalation"),
        ("5", "Fell/Jumped from Vehicle"),
        ("6", "Injured in Vehicle (Non-Collision)"),
        ("7", "Other Non-Collision"),
        ("8", "Pedestrian"),
        ("9", "Pedalcyclist"),
        ("10", "Railway Vehicle"),
        ("11", "Live Animal"),
        ("12", "Motor Vehicle in Transport"),
        ("14", "Parked Motor Vehicle (Not in Transport)"),
        ("15", "Non-Motorist on Personal Conveyance"),
        ("16", "Thrown or Falling Object"),
        ("17", "Boulder"),
        ("18", "Other Object (Not Fixed)"),
        ("19", "Building"),
        ("20", "Impact Attenuator/Crash Cushion"),
        ("21", "Bridge Pier or Support"),
        ("23", "Bridge Rail (Includes Parapet)"),
        ("24", "Guardrail Face"),
        ("25", "Concrete Traffic Barrier"),
        ("26", "Other Traffic Barrier"),
        ("30", "Utility Pole/Light Support"),
        ("31", "Post, Pole, or Other Supports"),
        ("32", "Culvert"),
        ("33", "Curb"),
        ("34", "Ditch"),
        ("35", "Embankment"),
        ("38", "Fence"),
        ("39", "Wall"),
        ("40", "Fire Hydrant"),
        ("41", "Shrubbery"),
        ("42", "Tree (Standing Only)"),
        ("43", "Other Fixed Object"),
        ("44", "Pavement Surface Irregularity (Ruts, Potholes, Grates, etc.)"),
        ("45", "Working Motor Vehicle"),
        ("46", "Traffic Signal Support"),
        ("48", "Snow Bank"),
        ("49", "Ridden Animal or Animal-Drawn Conveyance"),
        ("50", "Bridge Overhead Structure"),
        ("51", "Jackknife (Harmful to This Vehicle)"),
        ("52", "Guardrail End"),
        ("53", "Mail Box"),
        ("54", "Motor Vehicle In-Transport Strikes or is Struck by Cargo, Persons or Objects Set-in-Motion from/by Another Motor Vehicle In-Transport"),
        ("55", "Motor Vehicle in Motion Outside the Trafficway"),
        ("57", "Cable Barrier"),
        ("58", "Ground"),
        ("59", "Traffic Sign Support"),
        ("72", "Cargo/Equipment Loss or Shift (Harmful to This Vehicle)"),
        ("73", "Object That Had Fallen From Motor Vehicle In-Transport"),
        ("74", "Road Vehicle on Rails"),
        ("91", "Unknown Object Not Fixed"),
        ("93", "Unknown Fixed Object"),
        ("99", "Unknown"),
    ]),
    ("2016", [
        ("1", "Rollover/Overturn"),
        ("2", "Fire/Explosion"),
        ("3", "Immersion"),
        ("4", "Gas Inhalation"),
        ("5", "Fell/Jumped from Vehicle"),
        ("6", "Injured in Vehicle (Non-Collision)"),
        ("7", "Other Non-Collision"),
        ("8", "Pedestrian"),
        ("9", "Pedalcyclist"),
        ("10", "Railway Vehicle"),
        ("11", "Live Animal"),
        ("12", "Motor Vehicle in Transport"),
        ("14", "Parked Motor Vehicle (Not in Transport)"),
        ("15", "Non-Motorist on Personal Conveyance"),
        ("16", "Thrown or Falling Object"),
        ("17", "Boulder"),
        ("18", "Other Object (Not Fixed)"),
        ("19", "Building"),
        ("20", "Impact Attenuator/Crash Cushion"),
        ("21", "Bridge Pier or Support"),
        ("23", "Bridge Rail (Includes Parapet)"),
        ("24", "Guardrail Face"),
        ("25", "Concrete Traffic Barrier"),
        ("26", "Other Traffic Barrier"),
        ("30", "Utility Pole/Light Support"),
        ("31", "Post, Pole, or Other Supports"),
        ("32", "Culvert"),
        ("33", "Curb"),
        ("34", "Ditch"),
        ("35", "Embankment"),
        ("38", "Fence"),
        ("39", "Wall"),
        ("40", "Fire Hydrant"),
        ("41", "Shrubbery"),
        ("42", "Tree (Standing Only)"),
        ("43", "Other Fixed Object"),
        ("44", "Pavement Surface Irregularity (Ruts, Potholes, Grates, etc.)"),
        ("45", "Working Motor Vehicle"),
        ("46", "Traffic Signal Support"),
        ("48", "Snow Bank"),
        ("49", "Ridden Animal or Animal-Drawn Conveyance"),
        ("50", "Bridge Overhead Structure"),
        ("51", "Jackknife (Harmful to This Vehicle)"),
        ("52", "Guardrail End"),
        ("53", "Mail Box"),
        ("54", "Motor Vehicle In-Transport Strikes or is Struck by Cargo, Persons or Objects Set-in-Motion from/by Another Motor Vehicle In-Transport"),
        ("55", "Motor Vehicle in Motion Outside the Trafficway"),
        ("57", "Cable Barrier"),
        ("58", "Ground"),
        ("59", "Traffic Sign Support"),
        ("72", "Cargo/Equipment Loss or Shift (Harmful to This Vehicle)"),
        ("73", "Object That Had Fallen From Motor Vehicle In-Transport"),
        ("74", "Road Vehicle on Rails"),
        ("99", "Unknown"),
    ]),
    ("2010-2015", [
        ("1", "Rollover/Overturn"),
        ("2", "Fire/Explosion"),
        ("3", "Immersion"),
        ("4", "Gas Inhalation"),
        ("5", "Fell/Jumped from Vehicle"),
        ("6", "Injured in Vehicle (Non-Collision)"),
        ("7", "Other Non-Collision"),
        ("8", "Pedestrian"),
        ("9", "Pedalcyclist"),
        ("10", "Railway Vehicle"),
        ("11", "Live Animal"),
        ("12", "Motor Vehicle in Transport"),
        ("14", "Parked Motor Vehicle (Not in Transport)"),
        ("15", "Non-Motorist on Personal Conveyance"),
        ("16", "Thrown or Falling Object"),
        ("17", "Boulder"),
        ("18", "Other Object (Not Fixed)"),
        ("19", "Building"),
        ("20", "Impact Attenuator/Crash Cushion"),
        ("21", "Bridge Pier or Support"),
        ("23", "Bridge Rail (Includes Parapet)"),
        ("24", "Guardrail Face"),
        ("25", "Concrete Traffic Barrier"),
        ("26", "Other Traffic Barrier"),
        ("30", "Utility Pole/Light Support"),
        ("31", "Other Post, Other Pole, or Other Supports"),
        ("32", "Culvert"),
        ("33", "Curb"),
        ("34", "Ditch"),
        ("35", "Embankment"),
        ("38", "Fence"),
        ("39", "Wall"),
        ("40", "Fire Hydrant"),
        ("41", "Shrubbery"),
        ("42", "Tree (Standing Only)"),
        ("43", "Other Fixed Object"),
        ("44", "Pavement Surface Irregularity (Ruts, Potholes, Grates, etc.)"),
        ("45", "Working Motor Vehicle"),
        ("46", "Traffic Signal Support"),
        ("48", "Snow Bank"),
        ("49", "Ridden Animal or Animal-Drawn Conveyance"),
        ("50", "Bridge Overhead Structure"),
        ("51", "Jackknife (Harmful to This Vehicle)"),
        ("52", "Guardrail End"),
        ("53", "Mail Box"),
        ("54", "Motor Vehicle In-Transport Strikes or is Struck by Cargo, Persons or Objects Set-in-Motion from/by Another Motor Vehicle In-Transport"),
        ("55", "Motor Vehicle in Motion Outside the Trafficway"),
        ("57", "Cable Barrier"),
        ("58", "Ground"),
        ("59", "Traffic Sign Support"),
        ("72", "Cargo/Equipment Loss or Shift (Harmful to This Vehicle)"),
        ("73", "Object Fell From Motor Vehicle In-Transport"),
        ("98", "Not Reported"),
        ("99", "Unknown"),
    ]),
    ("2004-2009", [
        ("1", "Rollover/Overturn"),
        ("2", "Fire/Explosion"),
        ("3", "Immersion"),
        ("4", "Gas Inhalation"),
        ("5", "Fell/Jumped from Vehicle"),
        ("6", "Injured in Vehicle"),
        ("7", "Other Non-Collision"),
        ("8", "Pedestrian"),
        ("9", "Pedalcycle"),
        ("10", "Railway Train"),
        ("11", "Animal"),
        ("12", "Motor Vehicle in Transport on Same Roadway"),
        ("13", "Motor Vehicle in Transport on Other Roadway"),
        ("14", "Parked Motor Vehicle (Not in Transport)"),
        ("15", "Non-Motorist on Personal Conveyance"),
        ("16", "Thrown or Falling Object"),
        ("17", "Boulder"),
        ("18", "Other Object (Not Fixed)"),
        ("19", "Building"),
        ("20", "Impact Attenuator/Crash Cushion"),
        ("21", "Bridge Pier or Abutment"),
        ("22", "Bridge Parapet End"),
        ("23", "Bridge Rail"),
        ("24", "Guardrail Face"),
        ("25", "Concrete Traffic Barrier"),
        ("26", "Other Traffic Barrier"),
        ("27", "Highway/Traffic Sign Post"),
        ("28", "Overhead Sign Support/Sign"),
        ("29", "Luminary/Light Support"),
        ("30", "Utility Pole"),
        ("31", "Other Post, Other Pole, or Other Supports"),
        ("32", "Culvert"),
        ("33", "Curb"),
        ("34", "Ditch"),
        ("35", "Embankment - Earth"),
        ("36", "Embankment - Rock, Stone, or Concrete"),
        ("37", "Embankment - Material Type Unknown"),
        ("38", "Fence"),
        ("39", "Wall"),
        ("40", "Fire Hydrant"),
        ("41", "Shrubbery"),
        ("42", "Tree (Standing Only)"),
        ("43", "Other Fixed Object"),
        ("44", "Pavement Surface Irregularity"),
        ("45", "Working Construction, Maintenance, or Utility Vehicles"),
        ("46", "Traffic Signal Support"),
        ("47", "Vehicle Occupant Struck or Run Over by Own Vehicle"),
        ("48", "Collision with Snow Bank"),
        ("49", "Ridden Animal or Animal-Drawn Conveyance"),
        ("50", "Bridge Overhead Structure"),
        ("51", "Jackknife"),
        ("52", "Guardrail End"),
        ("53", "Mail Box"),
        ("54", "Motor Vehicle Struck by Falling/Shifting Cargo or Anything Set in Motion by Another Motor Vehicle in Transport"),
        ("55", "Motor Vehicle in Motion Outside the Trafficway"),
        ("57", "Cable Barrier"),
        ("99", "Unknown"),
    ])
]

HARM_EV_IDS = [
    ("2018", "2018-Later"),
    ("2017", "2017"),
    ("2016", "2016"),
    ("2015", "2010-2015"),
    ("2014", "2010-2015"),
    ("2013", "2010-2015"),
    ("2012", "2010-2015"),
    ("2011", "2010-2015"),
    ("2010", "2010-2015"),
    ("2009", "2004-2009"),
    ("2008", "2004-2009"),
    ("2007", "2004-2009"),
    ("2006", "2004-2009"),
    ("2005", "2004-2009"),
    ("2004", "2004-2009"),
]


def GET_HARM_EV():
    return HARM_EV


def GET_HARM_EV_IDS():
    return HARM_EV_IDS


MAN_COLL = [
    ("2019-Later", [
        ("0", "First Harmful Event was Not a Collision with Motor Vehicle In-Transport"),
        ("1", "Front-to-Rear"),
        ("2", "Front-to-Front"),
        ("6", "Angle"),
        ("7", "Sideswipe - Same Direction"),
        ("8", "Sideswipe - Opposite Direction"),
        ("9", "Rear-to-Side"),
        ("10", "Rear-to-Rear"),
        ("11", "Other (End-Swipes and Others)"),
        ("98", "Not Reported"),
        ("99", "Reported as Unknown"),
    ]),
    ("2018", [
        ("0", "Not Collision with Motor Vehicle in Transport"),
        ("1", "Front-to-Rear"),
        ("2", "Front-to-Front"),
        ("6", "Angle"),
        ("7", "Sideswipe - Same Direction"),
        ("8", "Sideswipe - Opposite Direction"),
        ("9", "Rear-to-Side"),
        ("10", "Rear-to-Rear"),
        ("11", "Other (End-Swipes and Others)"),
        ("98", "Not Reported"),
        ("99", "Reported as Unknown"),
    ]),
    ("2010-2017", [
        ("0", "Not Collision with Motor Vehicle in Transport"),
        ("1", "Front-to-Rear"),
        ("2", "Front-to-Front"),
        ("6", "Angle"),
        ("7", "Sideswipe - Same Direction"),
        ("8", "Sideswipe - Opposite Direction"),
        ("9", "Rear-to-Side"),
        ("10", "Rear-to-Rear"),
        ("11", "Other (End-Swipes and Others)"),
        ("98", "Not Reported"),
        ("99", "Unknown"),
    ]),
    ("2002-2009", [
        ("0", "Not Collision with Motor Vehicle in Transport"),
        ("1", "Front-to-Rear"),
        ("2", "Front-to-Front"),
        ("3", "Angle - Front-to-Side, Same Direction"),
        ("4", "Angle - Front-to-Side, Opposite Direction"),
        ("5", "Angle - Front-to-Side, Right Angle (Includes Broadside)"),
        ("6", "Angle – Front-to-Side/Angle-Direction Not Specified"),
        ("7", "Sideswipe - Same Direction"),
        ("8", "Sideswipe - Opposite Direction"),
        ("9", "Rear-to-Side"),
        ("10", "Rear-to-Rear"),
        ("11", "Other (End-Swipes and Others)"),
        ("98", "Not Reported"),
        ("99", "Unknown"),
    ]),
]
MAN_COLL_IDS = [
    ("2018", "2018"),
    ("2017", "2010-2017"),
    ("2016", "2010-2017"),
    ("2015", "2010-2017"),
    ("2014", "2010-2017"),
    ("2013", "2010-2017"),
    ("2012", "2010-2017"),
    ("2011", "2010-2017"),
    ("2010", "2010-2017"),
    ("2009", "2002-2009"),
    ("2008", "2002-2009"),
    ("2007", "2002-2009"),
    ("2006", "2002-2009"),
    ("2005", "2002-2009"),
    ("2004", "2002-2009"),
    ("2003", "2002-2009"),
    ("2002", "2002-2009"),
]
FUNC_SYS = [
    ("1", "Interstate"),
    ("2", "Principal Arterial - Other Freeways and Expressways"),
    ("3", "Principal Arterial - Other"),
    ("4", "Minor Arterial"),
    ("5", "Major Collector"),
    ("6", "Minor Collector"),
    ("7", "Local"),
    ("96", "Trafficway Not in State Inventory"),
    ("98", "Not Reported"),
    ("99", "Unknown"),
]


def GET_FUNC_SYS():
    return FUNC_SYS


RUR_URB = [
    ("1", "Rural"),
    ("2", "Urban"),
    ("6", "Trafficway Not in State Inventory"),
    ("8", "Not Reported"),
    ("9", "Unknown"),
]


def GET_RUR_URB():
    return RUR_URB


BODY_TYP = [
    ("2020-Later", [
        ("1", "Convertible"),
        ("2", "2-Door Sedan/Hardtop/Coupe"),
        ("3", "3-Door/2-Door Hatchback"),
        ("4", "4-Door Sedan/Hardtop"),
        ("5", "5-Door/4-Door Hatchback"),
        ("6", "Station Wagon"),
        ("7", "Hacthback, Number of Doors Unknown"),
        ("8", "Sedan/Hardtop, Number of Doors Unknown"),
        ("9", "Other or Unknown Automobile Type"),
        ("10", "Auto-Based Pickup"),
        ("11", "Auto-Based Panel"),
        ("12", "Large Limousine - More Than Four Side Doors or Stretch Chassis"),
        ("13", "Three-Wheel Automobile or Automobile Derivative"),
        ("14", "Compact Utility"),
        ("15", "Large Utility"),
        ("16", "Utility Station Wagon"),
        ("17", "3-Door Coupe"),
        ("19", "Utility Unknown Body"),
        ("20", "Minivan"),
        ("21", "Large Van - Includes Van-Based Buses"),
        ("22", "Step Van or Walk-In Van"),
        ("28", "Other Van Type"),
        ("29", "Unknown Van Type"),
        ("33", "Convertible Pickup"),
        ("34", "Light Pickup"),
        ("39", "Unknown Light Conventional Truck Type"),
        ("40", "Cab Chassis-Based"),
        ("41", "Truck-Based Panel"),
        ("42", "Light Vehicle-Based Motorhome (Chassis Mounted)"),
        ("45", "Other Light Conventional Truck Type"),
        ("48", "Unknown Light Truck Type"),
        ("49", "Unknown Light-Vehicle Type"),
        ("50", "School Bus"),
        ("51", "Cross-Country/Intercity Bus"),
        ("52", "Transit Bus"),
        ("55", "Van-Based Bus"),
        ("58", "Other Bus Type"),
        ("59", "Unknown Bus Type"),
        ("60", "Step Van"),
        ("61", "Single-Unit Straight Truck or Cab-Chassis (GVWR range 10,001 to 19,500 lbs)"),
        ("62", "Single-Unit Straight Truck or Cab-Chassis (GVWR range 19,501 to 26,000 lbs)"),
        ("63", "Single-Unit Straight Truck or Cab-Chassis (GVWR > 26,000 lbs)"),
        ("64", "Single-Unit Straight Truck or Cab-Chassis (GVWR Unknown)"),
        ("65", "Medium/Heavy Vehicle-Based Motorhome"),
        ("66", "Truck/Tractor"),
        ("67", "Medium/Heavy Pickup"),
        ("71", "Unknown if Single-Unit or Combination-Unit Medium Truck"),
        ("72", "Unknown if Single-Unit or Combination-Unit Heavy Truck"),
        ("73", "Camper or Motorhome, Unknown GVWR"),
        ("78", "Unknown Medium/Heavy Truck Type"),
        ("79", "Unknown Truck Type"),
        ("80", "Two Wheel Motorcycle"),
        ("81", "Moped or Motorized Bicycle"),
        ("82", "Three-Wheel Motorcycle"),
        ("83", "Off-Road Motorcycle"),
        ("84", "Motor Scooter"),
        ("85", "Unenclosed 3-Wheel Motorcycle/Unenclosed Autocycle"),
        ("86", "Enclosed 3-Wheel Motorcycle/Unenclosed Autocycle"),
        ("87", "Unknown Three Wheel Motorcycle Type"),
        ("88", "Other Motored Cycle Type"),
        ("89", "Unknown Motored Cycle Type"),
        ("90", "ATV"),
        ("91", "Snowmobile"),
        ("92", "Farm Equipment Other Than Trucks"),
        ("93", "Construction Equipment Other Than Trucks"),
        ("94", "Low Speed Vehicle/Neighborhood Electric Vehicle"),
        ("95", "Golf Cart"),
        ("96", "Recreational Off-Highway Vehicle"),
        ("97", "Other Vehicle Type"),
        ("98", "Not Reported"),
        ("99", "Unknown Body Type"),
    ]),
    ("2018-2019", [
        ("1", "Convertible"),
        ("2", "2-Door Sedan/Hardtop/Coupe"),
        ("3", "3-Door/2-Door Hatchback"),
        ("4", "4-Door Sedan/Hardtop"),
        ("5", "5-Door/4-Door Hatchback"),
        ("6", "Station Wagon"),
        ("7", "Hacthback, Number of Doors Unknown"),
        ("8", "Sedan/Hardtop, Number of Doors Unknown"),
        ("9", "Other or Unknown Automobile Type"),
        ("10", "Auto-Based Pickup"),
        ("11", "Auto-Based Panel"),
        ("12", "Large Limousine - More Than Four Side Doors or Stretch Chassis"),
        ("13", "Three-Wheel Automobile or Automobile Derivative"),
        ("14", "Compact Utility"),
        ("15", "Large Utility"),
        ("16", "Utility Station Wagon"),
        ("17", "3-Door Coupe"),
        ("19", "Utility Unknown Body"),
        ("20", "Minivan"),
        ("21", "Large Van - Includes Van-Based Buses"),
        ("22", "Step Van or Walk-In Van"),
        ("28", "Other Van Type"),
        ("29", "Unknown Van Type"),
        ("33", "Convertible Pickup"),
        ("34", "Light Pickup"),
        ("39", "Unknown Light Conventional Truck Type"),
        ("40", "Cab Chassis-Based"),
        ("41", "Truck-Based Panel"),
        ("42", "Light-Truck-Based Motorhome"),
        ("45", "Other Light Conventional Truck Type"),
        ("48", "Unknown Light Truck Type"),
        ("49", "Unknown Light-Vehicle Type"),
        ("50", "School Bus"),
        ("51", "Cross-Country/Intercity Bus"),
        ("52", "Transit Bus"),
        ("55", "Van-Based Bus"),
        ("58", "Other Bus Type"),
        ("59", "Unknown Bus Type"),
        ("60", "Step Van"),
        ("61", "Single-Unit Straight Truck or Cab-Chassis (GVWR range 10,001 to 19,500 lbs)"),
        ("62", "Single-Unit Straight Truck or Cab-Chassis (GVWR range 19,501 to 26,000 lbs)"),
        ("63", "Single-Unit Straight Truck or Cab-Chassis (GVWR > 26,000 lbs)"),
        ("64", "Single-Unit Straight Truck or Cab-Chassis (GVWR Unknown)"),
        ("65", "Medium/Heavy Truck-Based Motorhome"),
        ("66", "Truck/Tractor"),
        ("67", "Medium/Heavy Pickup"),
        ("71", "Unknown if Single-Unit or Combination-Unit Medium Truck"),
        ("72", "Unknown if Single-Unit or Combination-Unit Heavy Truck"),
        ("73", "Camper or Motorhome, Unknown Truck Type"),
        ("78", "Unknown Medium/Heavy Truck Type"),
        ("79", "Unknown Truck Type"),
        ("80", "Two Wheel Motorcycle"),
        ("81", "Moped or Motorized Bicycle"),
        ("82", "Three-Wheel Motorcycle"),
        ("83", "Off-Road Motorcycle"),
        ("84", "Motor Scooter"),
        ("85", "Unenclosed 3-Wheel Motorcycle/Unenclosed Autocycle"),
        ("86", "Enclosed 3-Wheel Motorcycle/Unenclosed Autocycle"),
        ("87", "Unknown Three Wheel Motorcycle Type"),
        ("88", "Other Motored Cycle Type"),
        ("89", "Unknown Motored Cycle Type"),
        ("90", "ATV"),
        ("91", "Snowmobile"),
        ("92", "Farm Equipment Other Than Trucks"),
        ("93", "Construction Equipment Other Than Trucks"),
        ("94", "Low Speed Vehicle/Neighborhood Electric Vehicle"),
        ("95", "Golf Cart"),
        ("96", "Recreational Off-Highway Vehicle"),
        ("97", "Other Vehicle Type"),
        ("98", "Not Reported"),
        ("99", "Unknown Body Type"),
    ]),
    ("2017", [
        ("1", "Convertible"),
        ("2", "2-Door Sedan/Hardtop/Coupe"),
        ("3", "3-Door/2-Door Hatchback"),
        ("4", "4-Door Sedan/Hardtop"),
        ("5", "5-Door/4-Door Hatchback"),
        ("6", "Station Wagon"),
        ("7", "Hacthback, Number of Doors Unknown"),
        ("8", "Sedan/Hardtop, Number of Doors Unknown"),
        ("9", "Other or Unknown Automobile Type"),
        ("10", "Auto-Based Pickup"),
        ("11", "Auto-Based Panel"),
        ("12", "Large Limousine - More Than Four Side Doors or Stretch Chassis"),
        ("13", "Three-Wheel Automobile or Automobile Derivative"),
        ("14", "Compact Utility"),
        ("15", "Large Utility"),
        ("16", "Utility Station Wagon"),
        ("17", "3-Door Coupe"),
        ("19", "Utility Unknown Body"),
        ("20", "Minivan"),
        ("21", "Large Van - Includes Van-Based Buses"),
        ("22", "Step Van or Walk-In Van"),
        ("28", "Other Van Type"),
        ("29", "Unknown Van Type"),
        ("32", "Pickup with Slide-In Camper"),
        ("33", "Convertible Pickup"),
        ("34", "Light Pickup"),
        ("39", "Unknown Light Conventional Truck Type"),
        ("40", "Cab Chassis-Based"),
        ("41", "Truck-Based Panel"),
        ("42", "Light-Truck-Based Motorhome"),
        ("45", "Other Light Conventional Truck Type"),
        ("48", "Unknown Light Truck Type"),
        ("49", "Unknown Light-Vehicle Type"),
        ("50", "School Bus"),
        ("51", "Cross-Country/Intercity Bus"),
        ("52", "Transit Bus"),
        ("55", "Van-Based Bus"),
        ("58", "Other Bus Type"),
        ("59", "Unknown Bus Type"),
        ("60", "Step Van"),
        ("61", "Single-Unit Straight Truck or Cab-Chassis (GVWR range 10,001 to 19,500 lbs)"),
        ("62", "Single-Unit Straight Truck or Cab-Chassis (GVWR range 19,501 to 26,000 lbs)"),
        ("63", "Single-Unit Straight Truck or Cab-Chassis (GVWR > 26,000 lbs)"),
        ("64", "Single-Unit Straight Truck or Cab-Chassis (GVWR Unknown)"),
        ("65", "Medium/Heavy Truck-Based Motorhome"),
        ("66", "Truck/Tractor"),
        ("67", "Medium/Heavy Pickup"),
        ("71", "Unknown if Single-Unit or Combination-Unit Medium Truck"),
        ("72", "Unknown if Single-Unit or Combination-Unit Heavy Truck"),
        ("73", "Camper or Motorhome, Unknown Truck Type"),
        ("78", "Unknown Medium/Heavy Truck Type"),
        ("79", "Unknown Truck Type"),
        ("80", "Two Wheel Motorcycle"),
        ("81", "Moped or Motorized Bicycle"),
        ("82", "Three-Wheel Motorcycle"),
        ("83", "Off-Road Motorcycle"),
        ("84", "Motor Scooter"),
        ("85", "Unenclosed 3-Wheel Motorcycle/Unenclosed Autocycle"),
        ("86", "Enclosed 3-Wheel Motorcycle/Unenclosed Autocycle"),
        ("87", "Unknown Three Wheel Motorcycle Type"),
        ("88", "Other Motored Cycle Type"),
        ("89", "Unknown Motored Cycle Type"),
        ("90", "ATV"),
        ("91", "Snowmobile"),
        ("92", "Farm Equipment Other Than Trucks"),
        ("93", "Construction Equipment Other Than Trucks"),
        ("94", "Low Speed Vehicle/Neighborhood Electric Vehicle"),
        ("95", "Golf Cart"),
        ("96", "Recreational Off-Highway Vehicle"),
        ("97", "Other Vehicle Type"),
        ("98", "Not Reported"),
        ("99", "Unknown Body Type"),
    ]),
    ("2010-2016", [
        ("1", "Convertible"),
        ("2", "2-Door Sedan/Hardtop/Coupe"),
        ("3", "3-Door/2-Door Hatchback"),
        ("4", "4-Door Sedan/Hardtop"),
        ("5", "5-Door/4-Door Hatchback"),
        ("6", "Station Wagon"),
        ("7", "Hacthback, Number of Doors Unknown"),
        ("8", "Sedan/Hardtop, Number of Doors Unknown"),
        ("9", "Other or Unknown Automobile Type"),
        ("10", "Auto-Based Pickup"),
        ("11", "Auto-Based Panel"),
        ("12", "Large Limousine - More Than Four Side Doors or Stretch Chassis"),
        ("13", "Three-Wheel Automobile or Automobile Derivative"),
        ("14", "Compact Utility"),
        ("15", "Large Utility"),
        ("16", "Utility Station Wagon"),
        ("17", "3-Door Coupe"),
        ("19", "Utility Unknown Body"),
        ("20", "Minivan"),
        ("21", "Large Van - Includes Van-Based Buses"),
        ("22", "Step Van or Walk-In Van"),
        ("28", "Other Van Type"),
        ("29", "Unknown Van Type"),
        ("30", "Compact Pickup"),
        ("31", "Standard Pickup"),
        ("32", "Pickup with Slide-In Camper"),
        ("33", "Convertible Pickup"),
        ("39", "Unknown Light Conventional Truck Type"),
        ("40", "Cab Chassis-Based"),
        ("41", "Truck-Based Panel"),
        ("42", "Light-Truck-Based Motorhome"),
        ("45", "Other Light Conventional Truck Type"),
        ("48", "Unknown Light Truck Type"),
        ("49", "Unknown Light-Vehicle Type"),
        ("50", "School Bus"),
        ("51", "Cross-Country/Intercity Bus"),
        ("52", "Transit Bus"),
        ("55", "Van-Based Bus"),
        ("58", "Other Bus Type"),
        ("59", "Unknown Bus Type"),
        ("60", "Step Van"),
        ("61", "Single-Unit Straight Truck or Cab-Chassis (GVWR range 10,001 to 19,500 lbs)"),
        ("62", "Single-Unit Straight Truck or Cab-Chassis (GVWR range 19,501 to 26,000 lbs)"),
        ("63", "Single-Unit Straight Truck or Cab-Chassis (GVWR > 26,000 lbs)"),
        ("64", "Single-Unit Straight Truck or Cab-Chassis (GVWR Unknown)"),
        ("65", "Medium/Heavy Truck-Based Motorhome"),
        ("66", "Truck/Tractor"),
        ("67", "Medium/Heavy Pickup"),
        ("68", "Single-Unit Straight Truck (GVWR Unknown)"),
        ("71", "Unknown if Single-Unit or Combination-Unit Medium Truck"),
        ("72", "Unknown if Single-Unit or Combination-Unit Heavy Truck"),
        ("73", "Camper or Motorhome, Unknown Truck Type"),
        ("78", "Unknown Medium/Heavy Truck Type"),
        ("79", "Unknown Truck Type"),
        ("80", "Motorcycle"),
        ("81", "Moped"),
        ("82", "Three-Wheel Motorcycle/Moped - Not All-Terrain Vehicle"),
        ("83", "Off-Road Motorcycle (2-Wheel)"),
        ("88", "Other Motored Cycle Type"),
        ("89", "Unknown Motored Cycle Type"),
        ("90", "ATV"),
        ("91", "Snowmobile"),
        ("92", "Farm Equipment Other Than Trucks"),
        ("93", "Construction Equipment Other Than Trucks"),
        ("94", "Low Speed Vehicle/Neighborhood Electric Vehicle"),
        ("95", "Golf Cart"),
        ("97", "Other Vehicle Type"),
        ("98", "Not Reported"),
        ("99", "Unknown Body Type"),
    ]),
    ("1991-2009", [
        ("1", "Convertible"),
        ("2", "2-Door Sedan/Hardtop/Coupe"),
        ("3", "3-Door/2-Door Hatchback"),
        ("4", "4-Door Sedan/Hardtop"),
        ("5", "5-Door/4-Door Hatchback"),
        ("6", "Station Wagon"),
        ("7", "Hacthback, Number of Doors Unknown"),
        ("8", "Sedan/Hardtop, Number of Doors Unknown"),
        ("9", "Other or Unknown Automobile Type"),
        ("10", "Auto-Based Pickup"),
        ("11", "Auto-Based Panel"),
        ("12", "Large Limousine - More Than Four Side Doors or Stretch Chassis"),
        ("13", "Three-Wheel Automobile or Automobile Derivative"),
        ("14", "Compact Utility"),
        ("15", "Large Utility"),
        ("16", "Utility Station Wagon"),
        ("19", "Utility Unknown Body"),
        ("20", "Minivan"),
        ("21", "Large Van - Includes Van-Based Buses"),
        ("22", "Step Van or Walk-In Van"),
        ("23", "Van Motorhome"),
        ("24", "Van-Based School Bus"),
        ("25", "Van-Based Transit Bus"),
        ("28", "Other Van Type"),
        ("29", "Unknown Van Type"),
        ("30", "Compact Pickup"),
        ("31", "Standard Pickup"),
        ("32", "Pickup with Slide-In Camper"),
        ("33", "Convertible Pickup"),
        ("39", "Unknown Light Conventional Truck Type"),
        ("40", "Cab Chassis-Based"),
        ("41", "Truck-Based Panel"),
        ("42", "Light-Truck-Based Motorhome"),
        ("45", "Other Light Conventional Truck Type"),
        ("48", "Unknown Light-Truck Type"),
        ("49", "Unknown Light-Vehicle Type"),
        ("50", "School Bus"),
        ("51", "Cross-Country/Intercity Bus"),
        ("52", "Transit Bus"),
        ("58", "Other Bus Type"),
        ("59", "Unknown Bus Type"),
        ("60", "Step Van"),
        ("61", "Single-Unit Straight Truck (GVWR range 10,001 to 19,500 lbs)"),
        ("62", "Single-Unit Straight Truck (GVWR range 19,501 to 26,000 lbs)"),
        ("63", "Single-Unit Straight Truck (GVWR > 26,000 lbs)"),
        ("64", "Single-Unit Straight Truck"),
        ("65", "Medium/Heavy Truck-Based Motorhome"),
        ("66", "Truck/Tractor"),
        ("67", "Medium/Heavy Pickup"),
        ("71", "Unknown if Single-Unit or Combination-Unit Medium Truck"),
        ("72", "Unknown if Single-Unit or Combination-Unit Heavy Truck"),
        ("73", "Camper or Motorhome, Unknown Truck Type"),
        ("78", "Unknown Medium/Heavy Truck Type"),
        ("79", "Unknown Truck Type"),
        ("80", "Motorcycle"),
        ("81", "Moped"),
        ("82", "Three-Wheel Motorcycle/Moped - Not All-Terrain Vehicle"),
        ("83", "Off-Road Motorcycle (2-Wheel)"),
        ("88", "Other Motored Cycle Type"),
        ("89", "Unknown Motored Cycle Type"),
        ("90", "ATV"),
        ("91", "Snowmobile"),
        ("92", "Farm Equipment Other Than Trucks"),
        ("93", "Construction Equipment Other Than Trucks"),
        ("94", "Motorized Wheel Chair"),
        ("97", "Other Vehicle Type"),
        ("99", "Unknown Body Type"),
    ]),
]
BODY_TYP_IDS = [
    ("2018", "2018-Later"),
    ("2017", "2017"),
    ("2016", "2010-2016"),
    ("2015", "2010-2016"),
    ("2014", "2010-2016"),
    ("2013", "2010-2016"),
    ("2012", "2010-2016"),
    ("2011", "2010-2016"),
    ("2010", "2010-2016"),
    ("2009", "1991-2009"),
    ("2008", "1991-2009"),
    ("2007", "1991-2009"),
    ("2006", "1991-2009"),
    ("2005", "1991-2009"),
    ("2004", "1991-2009"),
    ("2003", "1991-2009"),
    ("2002", "1991-2009"),
    ("2001", "1991-2009"),
    ("2000", "1991-2009"),
    ("1999", "1991-2009"),
    ("1998", "1991-2009"),
    ("1997", "1991-2009"),
    ("1996", "1991-2009"),
    ("1995", "1991-2009"),
    ("1994", "1991-2009"),
    ("1993", "1991-2009"),
    ("1992", "1991-2009"),
    ("1991", "1991-2009"),
]


def GET_BODY_TYP():
    return BODY_TYP


def GET_BODY_TYP_IDS():
    return BODY_TYP_IDS


IMPACT1 = [
    ("2017-Later", [
        ("0", "Non-Collision"),
        ("1", "Clock point 1"),
        ("2", "Clock point 2"),
        ("3", "Clock point 3"),
        ("4", "Clock point 4"),
        ("5", "Clock point 5"),
        ("6", "Clock point 6"),
        ("7", "Clock point 7"),
        ("8", "Clock point 8"),
        ("9", "Clock point 9"),
        ("10", "Clock point 10"),
        ("11", "Clock point 11"),
        ("12", "Clock point 12"),
        ("13", "Top"),
        ("14", "Undercarriage"),
        ("18", "Cargo/Vehicle Parts Set-In-Motion"),
        ("19", "Other Objects Set-In-Motion"),
        ("20", "Object Set in Motion, Unknown if Cargo/Vehicle Parts or Other"),
        ("61", "Left"),
        ("62", "Left-Front Side"),
        ("63", "Left-Back Side"),
        ("81", "Right"),
        ("82", "Right-Front Side"),
        ("83", "Right-Back Side"),
        ("98", "Not Reported"),
        ("99", "Unknown"),
    ]),
    ("2013-2016", [
        ("0", "Non-Collision"),
        ("1", "Clock point 1"),
        ("2", "Clock point 2"),
        ("3", "Clock point 3"),
        ("4", "Clock point 4"),
        ("5", "Clock point 5"),
        ("6", "Clock point 6"),
        ("7", "Clock point 7"),
        ("8", "Clock point 8"),
        ("9", "Clock point 9"),
        ("10", "Clock point 10"),
        ("11", "Clock point 11"),
        ("12", "Clock point 12"),
        ("13", "Top"),
        ("14", "Undercarriage"),
        ("18", "Cargo/Vehicle Parts Set-In-Motion"),
        ("19", "Other Objects Set-In-Motion"),
        ("61", "Left"),
        ("62", "Left-Front Side"),
        ("63", "Left-Back Side"),
        ("81", "Right"),
        ("82", "Right-Front Side"),
        ("83", "Right-Back Side"),
        ("98", "Not Reported"),
        ("99", "Unknown"),
    ]),
    ("2012", [
        ("0", "Non-Collision"),
        ("1", "Clock point 1"),
        ("2", "Clock point 2"),
        ("3", "Clock point 3"),
        ("4", "Clock point 4"),
        ("5", "Clock point 5"),
        ("6", "Clock point 6"),
        ("7", "Clock point 7"),
        ("8", "Clock point 8"),
        ("9", "Clock point 9"),
        ("10", "Clock point 10"),
        ("11", "Clock point 11"),
        ("12", "Clock point 12"),
        ("13", "Top"),
        ("14", "Undercarriage"),
        ("18", "Set-In-Motion"),
        ("61", "Left"),
        ("62", "Left-Front Side"),
        ("63", "Left-Back Side"),
        ("81", "Right"),
        ("82", "Right-Front Side"),
        ("83", "Right-Back Side"),
        ("98", "Not Reported"),
        ("99", "Unknown"),
    ]),
    ("2010-2011", [
        ("0", "Non-Collision"),
        ("1", "Clock point 1"),
        ("2", "Clock point 2"),
        ("3", "Clock point 3"),
        ("4", "Clock point 4"),
        ("5", "Clock point 5"),
        ("6", "Clock point 6"),
        ("7", "Clock point 7"),
        ("8", "Clock point 8"),
        ("9", "Clock point 9"),
        ("10", "Clock point 10"),
        ("11", "Clock point 11"),
        ("12", "Clock point 12"),
        ("13", "Top"),
        ("14", "Undercarriage"),
        ("18", "Set-In-Motion"),
        ("61", "Left"),
        ("62", "Left-Front Half"),
        ("63", "Left-Back Half"),
        ("81", "Right"),
        ("82", "Right-Front Half"),
        ("83", "Right-Back Half"),
        ("98", "Not Reported"),
        ("99", "Unknown"),
    ]),
    ("1994-2009", [
        ("0", "Non-Collision"),
        ("1", "Clock point 1"),
        ("2", "Clock point 2"),
        ("3", "Clock point 3"),
        ("4", "Clock point 4"),
        ("5", "Clock point 5"),
        ("6", "Clock point 6"),
        ("7", "Clock point 7"),
        ("8", "Clock point 8"),
        ("9", "Clock point 9"),
        ("10", "Clock point 10"),
        ("11", "Clock point 11"),
        ("12", "Clock point 12"),
        ("13", "Top"),
        ("14", "Undercarriage"),
        ("18", "This Vehicle Set Something in Motion Causing Injury or Damage"),
        ("99", "Unknown"),
    ]),
    ("1975-1993", [
        ("0", "Non-Collision"),
        ("1", "Clock point 1"),
        ("2", "Clock point 2"),
        ("3", "Clock point 3"),
        ("4", "Clock point 4"),
        ("5", "Clock point 5"),
        ("6", "Clock point 6"),
        ("7", "Clock point 7"),
        ("8", "Clock point 8"),
        ("9", "Clock point 9"),
        ("10", "Clock point 10"),
        ("11", "Clock point 11"),
        ("12", "Clock point 12"),
        ("13", "Top"),
        ("14", "Undercarriage"),
        ("15", "Underride"),
        ("16", "Override"),
        ("99", "Unknown"),
    ]),
]
IMPACT1_IDS = [
    ("2018", "2017-Later"),
    ("2017", "2017-Later"),
    ("2016", "2013-2016"),
    ("2015", "2013-2016"),
    ("2014", "2013-2016"),
    ("2013", "2013-2016"),
    ("2012", "2012"),
    ("2011", "2010-2011"),
    ("2010", "2010-2011"),
    ("2009", "1994-2009"),
    ("2008", "1994-2009"),
    ("2007", "1994-2009"),
    ("2006", "1994-2009"),
    ("2005", "1994-2009"),
    ("2004", "1994-2009"),
    ("2003", "1994-2009"),
    ("2002", "1994-2009"),
    ("2001", "1994-2009"),
    ("2000", "1994-2009"),
    ("1999", "1994-2009"),
    ("1998", "1994-2009"),
    ("1997", "1994-2009"),
    ("1996", "1994-2009"),
    ("1995", "1994-2009"),
    ("1994", "1994-2009"),
    ("1993", "1975-1993"),
    ("1992", "1975-1993"),
    ("1991", "1975-1993"),
    ("1990", "1975-1993"),
    ("1989", "1975-1993"),
    ("1988", "1975-1993"),
    ("1987", "1975-1993"),
    ("1986", "1975-1993"),
    ("1985", "1975-1993"),
    ("1984", "1975-1993"),
    ("1983", "1975-1993"),
    ("1982", "1975-1993"),
    ("1981", "1975-1993"),
    ("1980", "1975-1993"),
    ("1979", "1975-1993"),
    ("1978", "1975-1993"),
    ("1977", "1975-1993"),
    ("1976", "1975-1993"),
    ("1975", "1975-1993"),
]


def GET_IMPACT1():
    return IMPACT1


def GET_IMPACT1_IDS():
    return IMPACT1_IDS


MAKE = [
    ("1", "American Motors"),
    ("2", "Jeep/Kaiser-Jeep/Willys Jeep"),
    ("3", "AM General"),
    ("6", "Chrysler"),
    ("7", "Dodge"),
    ("8", "Imperial"),
    ("9", "Plymouth"),
    ("10", "Eagle"),
    ("12", "Ford"),
    ("13", "Lincoln"),
    ("14", "Mercury"),
    ("18", "Buick/Opel"),
    ("19", "Cadillac"),
    ("20", "Chevrolet"),
    ("21", "Oldsmobile"),
    ("22", "Pontiac"),
    ("23", "GMC"),
    ("24", "Saturn"),
    ("25", "Grumman"),
    ("26", "Coda (Since 2013)"),
    ("29", "Other Domestic"),
    ("30", "Volkswagen"),
    ("31", "Alfa Romeo"),
    ("32", "Audi"),
    ("33", "Austin/Austin Healey"),
    ("34", "BMW"),
    ("35", "Datsun/Nissan"),
    ("36", "Fiat"),
    ("37", "Honda"),
    ("38", "Isuzu"),
    ("39", "Jaguar"),
    ("40", "Lancia"),
    ("41", "Mazda"),
    ("42", "Mercedes-Benz"),
    ("43", "MG"),
    ("44", "Peugeot"),
    ("45", "Porsche"),
    ("46", "Renault"),
    ("47", "Saab"),
    ("48", "Subaru"),
    ("49", "Toyota"),
    ("50", "Triumph"),
    ("51", "Volvo"),
    ("52", "Mitsubishi"),
    ("53", "Suzuki"),
    ("54", "Acura"),
    ("55", "Hyundai"),
    ("56", "Merkur"),
    ("57", "Yugo"),
    ("58", "Infiniti"),
    ("59", "Lexus"),
    ("60", "Daihatsu"),
    ("61", "Sterling"),
    ("62", "Land Rover"),
    ("63", "Kia"),
    ("64", "Daewoo"),
    ("65", "Smart (Since 2010)"),
    ("66", "Mahindra (2011-2013)"),
    ("67", "Scion (Since 2012)"),
    ("69", "Other Imports"),
    ("70", "BSA"),
    ("71", "Ducati"),
    ("72", "Harley-Davidson"),
    ("73", "Kawasaki"),
    ("74", "Moto Guzzi"),
    ("75", "Norton"),
    ("76", "Yamaha"),
    ("77", "Victory"),
    ("78", "Other Make Moped (Since 2010)"),
    ("79", "Other Make Motored Cycle (Since 2010)"),
    ("80", "Brockway"),
    ("81", "Diamond Reo/Reo"),
    ("82", "Freightliner"),
    ("83", "FWD"),
    ("84", "International Harvester/Navistar"),
    ("85", "Kenworth"),
    ("86", "Mack"),
    ("87", "Peterbilt"),
    ("88", "Iveco/Magirus"),
    ("89", "White/Autocar, White/GMC"),
    ("90", "Bluebird"),
    ("91", "Eagle Coach"),
    ("92", "Gillig"),
    ("93", "MCI"),
    ("94", "Thomas Built"),
    ("97", "Not Reported (Since 2010)"),
    ("98", "Other Make"),
    ("99", "Unknown Make"),
]


def GET_MAKE():
    return MAKE


ROLLOVER = [
    ("2009-Later", [
        ("0", "No Rollover"),
        ("1", "Rollover, Tripped by Object/Vehicle"),
        ("2", "Rollover, Untripped"),
        ("9", "Rollover, Unknown Type"),
    ]),
    ("1978-2008", [
        ("0", "No Rollover"),
        ("1", "First Event"),
        ("2", "Subsequent Event")
    ]),
]
ROLLOVER_IDS = [
    ("2018", "2009-Later"),
    ("2017", "2009-Later"),
    ("2016", "2009-Later"),
    ("2015", "2009-Later"),
    ("2014", "2009-Later"),
    ("2013", "2009-Later"),
    ("2012", "2009-Later"),
    ("2011", "2009-Later"),
    ("2010", "2009-Later"),
    ("2009", "2009-Later"),
    ("2008", "1978-2008"),
    ("2007", "1978-2008"),
    ("2006", "1978-2008"),
    ("2005", "1978-2008"),
    ("2004", "1978-2008"),
    ("2003", "1978-2008"),
    ("2002", "1978-2008"),
    ("2001", "1978-2008"),
    ("2000", "1978-2008"),
    ("1999", "1978-2008"),
    ("1998", "1978-2008"),
    ("1997", "1978-2008"),
    ("1996", "1978-2008"),
    ("1995", "1978-2008"),
    ("1994", "1978-2008"),
    ("1993", "1978-2008"),
    ("1992", "1978-2008"),
    ("1991", "1978-2008"),
    ("1990", "1978-2008"),
    ("1989", "1978-2008"),
    ("1988", "1978-2008"),
    ("1987", "1978-2008"),
    ("1986", "1978-2008"),
    ("1985", "1978-2008"),
    ("1984", "1978-2008"),
    ("1983", "1978-2008"),
    ("1982", "1978-2008"),
    ("1981", "1978-2008"),
    ("1980", "1978-2008"),
    ("1979", "1978-2008"),
    ("1978", "1978-2008"),
]


def GET_ROLLOVER():
    return ROLLOVER


def GET_ROLLOVER_IDS():
    return ROLLOVER_IDS


SCH_BUS = [
    ("0", "No"),
    ("1", "Yes"),
    ("8", "Not Reported")
    ]


def GET_SCH_BUS():
    return SCH_BUS


SPEC_USE = [
    ("2018-Later", [
        ("0", "No Special Use"),
        ("1", "Taxi"),
        ("2", "Vehicle Used for School Transport"),
        ("3", "Vehicle Used as Other Bus"),
        ("4", "Military"),
        ("5", "Police"),
        ("6", "Ambulance"),
        ("7", "Fire Truck"),
        ("8", "Non-Transport Emergency Services Vehicle"),
        ("13", "Incident Response"),
        ("98", "Not Reported"),
        ("99", "Reported as Unknown"),
    ]),
    ("2013-2017", [
        ("0", "No Special Use"),
        ("1", "Taxi"),
        ("2", "Vehicle Used for School Transport"),
        ("3", "Vehicle Used as Other Bus"),
        ("4", "Military"),
        ("5", "Police"),
        ("6", "Ambulance"),
        ("7", "Fire Truck"),
        ("8", "Non-Transport Emergency Services Vehicle"),
        ("13", "Incident Response"),
        ("98", "Not Reported"),
        ("99", "Unknown"),
    ]),
    ("2012", [
        ("0", "No Special Use"),
        ("1", "Taxi"),
        ("2", "Vehicle Used for School Transport"),
        ("3", "Vehicle Used as Other Bus"),
        ("4", "Military"),
        ("5", "Police"),
        ("6", "Ambulance"),
        ("7", "Fire Truck"),
        ("8", "Emergency Services Vehicle"),
        ("98", "Not Reported"),
        ("99", "Unknown"),
    ]),
    ("2010-2011", [
        ("0", "No Special Use"),
        ("1", "Taxi"),
        ("2", "Vehicle Used for School Bus"),
        ("3", "Vehicle Used as Other Bus"),
        ("4", "Military"),
        ("5", "Police"),
        ("6", "Ambulance"),
        ("7", "Fire Truck"),
        ("8", "Emergency Services Vehicle"),
        ("98", "Not Reported"),
        ("99", "Unknown"),
    ]),
    ("1975-2009", [
        ("0", "No Special Use"),
        ("1", "Taxi"),
        ("2", "Vehicle Used for School Bus"),
        ("3", "Vehicle Used as Other Bus"),
        ("4", "Military"),
        ("5", "Police"),
        ("6", "Ambulance"),
        ("7", "Fire Truck"),
        ("8", "Emergency Services Vehicle"),
        ("9", "Unknown"),
    ]),
]
SPEC_USE_IDS = [
    ("2018", "2018-Later"),
    ("2017", "2013-2017"),
    ("2016", "2013-2017"),
    ("2015", "2013-2017"),
    ("2014", "2013-2017"),
    ("2013", "2013-2017"),
    ("2012", "2012"),
    ("2011", "2010-2011"),
    ("2010", "2010-2011"),
    ("2009", "1975-2009"),
    ("2008", "1975-2009"),
    ("2007", "1975-2009"),
    ("2006", "1975-2009"),
    ("2005", "1975-2009"),
    ("2004", "1975-2009"),
    ("2003", "1975-2009"),
    ("2002", "1975-2009"),
    ("2001", "1975-2009"),
    ("2000", "1975-2009"),
    ("1999", "1975-2009"),
    ("1998", "1975-2009"),
    ("1997", "1975-2009"),
    ("1996", "1975-2009"),
    ("1995", "1975-2009"),
    ("1994", "1975-2009"),
    ("1993", "1975-2009"),
    ("1992", "1975-2009"),
    ("1991", "1975-2009"),
    ("1990", "1975-2009"),
    ("1989", "1975-2009"),
    ("1988", "1975-2009"),
    ("1987", "1975-2009"),
    ("1986", "1975-2009"),
    ("1985", "1975-2009"),
    ("1984", "1975-2009"),
    ("1983", "1975-2009"),
    ("1982", "1975-2009"),
    ("1981", "1975-2009"),
    ("1980", "1975-2009"),
    ("1979", "1975-2009"),
    ("1978", "1975-2009"),
    ("1977", "1975-2009"),
    ("1976", "1975-2009"),
    ("1975", "1975-2009"),
]


def GET_SPEC_USE():
    return SPEC_USE


def GET_SPEC_USE_IDS():
    return SPEC_USE_IDS


DAY_WEEK = [
    ("1", "Sunday"),
    ("2", "Monday"),
    ("3", "Tuesday"),
    ("4", "Wednesday"),
    ("5", "Thursday"),
    ("6", "Friday"),
    ("7", "Saturday"),
]


def GET_DAY_WEEK():
    return DAY_WEEK


ROUTE = [
    ("1", "Interstate"),
    ("2", "U.S. Highway"),
    ("3", "State Highway"),
    ("4", "County Road"),
    ("5", "Local Street - Township"),
    ("6", "Local Street - Municipality"),
    ("7", "Local Street - Frontage Road"),
    ("8", "Other"),
    ("9", "Unknown"),
]


def GET_ROUTE():
    return ROUTE


RD_OWNER = [
    ("1", "State Highway Agency"),
    ("2", "County Highway Agency"),
    ("3", "Town or Township Highway Agency"),
    ("4", "City or Municipal Highway Agency"),
    ("11", "State Park, Forest or Reservation Agency"),
    ("12", "Local Park, Forest or Reservation Agency"),
    ("21", "Other State Agency"),
    ("25", "Other Local Agency"),
    ("26", "Private (other than Railroad)"),
    ("27", "Railroad"),
    ("31", "State Toll Road"),
    ("32", "Local Toll Authority"),
    ("40", "Other Public Instrumentality (i.e., Airport)"),
    ("50", "Indian Tribe Nation"),
    ("60", "Other Federal Agency"),
    ("62", "Bureau of Indian Affairs"),
    ("63", "Bureau of Fish and Wildlife"),
    ("64", "U.S. Forest Service"),
    ("66", "National Park Service"),
    ("67", "Tennessee Valley Authority"),
    ("68", "Bureau of Land Management"),
    ("69", "Bureau of Reclamation"),
    ("70", "Corps of Engineers"),
    ("72", "Air Force"),
    ("74", "Navy/Marines"),
    ("80", "Army"),
    ("96", "Trafficway Not in State Inventory"),
    ("98", "Not Reported"),
    ("99", "Unknown"),
]
NHS = [
    ("0", "This Section is Not on the National Highway System"),
    ("1", "This Section is on the National Highway System"),
    ("9", "Unknown"),
]


def GET_NHS():
    return NHS


SP_JUR = [
    ("0", "No Special Jurisdiction"),
    ("1", "National Park Service"),
    ("2", "Military"),
    ("3", "Indian Reservation"),
    ("4", "College/University Campus"),
    ("5", "Other Federal Properties"),
    ("8", "Other"),
    ("9", "Unknown"),
]
RELJCT1 = [
    ("2018-Later", [
        ("0", "No"),
        ("1", "Yes"),
        ("8", "Not Reported"),
        ("9", "Reported as Unknown")
    ]),
    ("2010-2017", [
        ("0", "No"),
        ("1", "Yes"),
        ("8", "Not Reported"),
        ("9", "Unknown")
    ]),
]
RELJCT1_IDS = [
    ("2018", "2018"),
    ("2017", "2010-2017"),
    ("2016", "2010-2017"),
    ("2015", "2010-2017"),
    ("2014", "2010-2017"),
    ("2013", "2010-2017"),
    ("2012", "2010-2017"),
    ("2011", "2010-2017"),
    ("2010", "2010-2017"),
]


def GET_RELJCT1():
    return RELJCT1


def GET_RELJCT1_IDS():
    return RELJCT1_IDS


RELJCT2 = [
    ("2018-Later", [
        ("1", "Non-Junction"),
        ("2", "Intersection"),
        ("3", "Intersection Related"),
        ("4", "Driveway Access"),
        ("5", "Entrance/Exit Ramp Related"),
        ("6", "Railway Grade Crossing"),
        ("7", "Crossover Related"),
        ("8", "Driveway Access Related"),
        ("16", "Shared-Use Path Crossing"),
        ("17", "Acceleration/Deceleration Lane"),
        ("18", "Through Roadway"),
        ("19", "Other Location Within Interchange Area"),
        ("20", "Entrance/Exit Ramp"),
        ("98", "Not Reported"),
        ("99", "Reported as Unknown"),
    ]),
    ("2014-2017", [
        ("1", "Non-Junction"),
        ("2", "Intersection"),
        ("3", "Intersection Related"),
        ("4", "Driveway Access"),
        ("5", "Entrance/Exit Ramp Related"),
        ("6", "Railway Grade Crossing"),
        ("7", "Crossover Related"),
        ("8", "Driveway Access Related"),
        ("16", "Shared-Use Path Crossing"),
        ("17", "Acceleration/Deceleration Lane"),
        ("18", "Through Roadway"),
        ("19", "Other Location Within Interchange Area"),
        ("20", "Entrance/Exit Ramp"),
        ("98", "Not Reported"),
        ("99", "Unknown"),
    ]),
    ("2013", [
        ("1", "Non-Junction"),
        ("2", "Intersection"),
        ("3", "Intersection Related"),
        ("4", "Driveway Access"),
        ("5", "Entrance/Exit Ramp Related"),
        ("6", "Railway Grade Crossing"),
        ("7", "Crossover Related"),
        ("8", "Driveway Access Related"),
        ("16", "Shared-Use Path or Trail"),
        ("17", "Acceleration/Deceleration Lane"),
        ("18", "Through Roadway"),
        ("19", "Other Location Within Interchange Area"),
        ("20", "Entrance/Exit Ramp"),
        ("98", "Not Reported"),
        ("99", "Unknown"),
    ]),
    ("2010-2012", [
        ("1", "Non-Junction"),
        ("2", "Intersection"),
        ("3", "Intersection Related"),
        ("4", "Driveway Access"),
        ("5", "Entrance/Exit Ramp Related"),
        ("6", "Railway Grade Crossing"),
        ("7", "Crossover Related"),
        ("8", "Driveway Access Related"),
        ("16", "Shared-Use Path or Trail"),
        ("17", "Acceleration/Deceleration Lane"),
        ("18", "Through Roadway"),
        ("19", "Other Location Within Interchange Area"),
        ("98", "Not Reported"),
        ("99", "Unknown"),
    ]),
    ("1991-2009", [
        ("0", "None"),
        ("1", "Non-Junction"),
        ("2", "Intersection"),
        ("3", "Intersection-Related"),
        ("4", "Driveway, Alley Access, etc."),
        ("5", "Entrance/Exit Ramp-Related"),
        ("6", "Railway Grade Crossing"),
        ("7", "In Crossover"),
        ("8", "Driveway Access Related"),
        ("9", "Unknown, Non-Interchange"),
        ("10", "Intersection"),
        ("11", "Intersection-Related"),
        ("12", "Driveway Access"),
        ("13", "Entrance/Exit Ramp-Related"),
        ("14", "In Crossover"),
        ("15", "Other Location in Interchange"),
        ("19", "Unknown, Interchange Area"),
        ("99", "Unknown"),
    ]),
]
RELJCT2_IDS = [
    ("2018", "2018"),
    ("2017", "2014-2017"),
    ("2016", "2014-2017"),
    ("2015", "2014-2017"),
    ("2015", "2014-2017"),
    ("2014", "2014-2017"),
    ("2013", "2013"),
    ("2012", "2010-2012"),
    ("2011", "2010-2012"),
    ("2010", "2010-2012"),
    ("2009", "1991-2009"),
    ("2008", "1991-2009"),
    ("2007", "1991-2009"),
    ("2006", "1991-2009"),
    ("2005", "1991-2009"),
    ("2004", "1991-2009"),
    ("2003", "1991-2009"),
    ("2002", "1991-2009"),
    ("2001", "1991-2009"),
    ("2000", "1991-2009"),
    ("1999", "1991-2009"),
    ("1998", "1991-2009"),
    ("1997", "1991-2009"),
    ("1996", "1991-2009"),
    ("1995", "1991-2009"),
    ("1994", "1991-2009"),
    ("1993", "1991-2009"),
    ("1992", "1991-2009"),
    ("1991", "1991-2009"),
]


def GET_RELJCT2():
    return RELJCT2


def GET_RELJCT2_IDS():
    return RELJCT2_IDS


TYP_INT = [
    ("2020-Later", [
        ("1", "Not an Intersection"),
        ("2", "Four-Way Intersection"),
        ("3", "T-Intersection"),
        ("4", "Y-Intersection"),
        ("5", "Traffic Circle"),
        ("6", "Roundabout"),
        ("7", "Five-Point, or More"),
        ("10", "L-Intersection"),
        ("11", "Other Intersection Type"),
        ("98", "Not Reported"),
        ("99", "Reported as Unknown"),
    ]),
    ("2018-2019", [
        ("1", "Not an Intersection"),
        ("2", "Four-Way Intersection"),
        ("3", "T-Intersection"),
        ("4", "Y-Intersection"),
        ("5", "Traffic Circle"),
        ("6", "Roundabout"),
        ("7", "Five-Point, or More"),
        ("10", "L-Intersection"),
        ("98", "Not Reported"),
        ("99", "Reported as Unknown"),
    ]),
    ("2013-2017", [
        ("1", "Not an Intersection"),
        ("2", "Four-Way Intersection"),
        ("3", "T-Intersection"),
        ("4", "Y-Intersection"),
        ("5", "Traffic Circle"),
        ("6", "Roundabout"),
        ("7", "Five-Point, or More"),
        ("10", "L-Intersection"),
        ("98", "Not Reported"),
        ("99", "Unknown"),
    ]),
    ("2010", [
        ("1", "Not an Intersection"),
        ("2", "Four-Way Intersection"),
        ("3", "T-Intersection"),
        ("4", "Y-Intersection"),
        ("5", "Traffic Circle"),
        ("6", "Roundabout"),
        ("7", "Five-Point, or More"),
        ("8", "Not Reported"),
        ("9", "Unknown"),
    ]),
]
TYP_INT_IDS = [
    ("2018", "2018"),
    ("2017", "2013-2017"),
    ("2016", "2013-2017"),
    ("2015", "2013-2017"),
    ("2014", "2013-2017"),
    ("2013", "2013-2017"),
    ("2012", "2010"),
    ("2011", "2010"),
    ("2010", "2010"),
]


def GET_TYP_INT():
    return TYP_INT


def GET_TYP_INT_IDS():
    return TYP_INT_IDS


REL_ROAD = [
    ("2018-Later", [
        ("1", "On Roadway"),
        ("2", "On Shoulder"),
        ("3", "On Median"),
        ("4", "On Roadside"),
        ("5", "Outside Trafficway"),
        ("6", "Off Roadway - Location Unknown"),
        ("7", "In Parking Lane/Zone"),
        ("8", "Gore"),
        ("10", "Separator"),
        ("11", "Continuous Left-Turn Lane"),
        ("98", "Not Reported"),
        ("99", "Reported as Unknown"),
    ]),
    ("2010-2017", [
        ("1", "On Roadway"),
        ("2", "On Shoulder"),
        ("3", "On Median"),
        ("4", "On Roadside"),
        ("5", "Outside Trafficway"),
        ("6", "Off Roadway - Location Unknown"),
        ("7", "In Parking Lane/Zone"),
        ("8", "Gore"),
        ("10", "Separator"),
        ("11", "Continuous Left-Turn Lane"),
        ("98", "Not Reported"),
        ("99", "Unknown"),
    ]),
    ("1998-2009", [
        ("1", "On Roadway"),
        ("2", "On Shoulder"),
        ("3", "On Median"),
        ("4", "On Roadside"),
        ("5", "Outside Trafficway/Outside Right-Of-Way"),
        ("6", "Off Roadway - Location Unknown"),
        ("7", "In Parking Lane/Zone"),
        ("8", "Gore"),
        ("10", "Separator"),
        ("11", "Continuous Left-Turn Lane"),
        ("99", "Unknown"),
    ]),
]
REL_ROAD_IDS = [
    ("2018", "2018"),
    ("2017", "2010-2017"),
    ("2016", "2010-2017"),
    ("2015", "2010-2017"),
    ("2014", "2010-2017"),
    ("2013", "2010-2017"),
    ("2012", "2010-2017"),
    ("2011", "2010-2017"),
    ("2010", "2010-2017"),
    ("2009", "1998-2009"),
    ("2008", "1998-2009"),
    ("2007", "1998-2009"),
    ("2006", "1998-2009"),
    ("2005", "1998-2009"),
    ("2004", "1998-2009"),
    ("2003", "1998-2009"),
    ("2002", "1998-2009"),
    ("2001", "1998-2009"),
    ("2000", "1998-2009"),
    ("1999", "1998-2009"),
    ("1998", "1998-2009"),
]


def GET_REL_ROAD():
    return REL_ROAD


def GET_REL_ROAD_IDS():
    return REL_ROAD_IDS


WRK_ZONE = [
    ("2012-Later", [
        ("0", "None"),
        ("1", "Construction"),
        ("2", "Maintenance"),
        ("3", "Utility"),
        ("4", "Work Zone, Type Unknown"),
    ]),
    ("2010-2011", [
        ("0", "None"),
        ("1", "Construction"),
        ("2", "Maintenance"),
        ("3", "Utility"),
        ("4", "Work Zone, Type Unknown"),
        ("8", "Not Reported"),
    ]),
    ("1982-2009", [
        ("0", "None"),
        ("1", "Construction"),
        ("2", "Maintenance"),
        ("3", "Utility"),
        ("4", "Work Zone, Type Unknown"),
    ]),
]
WRK_ZONE_IDS = [
    ("2018", "2012-Later"),
    ("2017", "2012-Later"),
    ("2016", "2012-Later"),
    ("2015", "2012-Later"),
    ("2014", "2012-Later"),
    ("2013", "2012-Later"),
    ("2012", "2012-Later"),
    ("2011", "2010-2011"),
    ("2010", "2010-2011"),
    ("2009", "1982-2009"),
    ("2008", "1982-2009"),
    ("2007", "1982-2009"),
    ("2006", "1982-2009"),
    ("2005", "1982-2009"),
    ("2004", "1982-2009"),
    ("2003", "1982-2009"),
    ("2002", "1982-2009"),
    ("2001", "1982-2009"),
    ("2000", "1982-2009"),
    ("1999", "1982-2009"),
    ("1998", "1982-2009"),
    ("1997", "1982-2009"),
    ("1996", "1982-2009"),
    ("1995", "1982-2009"),
    ("1994", "1982-2009"),
    ("1993", "1982-2009"),
    ("1992", "1982-2009"),
    ("1991", "1982-2009"),
    ("1990", "1982-2009"),
    ("1989", "1982-2009"),
    ("1988", "1982-2009"),
    ("1987", "1982-2009"),
    ("1986", "1982-2009"),
    ("1985", "1982-2009"),
    ("1984", "1982-2009"),
    ("1983", "1982-2009"),
    ("1982", "1982-2009"),
]


def GET_WRK_ZONE():
    return WRK_ZONE


def GET_WRK_ZONE_IDS():
    return WRK_ZONE_IDS


LGT_COND = [
    ("2018-Later", [
        ("1", "Daylight"),
        ("2", "Dark - Not Lighted"),
        ("3", "Dark - Lighted"),
        ("4", "Dawn"),
        ("5", "Dusk"),
        ("6", "Dark - Unknown Lighting"),
        ("7", "Other"),
        ("8", "Not Reported"),
        ("9", "Reported as Unknown"),
    ]),
    ("2010-2017", [
        ("1", "Daylight"),
        ("2", "Dark - Not Lighted"),
        ("3", "Dark - Lighted"),
        ("4", "Dawn"),
        ("5", "Dusk"),
        ("6", "Dark - Unknown Lighting"),
        ("7", "Other"),
        ("8", "Not Reported"),
        ("9", "Unknown"),
    ]),
    ("2009", [
        ("1", "Daylight"),
        ("2", "Dark - Not Lighted"),
        ("3", "Dark but Lighted"),
        ("4", "Dawn"),
        ("5", "Dusk"),
        ("6", "Dark - Unknown Lighting"),
        ("7", "Other"),
        ("9", "Unknown"),
    ]),
    ("1980-2008", [
        ("1", "Daylight"),
        ("2", "Dark"),
        ("3", "Dark but Lighted"),
        ("4", "Dawn"),
        ("5", "Dusk"),
        ("9", "Unknown"),
    ]),
]
LGT_COND_IDS = [
    ("2018", "2018"),
    ("2017", "2010-2017"),
    ("2016", "2010-2017"),
    ("2015", "2010-2017"),
    ("2014", "2010-2017"),
    ("2013", "2010-2017"),
    ("2012", "2010-2017"),
    ("2011", "2010-2017"),
    ("2010", "2010-2017"),
    ("2009", "2009"),
    ("2008", "1980-2008"),
    ("2007", "1980-2008"),
    ("2006", "1980-2008"),
    ("2005", "1980-2008"),
    ("2004", "1980-2008"),
    ("2003", "1980-2008"),
    ("2002", "1980-2008"),
    ("2001", "1980-2008"),
    ("2000", "1980-2008"),
    ("1999", "1980-2008"),
    ("1998", "1980-2008"),
    ("1997", "1980-2008"),
    ("1996", "1980-2008"),
    ("1995", "1980-2008"),
    ("1994", "1980-2008"),
    ("1993", "1980-2008"),
    ("1992", "1980-2008"),
    ("1991", "1980-2008"),
    ("1990", "1980-2008"),
    ("1989", "1980-2008"),
    ("1988", "1980-2008"),
    ("1987", "1980-2008"),
    ("1986", "1980-2008"),
    ("1985", "1980-2008"),
    ("1984", "1980-2008"),
    ("1983", "1980-2008"),
    ("1982", "1980-2008"),
    ("1981", "1980-2008"),
    ("1980", "1980-2008"),
]


def GET_LGT_COND():
    return LGT_COND


def GET_LGT_COND_IDS():
    return LGT_COND_IDS


WEATHER = [
    ("2013-Later", [
        ("1", "Clear"),
        ("2", "Rain"),
        ("3", "Sleet, Hail"),
        ("4", "Snow"),
        ("5", "Fog, Smog, Smoke"),
        ("6", "Severe Crosswinds"),
        ("7", "Blowing Sand, Soil, Dirt"),
        ("8", "Other"),
        ("10", "Cloudy"),
        ("11", "Blowing Snow"),
        ("12", "Freezing Rain or Drizzle"),
        ("98", "Not Reported"),
        ("99", "Unknown"),
    ]),
    ("2010-2012", [
        ("1", "Clear"),
        ("0", "No Additional Atmospheric Conditions"),
        ("2", "Rain"),
        ("3", "Sleet, Hail (Freezing Rain or Drizzle)"),
        ("4", "Snow"),
        ("5", "Fog, Smog, Smoke"),
        ("6", "Severe Crosswinds"),
        ("7", "Blowing Sand, Soil, Dirt"),
        ("8", "Other"),
        ("10", "Cloudy"),
        ("11", "Blowing Snow"),
        ("98", "Not Reported"),
        ("99", "Unknown"),
    ]),
    ("2007-2009", [
        ("0", "No Adverse Atmospheric Conditions"),
        ("1", "Clear/Cloud (No Adverse Conditions)"),
        ("2", "Rain (Mist)"),
        ("3", "Sleet (Hail)"),
        ("4", "Snow or Blowing Snow"),
        ("5", "Fog, Smog, Smoke"),
        ("6", "Severe Crosswinds"),
        ("7", "Blowing Sand, Soil, Dirt"),
        ("8", "Other"),
        ("9", "Unknown"),
    ]),
    ("1982-2006", [
        ("1", "No Adverse Atmospheric Conditions"),
        ("2", "Rain (Mist)"),
        ("3", "Sleet (Hail)"),
        ("4", "Snow"),
        ("5", "Fog"),
        ("6", "Rain and Fog"),
        ("7", "Sleet and Fog"),
        ("8", "Other: Smog, Smoke, Blowing Sand or Dust"),
        ("9", "Unknown"),
    ]),
]
WEATHER_IDS = [
    ("2018", "2013-Later"),
    ("2017", "2013-Later"),
    ("2016", "2013-Later"),
    ("2015", "2013-Later"),
    ("2014", "2013-Later"),
    ("2013", "2013-Later"),
    ("2012", "2010-2012"),
    ("2011", "2010-2012"),
    ("2010", "2010-2012"),
    ("2009", "2007-2009"),
    ("2008", "2007-2009"),
    ("2007", "2007-2009"),
    ("2006", "1982-2006"),
    ("2005", "1982-2006"),
    ("2004", "1982-2006"),
    ("2003", "1982-2006"),
    ("2002", "1982-2006"),
    ("2001", "1982-2006"),
    ("2000", "1982-2006"),
    ("1999", "1982-2006"),
    ("1998", "1982-2006"),
    ("1997", "1982-2006"),
    ("1996", "1982-2006"),
    ("1995", "1982-2006"),
    ("1994", "1982-2006"),
    ("1993", "1982-2006"),
    ("1992", "1982-2006"),
    ("1991", "1982-2006"),
    ("1990", "1982-2006"),
    ("1989", "1982-2006"),
    ("1988", "1982-2006"),
    ("1987", "1982-2006"),
    ("1986", "1982-2006"),
    ("1985", "1982-2006"),
    ("1984", "1982-2006"),
    ("1983", "1982-2006"),
    ("1982", "1982-2006"),
]


def GET_WEATHER():
    return WEATHER


def GET_WEATHER1():
    return WEATHER


def GET_WEATHER2():
    return WEATHER


def GET_WEATHER_IDS():
    return WEATHER_IDS


def GET_WEATHER1_IDS():
    return WEATHER_IDS


def GET_WEATHER2_IDS():
    return WEATHER_IDS


CF = [
    ("0", "None"),
    ("1", "Inadequate Warning of Exits, Lanes Narrowing, Traffic Controls etc."),
    ("2", "Shoulder Related (Design or Condition)"),
    ("3", "Other Maintenance or Construction-Created Condition"),
    ("4", "No or Obscured Pavement Marking"),
    ("5", "Surface Under Water"),
    ("6", "Inadequate Construction or Poor Design of Roadway, Bridge, etc."),
    ("7", "Surface Washed Out (Caved in, Road Slippage)"),
    ("12", "Distracted Driver of a Non-Contact Vehicle"),
    ("13", "Aggressive Driving/Road Rage by Non-Contact Vehicle Driver"),
    ("14", "Motor Vehicle Struck By Falling Cargo or Something That Came Loose From or Something That Was Set in Motion By a Vehicle"),
    ("15", "Non-Occupant Struck By Falling Cargo, or Something Came Loose From or Something That Was Set In Motion By A Vehicle"),
    ("16", "Non-Occupant Struck Vehicle"),
    ("17", "Vehicle Set In Motion By Non-Driver"),
    ("18", "Date of Crash and Date of EMS Notification Were Not Same Day"),
    ("19", "Recent Previous Crash Scene Nearby"),
    ("20", "Police-Pursuit-Involved"),
    ("21", "Within Designated School Zone"),
    ("22", "Speed Limit Is a Statutory Limit as Recorded or Was Determined as This State’s “Basic Rule”"),
    ("23", "Indication of a Stalled/Disabled Vehicle"),
    ("24", "Unstabilized Situation Began and All Harmful Events Occurred Off of the Roadway"),
    ("25", "Toll Booth/Plaza Related"),
    ("26", "Backup Due to Prior Non-Recurring Incident"),
    ("27", "Backup Due to Prior Crash"),
    ("28", "Backup Due to Regular Congestion"),
    ("99", "Unknown"),
]


def GET_CF():
    return CF


def GET_CF1():
    return CF


def GET_CF2():
    return CF


def GET_CF3():
    return CF


def GET_RD_OWNER():
    return RD_OWNER


def GET_SP_JUR():
    return SP_JUR


def GET_MAN_COLL():
    return MAN_COLL


def GET_MAN_COLL_IDS():
    return MAN_COLL_IDS


DRUGS = [
    ("0", "No"),
    ("1", "Yes"),
    ("8", "Not Reported"),
    ("9", "Unknown")
    ]


def GET_DRUGS():
    return DRUGS


ALC_RES = [
    ("2018-Later", [
        ("940", "0.94 or Greater BAC Test"),
        ("995", "Not Reported"),
        ("996", "None Given"),
        ("997", "AC Test Performed, Results Unknown"),
        ("998", "PBT Positive Reading with No Actual Value"),
        ("999", "Reported as Unknown if Tested"),
    ]),
    ("2015-2017", [
        ("940", "0.94 or Greater BAC Test"),
        ("995", "Not Reported"),
        ("996", "None Given"),
        ("997", "AC Test Performed, Results Unknown"),
        ("998", "PBT Positive Reading with No Actual Value"),
        ("999", "Unknown if Tested"),
    ]),
    ("2010-2014", [
        ("94", "0.94 or Greater BAC Test"),
        ("95", "Not Reported"),
        ("96", "None Given"),
        ("97", "AC Test Performed, Results Unknown"),
        ("98", "PBT Positive Reading with No Actual Value"),
        ("99", "Unknown if Tested"),
    ]),
    ("1991-2009", [
        ("94", "0.94 or Greater BAC Test"),
        ("95", "Test Refused"),
        ("96", "None Given"),
        ("97", "AC Test Performed, Results Unknown"),
        ("98", "PBT Positive Reading with No Actual Value"),
        ("99", "Unknown if Tested/Not Reported"),
    ]),
    ("1975-1990", [
        ("95", "Test Refused"),
        ("96", "None Given"),
        ("97", "AC Test Performed, Results Unknown"),
        ("99", "Unknown"),
    ]),
]
# for i in range(0, 95):
#     ALC_RES["1975-1990"][str(i)] = (
#         ("0." + str("[:02d]".format(i)) + " Actual Value of BAC Test"
#     )
# for i in range(0, 94):
#     ALC_RES["1991-2009"][str(i)] = (
#         ("0." + str("[:02d]".format(i)) + " Actual Value of BAC Test"
#     )
#     ALC_RES["2010-2014"][str(i)] = (
#         ("0." + str("[:02d]".format(i)) + " Actual Value of BAC Test"
#     )
# for i in range(0, 940):
#     ALC_RES["2015-2017"][str(i)] = (
#         ("0." + str("[:03d]".format(i)) + " Actual Value of BAC Test"
#     )
#     ALC_RES["2018-Later"][str(i)] = (
#         ("0." + str("[:03d]".format(i)) + " Actual Value of BAC Test"
#     )
ALC_RES_IDS = [
    ("2018", "2018-Later"),
    ("2017", "2015-2017"),
    ("2016", "2015-2017"),
    ("2015", "2015-2017"),
    ("2014", "2010-2014"),
    ("2013", "2010-2014"),
    ("2012", "2010-2014"),
    ("2011", "2010-2014"),
    ("2010", "2010-2014"),
    ("2009", "1991-2009"),
    ("2008", "1991-2009"),
    ("2007", "1991-2009"),
    ("2006", "1991-2009"),
    ("2005", "1991-2009"),
    ("2004", "1991-2009"),
    ("2003", "1991-2009"),
    ("2002", "1991-2009"),
    ("2001", "1991-2009"),
    ("2000", "1991-2009"),
    ("1999", "1991-2009"),
    ("1998", "1991-2009"),
    ("1997", "1991-2009"),
    ("1996", "1991-2009"),
    ("1995", "1991-2009"),
    ("1994", "1991-2009"),
    ("1993", "1991-2009"),
    ("1992", "1991-2009"),
    ("1991", "1991-2009"),
    ("1990", "1975-1990"),
    ("1989", "1975-1990"),
    ("1988", "1975-1990"),
    ("1987", "1975-1990"),
    ("1986", "1975-1990"),
    ("1985", "1975-1990"),
    ("1984", "1975-1990"),
    ("1983", "1975-1990"),
    ("1982", "1975-1990"),
    ("1981", "1975-1990"),
    ("1980", "1975-1990"),
    ("1979", "1975-1990"),
    ("1978", "1975-1990"),
    ("1977", "1975-1990"),
    ("1976", "1975-1990"),
    ("1975", "1975-1990"),
]


def GET_ALC_RES():
    return ALC_RES


def GET_ALC_RES_IDS():
    return ALC_RES_IDS


ATST_TYP = [
    ("2018-Later", [
        ("0", "Not Tested for Alcohol"),
        ("1", "Blood Test"),
        ("2", "Breath Test (AC)"),
        ("3", "Urine"),
        ("4", "Vitreous"),
        ("5", "Blood Plasma/Serum"),
        ("6", "Blood Clot"),
        ("7", "Liver"),
        ("8", "Other Test Type"),
        ("10", "Preliminary Breath Test (PBT)"),
        ("11", "Breath Test, Unknown Type"),
        ("95", "Not Reported"),
        ("98", "Unknown Test Type"),
        ("99", "Reported as Unknown if Tested"),
    ]),
    ("2015-2017", [
        ("0", "Not Tested for Alcohol"),
        ("1", "Blood Test"),
        ("2", "Breath Test (AC)"),
        ("3", "Urine"),
        ("4", "Vitreous"),
        ("5", "Blood Plasma/Serum"),
        ("6", "Blood Clot"),
        ("7", "Liver"),
        ("8", "Other Test Type"),
        ("10", "Preliminary Breath Test (PBT)"),
        ("95", "Not Reported"),
        ("98", "Unknown Test Type"),
        ("99", "Unknown if Tested"),
    ]),
    ("2010-2014", [
        ("0", "Not Tested for Alcohol"),
        ("1", "Blood Test"),
        ("2", 'Breathalyzer "BAC"'),
        ("3", "Urine"),
        ("4", "Vitreous"),
        ("5", "Blood Plasma/Serum"),
        ("6", "Blood Clot"),
        ("7", "Liver"),
        ("8", "Other Test Type"),
        ("10", "Preliminary Breath Test (PBT)"),
        ("95", "Not Reported"),
        ("98", "Unknown Test Type"),
        ("99", "Unknown if Tested"),
    ]),
    ("2004-2009", [
        ("0", "Not Tested for Alcohol"),
        ("1", "Blood Test"),
        ("2", 'Breathalyzer "BAC"'),
        ("3", "Urine"),
        ("4", "Vitreous"),
        ("5", "Blood Plasma/Serum"),
        ("6", "Blood Clot"),
        ("7", "Liver"),
        ("8", "Other Test Type"),
        ("9", "Unknown/Not Reported"),
        ("10", "Preliminary Breath Test (PBT)"),
        ("98", "Positive Reading with No Actual Value"),
        ("99", "Unknown if Tested/Not Reported"),
    ]),
    ("1998-2003", [
        ("0", "Not Tested for Alcohol"),
        ("1", "Whole Blood"),
        ("2", 'Breath "BAC"'),
        ("3", "Urine"),
        ("4", "Vitreous"),
        ("5", "Blood Plasma/Serum"),
        ("6", "Blood Clot"),
        ("7", "Liver"),
        ("8", "Other Test Type"),
        ("9", "Unknown/Not Reported"),
    ]),
]
ATST_TYP_IDS = [
    ("2018", "2018-Later"),
    ("2017", "2015-2017"),
    ("2016", "2015-2017"),
    ("2015", "2015-2017"),
    ("2014", "2010-2014"),
    ("2013", "2010-2014"),
    ("2012", "2010-2014"),
    ("2011", "2010-2014"),
    ("2010", "2010-2014"),
    ("2009", "2004-2009"),
    ("2008", "2004-2009"),
    ("2007", "2004-2009"),
    ("2006", "2004-2009"),
    ("2005", "2004-2009"),
    ("2004", "2004-2009"),
    ("2003", "1998-2003"),
    ("2002", "1998-2003"),
    ("2001", "1998-2003"),
    ("2000", "1998-2003"),
    ("1999", "1998-2003"),
    ("1998", "1998-2003"),
]


def GET_ATST_TYP():
    return ATST_TYP


def GET_ATST_TYP_IDS():
    return ATST_TYP_IDS


ALC_STATUS = [
    ("2018-Later", [
        ("0", "Test Not Given"),
        ("2", "Test Given"),
        ("8", "Not Reported"),
        ("9", "Reported as Unknown if Tested"),
    ]),
    ("2017", [
        ("0", "Test Not Given"),
        ("2", "Test Given"),
        ("8", "Not Reported"),
        ("9", "Unknown if Tested"),
    ]),
    ("2010-2016", [
        ("0", "Test Not Given"),
        ("1", "Test Refused"),
        ("2", "Test Given"),
        ("8", "Not Reported"),
        ("9", "Unknown if Tested"),
    ]),
    ("2009", [
        ("0", "Test Not Given"),
        ("1", "Test Refused"),
        ("2", "Test Given"),
        ("9", "Unknown if Tested/Not Reported"),
    ]),
]
ALC_STATUS_IDS = [
    ("2018", "2018-Later"),
    ("2017", "2017"),
    ("2016", "2010-2016"),
    ("2015", "2010-2016"),
    ("2014", "2010-2016"),
    ("2013", "2010-2016"),
    ("2012", "2010-2016"),
    ("2011", "2010-2016"),
    ("2010", "2010-2016"),
    ("2009", "2009"),
]


def GET_ALC_STATUS():
    return ALC_STATUS


def GET_ALC_STATUS_IDS():
    return ALC_STATUS_IDS


SEX = [
    ("1", "Male"),
    ("2", "Female"),
    ("3", "Other"),
    ("8", "Not Reported"),
    ("9", "Unknown")
]


def GET_SEX():
    return SEX


PER_TYP = [
    ("2022-Later", [
        ("1", "Driver of a Motor Vehicle In-Transport"),
        ("2", "Passenger of a Motor Vehicle In-Transport"),
        ("3", "Occupant of a Motor Vehicle Not In-Transport"),
        ("4", "Occupant of a Non-Motor Vehicle Transport Device"),
        ("5", "Pedestrian"),
        ("6", "Bicyclist"),
        ("7", "Other Pedalcyclist"),
        ("8", "Person on Personal Conveyance"),
        ("9", "Unknown Occupant Type in a Motor Vehicle In-Transport"),
        ("10", "Person In/On a Building"),
        ("19", "Unknown Type of Non-Motorist")
    ]),
    ("2020-2021", [

    ]),
    ("2011-2019", [
        ("1", "Driver of a Motor Vehicle In-Transport"),
        ("2", "Passenger of a Motor Vehicle In-Transport"),
        ("3", "Occupant of a Motor Vehicle Not In-Transport"),
        ("4", "Occupant of a Non-Motor Vehicle Transport Device"),
        ("5", "Pedestrian"),
        ("6", "Bicyclist"),
        ("7", "Other Cyclist"),
        ("8", "Person on Personal Conveyances"),
        ("9", "Unknown Occupant Type in a Motor Vehicle In-Transport"),
        ("10", "Persons In/On Buidings"),
        ("19", "Unknown Type of Non-Motorist"),
    ]),
    ("2010", [
        ("1", "Driver of a Motor Vehicle In-Transport"),
        ("2", "Passenger of a Motor Vehicle In-Transport"),
        ("3", "Occupant of a Motor Vehicle Not In-Transport"),
        ("4", "Occupant of a Non-Motor Vehicle Transport Device"),
        ("5", "Pedestrian"),
        ("6", "Bicyclist"),
        ("7", "Other Cyclist"),
        ("8", "Person on Personal Conveyances"),
        ("9", "Unknown Occupant Type in a Motor Vehicle In-Transport"),
        ("10", "Persons In/On Buidings"),
        ("19", "Unknown Type of Non-Motorist"),
        ("88", "Not Reported"),
    ]),
    ("1994-2009", [
        ("1", "Driver of a Motor Vehicle In-Transport"),
        ("2", "Passenger of a Motor Vehicle In-Transport"),
        ("3", "Occupant of a Motor Vehicle Not In-Transport"),
        ("4", "Occupant of a Non-Motor Vehicle Transport Device"),
        ("5", "Pedestrian"),
        ("6", "Bicyclist"),
        ("7", "Other Cyclist"),
        ("8", "Other Pedestrian"),
        ("9", "Unknown Occupant Type in a Motor Vehicle In-Transport"),
        ("10", "Persons In/On Buidings"),
        ("19", "Unknown Type of Non-Motorist"),
        ("99", "Unknown"),
    ]),
]
PER_TYP_IDS = [
    ("2018", "2011-Later"),
    ("2017", "2011-Later"),
    ("2016", "2011-Later"),
    ("2015", "2011-Later"),
    ("2014", "2011-Later"),
    ("2013", "2011-Later"),
    ("2012", "2011-Later"),
    ("2011", "2011-Later"),
    ("2010", "2010"),
    ("2009", "1994-2009"),
    ("2008", "1994-2009"),
    ("2007", "1994-2009"),
    ("2006", "1994-2009"),
    ("2005", "1994-2009"),
    ("2004", "1994-2009"),
    ("2003", "1994-2009"),
    ("2002", "1994-2009"),
    ("2001", "1994-2009"),
    ("2000", "1994-2009"),
    ("1999", "1994-2009"),
    ("1998", "1994-2009"),
    ("1997", "1994-2009"),
    ("1996", "1994-2009"),
    ("1995", "1994-2009"),
    ("1994", "1994-2009"),
]


def GET_PER_TYP():
    return PER_TYP


def GET_PER_TYP_IDS():
    return PER_TYP_IDS


INJ_SEV = [
    ("2016-Later", [
        ("0", "No Apparent Injury"),
        ("1", "Possible Injury"),
        ("2", "Suspected Minor Injury"),
        ("3", "Suspected Serious Injury"),
        ("4", "Fatal Injury"),
        ("5", "Injured, Severity Unknown"),
        ("6", "Died Prior to Crash"),
        ("9", "Unknown/Not Reported"),
    ]),
    ("2013-2015", [
        ("0", "No Apparent Injury"),
        ("1", "Possible Injury"),
        ("2", "Suspected Minor Injury"),
        ("3", "Suspected Serious Injury"),
        ("4", "Fatal Injury"),
        ("5", "Injured, Severity Unknown"),
        ("6", "Died Prior to Crash"),
        ("9", "Unknown"),
    ]),
    ("1975-2012", [
        ("0", "No Injury"),
        ("1", "Possible Injury"),
        ("2", "Non-Incapacitating Injury"),
        ("3", "Incapacitating Injury"),
        ("4", "Fatal Injury"),
        ("5", "Injured, Severity Unknown"),
        ("6", "Died Prior to Crash"),
        ("8", "Not Reported"),
        ("9", "Unknown"),
    ]),
]
INJ_SEV_IDS = [
    ("2018", "2016-Later"),
    ("2017", "2016-Later"),
    ("2016", "2016-Later"),
    ("2015", "2013-2015"),
    ("2014", "2013-2015"),
    ("2013", "2013-2015"),
    ("2012", "1975-2012"),
    ("2011", "1975-2012"),
    ("2010", "1975-2012"),
    ("2009", "1975-2012"),
    ("2009", "1975-2012"),
    ("2009", "1975-2012"),
    ("2009", "1975-2012"),
    ("2009", "1975-2012"),
    ("2009", "1975-2012"),
    ("2009", "1975-2012"),
    ("2009", "1975-2012"),
    ("2009", "1975-2012"),
    ("2009", "1975-2012"),
    ("1999", "1975-2012"),
    ("1998", "1975-2012"),
    ("1997", "1975-2012"),
    ("1996", "1975-2012"),
    ("1995", "1975-2012"),
    ("1994", "1975-2012"),
    ("1993", "1975-2012"),
    ("1992", "1975-2012"),
    ("1991", "1975-2012"),
    ("1990", "1975-2012"),
    ("1989", "1975-2012"),
    ("1988", "1975-2012"),
    ("1987", "1975-2012"),
    ("1986", "1975-2012"),
    ("1985", "1975-2012"),
    ("1984", "1975-2012"),
    ("1983", "1975-2012"),
    ("1982", "1975-2012"),
    ("1981", "1975-2012"),
    ("1980", "1975-2012"),
    ("1979", "1975-2012"),
    ("1978", "1975-2012"),
    ("1977", "1975-2012"),
    ("1976", "1975-2012"),
    ("1975", "1975-2012"),
]


def GET_INJ_SEV():
    return INJ_SEV


def GET_INJ_SEV_IDS():
    return INJ_SEV_IDS


SEAT_POS = [
    ("0", "Not a Motor Vehicle Occupant"),
    ("11", "Front Seat - Left Side (Driver's Side)"),
    ("12", "Front Seat - Middle"),
    ("13", "Front Seat - Right Side"),
    ("18", "Front Seat - Other"),
    ("19", "Front Seat - Unknown"),
    ("21", "Second Seat - Left Side"),
    ("22", "Second Seat - Middle"),
    ("23", "Second Seat - Right Side"),
    ("28", "Second Seat - Other"),
    ("29", "Second Seat - Unknown"),
    ("31", "Third Seat - Left Side"),
    ("32", "Third Seat - Middle"),
    ("33", "Third Seat - Right Side"),
    ("38", "Third Seat - Other"),
    ("39", "Third Seat - Unknown"),
    ("41", "Fourth Seat - Left Side"),
    ("42", "Fourth Seat - Middle"),
    ("43", "Fourth Seat - Right Side"),
    ("48", "Fourth Seat - Other"),
    ("49", "Fourth Seat - Unknown"),
    ("50", "Sleeper Section of Cab"),
    ("51", "Other Passenger in Enclosed Passenger or Cargo Area"),
    ("52", "Other Passenger in Unenclosed Passenger or Cargo Area"),
    ("53", "Other Passenger in Passenger or Cargo Area, Unknown Whether or Not Enclosed"),
    ("54", "Trailing Unit"),
    ("55", "Riding on Vehicle Exterior"),
    ("56", "Appended to a Motor Vehicle for Motion"),
    ("98", "Not Reported"),
    ("99", "Unknown"),
]


def GET_SEAT_POS():
    return SEAT_POS


REST_USE = [
    ("2019-Later", [
        ("1", "Shoulder Belt Only Used"),
        ("2", "Lap Belt Only Used"),
        ("3", "Lap and Shoulder Belt Used"),
        ("4", "Child Restraint - Type Unknown"),
        ("5", "DOT-Compliant Motorcycle Helmet"),
        ("6", "Racing-Style Harness Used"),
        ("8", "Restraint Used - Type Unknown"),
        ("10", "Child Restraint System - Forward Facing"),
        ("11", "Child Restraint System - Rear Facing"),
        ("12", "Booster Seat"),
        ("17", "No Helmet"),
        ("19", "Helmet, Unknown if DOT-Compliant"),
        ("20", "None Used/Not Applicable"),
        ("96", "Not a Motor Vehicle Occupant"),
        ("97", "Other"),
        ("98", "Not Reported"),
        ("99", "Reported as Unknown"),
    ]),
    ("2017-2018", [
        ("1", "Shoulder Belt Only Used"),
        ("2", "Lap Belt Only Used"),
        ("3", "Lap and Shoulder Belt Used"),
        ("4", "Child Restraint - Type Unknown"),
        ("5", "DOT-Compliant Motorcycle Helmet"),
        ("8", "Restraint Used - Type Unknown"),
        ("10", "Child Restraint System - Forward Facing"),
        ("11", "Child Restraint System - Rear Facing"),
        ("12", "Booster Seat"),
        ("16", "Helmet, Other than DOT-Compliant Motorcycle Helmet"),
        ("17", "No Helmet"),
        ("19", "Helmet, Unknown if DOT-Compliant"),
        ("20", "None Used/Not Applicable"),
        ("29", "Unknown if Helmet Worn"),
        ("96", "Not a Motor Vehicle Occupant"),
        ("97", "Other"),
        ("98", "Not Reported"),
        ("99", "Unknown"),
    ]),
    ("2013-2016", [
        ("0", "Not Applicable"),
        ("1", "Shoulder Belt Only Used"),
        ("2", "Lap Belt Only Used"),
        ("3", "Lap and Shoulder Belt Used"),
        ("4", "Child Restraint Type Unknown"),
        ("5", "DOT-Compliant Motorcycle Helmet"),
        ("7", "None Used"),
        ("8", "Restraint Used - Type Unknown"),
        ("10", "Child Restraint System - Forward Facing"),
        ("11", "Child Restraint System - Rear Facing"),
        ("12", "Booster Seat"),
        ("16", "Helmet, Other than DOT-Compliant Motorcycle Helmet"),
        ("17", "No Helmet"),
        ("19", "Helmet, Unknown if DOT-Compliant"),
        ("29", "Unknown if Helmet Worn"),
        ("96", "Not a Motor Vehicle Occupant"),
        ("97", "Other"),
        ("98", "Not Reported"),
        ("99", "Unknown"),
    ]),
    ("2010-2012", [
        ("0", "Not Applicable"),
        ("1", "Shoulder Belt Only Used"),
        ("2", "Lap Belt Only Used"),
        ("3", "Lap and Shoulder Belt Used"),
        ("4", "Child Restraint Type Unknown"),
        ("5", "DOT-Compliant Motorcycle Helmet"),
        ("7", "None Used - Motor Vehicle Occupant"),
        ("8", "Restraint Used - Type Unknown"),
        ("10", "Child Restraint System - Forward Facing"),
        ("11", "Child Restraint System - Rear Facing"),
        ("12", "Booster Seat"),
        ("16", "Other Helmet"),
        ("17", "No Helmet"),
        ("96", "Not a Motor Vehicle Occupant"),
        ("97", "Other"),
        ("98", "Not Reported"),
        ("99", "Unknown"),
    ]),
    ("1994-2009", [
        ("0", "None Used- Vehicle Occupant; Not Applicable"),
        ("1", "Shoulder Belt Only Used"),
        ("2", "Lap Belt Only Used"),
        ("3", "Lap and Shoulder Belt Used"),
        ("4", "Child Safety Seat"),
        ("5", "Motorcycle Helmet"),
        ("6", "Bicycle Helmet"),
        ("8", "Restraint Used - Type Unknown"),
        ("10", "Child Restraint System - Forward Facing"),
        ("11", "Child Restraint System - Rear Facing"),
        ("12", "Booster Seat with Lap/Shoulder Belt Used Properly"),
        ("13", "Safety Belt Used Improperly"),
        ("14", "Child Safety Seat Used Improperly"),
        ("15", "Helmets Used Improperly"),
        ("99", "Unknown"),
    ]),
]
REST_USE_IDS = [
    ("2018", "2018-Later"),
    ("2017", "2017"),
    ("2016", "2013-2016"),
    ("2015", "2013-2016"),
    ("2014", "2013-2016"),
    ("2013", "2013-2016"),
    ("2012", "2010-2012"),
    ("2011", "2010-2012"),
    ("2010", "2010-2012"),
    ("2009", "1994-2009"),
    ("2008", "1994-2009"),
    ("2007", "1994-2009"),
    ("2006", "1994-2009"),
    ("2005", "1994-2009"),
    ("2004", "1994-2009"),
    ("2003", "1994-2009"),
    ("2002", "1994-2009"),
    ("2001", "1994-2009"),
    ("2000", "1994-2009"),
    ("1999", "1994-2009"),
    ("1998", "1994-2009"),
    ("1997", "1994-2009"),
    ("1996", "1994-2009"),
    ("1995", "1994-2009"),
    ("1994", "1994-2009"),
]


def GET_REST_USE():
    return REST_USE


def GET_REST_USE_IDS():
    return REST_USE_IDS


REST_MIS = [
    ("0", "No Indication of Misuse"),
    ("1", "Yes, Indication of Misuse"),
    ("7", "None Used/Not Applicable"),
    ("8", "Not a Motor Vehicle Occupant")
]


def GET_REST_MIS():
    return REST_MIS


AIR_BAG = [
    ("2018-Later", [
        ("1", "Deployed: Front"),
        ("2", "Deployed: Side"),
        ("3", "Deployed: Curtain"),
        ("7", "Deployed: Other"),
        ("8", "Deployed: Combination"),
        ("9", "Deployed: Unknown Location"),
        ("20", "Not Deployed"),
        ("97", "Not a Motor Vehicle Occupant"),
        ("98", "Not Reported"),
        ("99", "Reported as Deployment Unknown"),
    ]),
    ("2017", [
        ("1", "Deployed: Front"),
        ("2", "Deployed: Side"),
        ("3", "Deployed: Curtain"),
        ("7", "Deployed: Other"),
        ("8", "Deployed: Combination"),
        ("9", "Deployed: Unknown Location"),
        ("20", "Not Deployed"),
        ("97", "Not a Motor Vehicle Occupant"),
        ("98", "Not Reported"),
        ("99", "Unknown"),
    ]),
    ("2010-2016", [
        ("0", "Not Applicable"),
        ("1", "Deployed: Front"),
        ("2", "Deployed: Side"),
        ("3", "Deployed: Curtain"),
        ("7", "Deployed: Other"),
        ("8", "Deployed: Combination"),
        ("9", "Deployed: Unknown Location"),
        ("20", "Not Deployed"),
        ("28", "Switched Off"),
        ("97", "Not a Motor Vehicle Occupant"),
        ("98", "Not Reported"),
        ("99", "Unknown"),
    ]),
    ("2009", [
        ("0", "Not a Motor Vehicle Occupant/Not Applicable"),
        ("1", "Deployed: Front"),
        ("2", "Deployed: Side"),
        ("3", "Deployed: Curtain"),
        ("7", "Deployed: Other"),
        ("8", "Deployed: Combination"),
        ("9", "Deployed: Unknown Location"),
        ("20", "Not Deployed"),
        ("28", "Switched Off"),
        ("98", "Not Reported"),
        ("99", "Unknown"),
    ]),
    ("1998-2008", [
        ("0", "Non-Motorist"),
        ("1", "Deployed Air Bag From Front"),
        ("2", "Deployed Air Bag From Side"),
        ("7", "Deployed Air Bag Other Direction"),
        ("8", "Deployed Air Bag Multiple Directions"),
        ("9", "Deployed Air Bag Direction Unknown"),
        ("20", "Air Bag Available but Not Deployed for This Seat"),
        ("28", "Air Bag Available and Switched Off"),
        ("29", "Air Bag Available, Deployment Not Known for This Seat"),
        ("30", "Air Bag Not Available for This Seat"),
        ("31", "Air Bag Previously Deployed and Not Replaced"),
        ("32", "Air Bag Disabled or Removed"),
        ("99", "Unknown"),
    ]),
]
AIR_BAG_IDS = [
    ("2018", "2018-Later"),
    ("2017", "2017"),
    ("2016", "2010-2016"),
    ("2015", "2010-2016"),
    ("2014", "2010-2016"),
    ("2013", "2010-2016"),
    ("2012", "2010-2016"),
    ("2011", "2010-2016"),
    ("2010", "2010-2016"),
    ("2009", "2009"),
    ("2008", "1998-2008"),
    ("2007", "1998-2008"),
    ("2006", "1998-2008"),
    ("2005", "1998-2008"),
    ("2004", "1998-2008"),
    ("2003", "1998-2008"),
    ("2002", "1998-2008"),
    ("2001", "1998-2008"),
    ("2000", "1998-2008"),
    ("1999", "1998-2008"),
    ("1998", "1998-2008"),
]


def GET_AIR_BAG():
    return AIR_BAG


def GET_AIR_BAG_IDS():
    return AIR_BAG_IDS


EJECTION = [
    ("2018-Later", [
        ("0", "Not Ejected"),
        ("1", "Totally Ejected"),
        ("2", "Partially Ejected"),
        ("3", "Ejected - Unknown Degree"),
        ("7", "Not Reported"),
        ("8", "Not Applicable"),
        ("9", "Reported as Unknown if Ejected"),
    ]),
    ("2010-2017", [
        ("0", "Not Ejected"),
        ("1", "Totally Ejected"),
        ("2", "Partially Ejected"),
        ("3", "Ejected - Unknown Degree"),
        ("7", "Not Reported"),
        ("8", "Not Applicable"),
        ("9", "Unknown if Ejected"),
    ]),
    ("2007-2009", [
        ("0", "Not Ejected"),
        ("1", "Totally Ejected"),
        ("2", "Partially Ejected"),
        ("3", "Ejected - Unknown Degree"),
        ("8", "Not Applicable"),
        ("9", "Unknown if Ejected"),
    ]),
    ("1975-2006", [
        ("0", "Not Ejected or Not Applicable"),
        ("1", "Totally Ejected"),
        ("2", "Partially Ejected"),
        ("9", "Unknown"),
    ]),
]
EJECTION_IDS = [
    ("2018", "2018-Later"),
    ("2017", "2010-2017"),
    ("2016", "2010-2017"),
    ("2015", "2010-2017"),
    ("2014", "2010-2017"),
    ("2013", "2010-2017"),
    ("2012", "2010-2017"),
    ("2011", "2010-2017"),
    ("2010", "2010-2017"),
    ("2009", "2007-2009"),
    ("2008", "2007-2009"),
    ("2007", "2007-2009"),
    ("2006", "1975-2006"),
    ("2005", "1975-2006"),
    ("2004", "1975-2006"),
    ("2003", "1975-2006"),
    ("2002", "1975-2006"),
    ("2001", "1975-2006"),
    ("2000", "1975-2006"),
    ("1999", "1975-2006"),
    ("1998", "1975-2006"),
    ("1997", "1975-2006"),
    ("1996", "1975-2006"),
    ("1995", "1975-2006"),
    ("1994", "1975-2006"),
    ("1993", "1975-2006"),
    ("1992", "1975-2006"),
    ("1991", "1975-2006"),
    ("1990", "1975-2006"),
    ("1989", "1975-2006"),
    ("1988", "1975-2006"),
    ("1987", "1975-2006"),
    ("1986", "1975-2006"),
    ("1985", "1975-2006"),
    ("1984", "1975-2006"),
    ("1983", "1975-2006"),
    ("1982", "1975-2006"),
    ("1981", "1975-2006"),
    ("1980", "1975-2006"),
    ("1979", "1975-2006"),
    ("1978", "1975-2006"),
    ("1977", "1975-2006"),
    ("1976", "1975-2006"),
    ("1975", "1975-2006"),
]


def GET_EJECTION():
    return EJECTION


def GET_EJECTION_IDS():
    return EJECTION_IDS


EJ_PATH = [
    ("2015-Later", [
        ("0", "Ejection Path Not Applicable"),
        ("1", "Through Side Door Opening"),
        ("2", "Through Side Window"),
        ("3", "Through Windshield"),
        ("4", "Through Back Window"),
        ("5", "Through Back Door/Tailgate Opening"),
        ("6", "Through Roof Opening"),
        ("7", "Through Roof"),
        ("8", "Other Path"),
        ("9", "Ejection Path Unknown"),
    ]),
    ("1991-2015", [
        ("0", "Not Ejected/Not Applicable"),
        ("1", "Through Side Door Opening"),
        ("2", "Through Side Window"),
        ("3", "Through Windshield"),
        ("4", "Through Back Window"),
        ("5", "Through Back Door/Tailgate Opening"),
        ("6", "Through Roof Opening"),
        ("7", "Through Roof"),
        ("8", "Other Path"),
        ("9", "Unknown/Unknown Path"),
    ]),
]
EJ_PATH_IDS = [
    ("2018", "2015-Later"),
    ("2017", "2015-Later"),
    ("2016", "2015-Later"),
    ("2015", "2015-Later"),
    ("2014", "1991-2014"),
    ("2013", "1991-2014"),
    ("2012", "1991-2014"),
    ("2011", "1991-2014"),
    ("2010", "1991-2014"),
    ("2009", "1991-2014"),
    ("2008", "1991-2014"),
    ("2007", "1991-2014"),
    ("2006", "1991-2014"),
    ("2005", "1991-2014"),
    ("2004", "1991-2014"),
    ("2003", "1991-2014"),
    ("2002", "1991-2014"),
    ("2001", "1991-2014"),
    ("2000", "1991-2014"),
    ("1999", "1991-2014"),
    ("1998", "1991-2014"),
    ("1997", "1991-2014"),
    ("1996", "1991-2014"),
    ("1995", "1991-2014"),
    ("1994", "1991-2014"),
    ("1993", "1991-2014"),
    ("1992", "1991-2014"),
    ("1991", "1991-2014"),
]


def GET_EJ_PATH():
    return EJ_PATH


def GET_EJ_PATH_IDS():
    return EJ_PATH_IDS


EXTRICAT = [
    ("0", "Not Extricated/Not Applicable"),
    ("1", "Extricated"), ("9", "Unknown")
    ]


def GET_EXTRICAT():
    return EXTRICAT


DRINKING = [
    ("0", "No"),
    ("1", "Yes"),
    ("8", "Not Reported"), ("9", "Unknown")
    ]


def GET_DRINKING():
    return DRINKING


ALC_DET = [
    ("1", "Evidential Test"),
    ("2", "Preliminary Breath Test"),
    ("3", "Behavioral"),
    ("4", "Passive Alcohol Sensor"),
    ("5", "Observed"),
    ("8", "Other"),
    ("9", "Not Reported"),
]


def GET_ALC_DET():
    return ALC_DET


TOW_VEH = [
    ("2022-Later", [
        ("0", "No Trailers"),
        ("1", "One Trailer"),
        ("2", "Two Trailers"),
        ("3", "Three or More Trailers"),
        ("4", "Yes, Number of Trailers Unknown"),
        ("5", "Vehicle Towing another Motor Vehicle - Fixed Linkage"),
        ("6", "Vehicle Towing another Motor Vehicle - Non-Fixed Linkage"),
        ("7", "Trailing Unit Other than a Trailer or Another Motor Vehicle"),
        ("9", "Unknown"),
    ]),
    ("2009-2021", [
        ("0", "No Trailing Unit"),
        ("1", "Yes, One Trailing Unit"),
        ("2", "Yes, Two Trailing Units"),
        ("3", "Yes, Three or More Trailing Units"),
        ("4", "Yes, Number of Trailing Units Unknown"),
        ("5", "Vehicle Towing another Motor Vehicle - Fixed Linkage"),
        ("6", "Vehicle Towing another Motor Vehicle - Non-Fixed Linkage"),
        ("9", "Unknown"),
    ]),
    ("2004-2008", [
        ("0", "No Trailing Unit"),
        ("1", "Yes, One Trailing Unit"),
        ("2", "Yes, Two Trailing Units"),
        ("3", "Yes, Three or More Trailing Units"),
        ("4", "Yes, Number of Trailing Units Unknown"),
        ("5", "Vehicle Towing another Motor Vehicle"),
        ("9", "Unknown"),
    ]),
    ("1981-1986", [
        ("0", "No Trailing Unit"),
        ("1", "Yes, One Trailing Unit"),
        ("2", "Yes, Two Trailing Units"),
        ("3", "Yes, Three or More Trailing Units"),
        ("4", "Yes, Number of Trailing Units Unknown"),
        ("9", "Unknown"),
    ]),
    ("1982", [
        ("0", "No Trailing Unit"),
        ("1", "Yes, One Trailing Unit"),
        ("4", "Yes, Number of Trailing Units Unknown"),
        ("5", "Yes, Two or More Trailing Units"),
    ]),
    ("1975-1981", [
        ("0", "No Trailing Unit"),
        ("1", "Yes"),
    ]),
]
TOW_VEH_IDS = [
    ("2018", "2009-Later"),
    ("2017", "2009-Later"),
    ("2016", "2009-Later"),
    ("2015", "2009-Later"),
    ("2014", "2009-Later"),
    ("2013", "2009-Later"),
    ("2012", "2009-Later"),
    ("2011", "2009-Later"),
    ("2010", "2009-Later"),
    ("2009", "2009-Later"),
    ("2008", "2004-2008"),
    ("2007", "2004-2008"),
    ("2006", "2004-2008"),
    ("2005", "2004-2008"),
    ("2004", "2004-2008"),
    ("2003", "1981-1986"),
    ("2002", "1981-1986"),
    ("2001", "1981-1986"),
    ("2000", "1981-1986"),
    ("1999", "1981-1986"),
    ("1998", "1981-1986"),
    ("1997", "1981-1986"),
    ("1996", "1981-1986"),
    ("1995", "1981-1986"),
    ("1994", "1981-1986"),
    ("1993", "1981-1986"),
    ("1992", "1981-1986"),
    ("1991", "1981-1986"),
    ("1990", "1981-1986"),
    ("1989", "1981-1986"),
    ("1988", "1981-1986"),
    ("1987", "1981-1986"),
    ("1986", "1981-1986"),
    ("1985", "1981-1986"),
    ("1984", "1981-1986"),
    ("1983", "1981-1986"),
    ("1982", "1982"),
    ("1981", "1975-1981"),
    ("1980", "1975-1981"),
    ("1979", "1975-1981"),
    ("1978", "1975-1981"),
    ("1977", "1975-1981"),
    ("1976", "1975-1981"),
    ("1975", "1975-1981"),
]


def GET_TOW_VEH():
    return TOW_VEH


def GET_TOW_VEH_IDS():
    return TOW_VEH_IDS


HISPANIC = [
    ("2001-Later", [
        ("0", "Not A Fatality"),
        ("1", "Mexican"),
        ("2", "Puerto Rican"),
        ("3", "Cuban"),
        ("4", "Central or South American"),
        ("5", "European Spanish"),
        ("6", "Hispanic, Origin Not Specified or Other Origin"),
        ("7", "Non-Hispanic"),
        ("99", "Unknown"),
    ]),
    ("2000", [
        ("0", "Not A Fatality"),
        ("1", "Mexican"),
        ("2", "Puerto Rican"),
        ("3", "Cuban"),
        ("4", "Central or South American"),
        ("5", "European Spanish"),
        ("6", "Other Hispanic Origin"),
        ("7", "Non-Hispanic"),
        ("99", "Unknown"),
    ]),
    ("1999", [
        ("0", "Not A Fatality"),
        ("1", "Mexican"),
        ("2", "Puerto Rican"),
        ("3", "Cuban"),
        ("4", "Central or South American"),
        ("5", "Other or Unknown Hispanic"),
        ("6", "Hispanic, Origin Not Specified"),
        ("7", "Non-Hispanic"),
        ("99", "Unknown"),
    ]),
]
HISPANIC_IDS = [
    ("2018", "2001-Later"),
    ("2017", "2001-Later"),
    ("2016", "2001-Later"),
    ("2015", "2001-Later"),
    ("2014", "2001-Later"),
    ("2013", "2001-Later"),
    ("2012", "2001-Later"),
    ("2011", "2001-Later"),
    ("2010", "2001-Later"),
    ("2009", "2001-Later"),
    ("2008", "2001-Later"),
    ("2007", "2001-Later"),
    ("2006", "2001-Later"),
    ("2005", "2001-Later"),
    ("2004", "2001-Later"),
    ("2003", "2001-Later"),
    ("2002", "2001-Later"),
    ("2001", "2001-Later"),
    ("2000", "2000"),
    ("1999", "1999"),
]


def GET_HISPANIC():
    return HISPANIC


def GET_HISPANIC_IDS():
    return HISPANIC_IDS


RACE = [
    ("2001-Later", [
        ("0", "Not A Fatality"),
        ("1", "White"),
        ("2", "Black"),
        ("3", "American Indian"),
        ("4", "Chinese"),
        ("5", "Japanese"),
        ("6", "Hawaiian"),
        ("7", "Filipino"),
        ("18", "Asian Indian"),
        ("19", "Other Indian"),
        ("28", "Korean"),
        ("38", "Samoan"),
        ("48", "Vietnamese"),
        ("58", "Guamanian"),
        ("68", "Other Asian or Pacific Islander"),
        ("78", "Asian Or Pacific Islander, No Specific Individual Race"),
        ("97", "Multiple Races"),
        ("98", "All Other Races"),
        ("99", "Unknown"),
    ]),
    ("1999-2000", [
        ("0", "Not A Fatality"),
        ("1", "White"),
        ("2", "Black"),
        ("3", "American Indian"),
        ("4", "Chinese"),
        ("5", "Japanese"),
        ("6", "Hawaiian"),
        ("7", "Filipino"),
        ("18", "Asian Indian"),
        ("19", "Other Indian"),
        ("28", "Korean"),
        ("38", "Samoan"),
        ("48", "Vietnamese"),
        ("58", "Guamanian"),
        ("68", "Other Asian or Pacific Islander"),
        ("78", "Combined Other Asian Or Pacific Islander"),
        ("97", "Multiple Races"),
        ("99", "Unknown"),
    ]),
]
RACE_IDS = [
    ("2018", "2001-Later"),
    ("2017", "2001-Later"),
    ("2016", "2001-Later"),
    ("2015", "2001-Later"),
    ("2014", "2001-Later"),
    ("2013", "2001-Later"),
    ("2012", "2001-Later"),
    ("2011", "2001-Later"),
    ("2010", "2001-Later"),
    ("2009", "2001-Later"),
    ("2008", "2001-Later"),
    ("2007", "2001-Later"),
    ("2006", "2001-Later"),
    ("2005", "2001-Later"),
    ("2004", "2001-Later"),
    ("2003", "2001-Later"),
    ("2002", "2001-Later"),
    ("2001", "2001-Later"),
    ("2000", "1999-2000"),
    ("1999", "1999-2000"),
]


def GET_RACE():
    return RACE


def GET_RACE_IDS():
    return RACE_IDS


WORK_INJ = [
    ("0", "No"),
    ("1", "Yes"),
    ("8", "Not Applicable"),
    ("9", "Unknown")
    ]


def GET_WORK_INJ():
    return WORK_INJ


ROAD_FNC = [
    ("1981-1986", [
        ("1", "Principal Arterial - Interstate"),
        ("2", "Principal Arterial – Other Urban Freeways and Expressways"),
        ("3", "Principal Arterial – Other"),
        ("4", "Minor Arterial"),
        ("5", "Urban Collector"),
        ("6", "Major Rural Collector"),
        ("7", "Minor Rural Collector"),
        ("8", "Local Road or Street"),
        ("9", "Unknown"),
    ]),
    ("1987-Later", [
        ("1", "Rural Principal Arterial - Interstate"),
        ("2", "Rural Principal Arterial - Other"),
        ("3", "Rural Minor Arterial"),
        ("4", "Rural Major Collector"),
        ("5", "Rural Minor Collector"),
        ("6", "Rural Local Road or Street"),
        ("9", "Rural Unknown"),
        ("11", "Urban Principal Arterial - Interstate"),
        ("12", "Urban Principal Arterial - Other Freeways or Expressways"),
        ("13", "Urban Other Principal Arterial"),
        ("14", "Urban Minor Arterial"),
        ("15", "Urban Collector"),
        ("16", "Urban Local Road or Street"),
        ("19", "Urban Unknown"),
        ("99", "Unknown"),
    ]),
]
ROAD_FNC_IDS = [
    ("2014", "1987-Later"),
    ("2013", "1987-Later"),
    ("2012", "1987-Later"),
    ("2011", "1987-Later"),
    ("2010", "1987-Later"),
    ("2009", "1987-Later"),
    ("2008", "1987-Later"),
    ("2007", "1987-Later"),
    ("2006", "1987-Later"),
    ("2005", "1987-Later"),
    ("2004", "1987-Later"),
    ("2003", "1987-Later"),
    ("2002", "1987-Later"),
    ("2001", "1987-Later"),
    ("2000", "1987-Later"),
    ("1999", "1987-Later"),
    ("1998", "1987-Later"),
    ("1997", "1987-Later"),
    ("1996", "1987-Later"),
    ("1995", "1987-Later"),
    ("1994", "1987-Later"),
    ("1993", "1987-Later"),
    ("1992", "1987-Later"),
    ("1991", "1987-Later"),
    ("1990", "1987-Later"),
    ("1989", "1987-Later"),
    ("1988", "1987-Later"),
    ("1987", "1987-Later"),
    ("1986", "1981-1986"),
    ("1985", "1981-1986"),
    ("1984", "1981-1986"),
    ("1983", "1981-1986"),
    ("1982", "1981-1986"),
    ("1981", "1981-1986"),
]


def GET_ROAD_FNC():
    return ROAD_FNC


def GET_ROAD_FNC_IDS():
    return ROAD_FNC_IDS

UNITTYPE = [
    ("1", "Motor Vehicle In-Transport (Inside or Outside the Trafficway)")
]

HIT_RUN = [
    ("0", "No"),
    ("1", "Yes"),
    ("8", "Not Reported"),
]

REG_STAT = [
    ("0", "Not Applicable"),
    ("1", "Alabama"),
    ("2", "Alaska"),
    ("4", "Arizona"),
    ("5", "Arkansas"),
    ("6", "California"),
    ("8", "Colorado"),
    ("9", "Connecticut"),
    ("10", "Delaware"),
    ("11", "District of Columbia"),
    ("12", "Florida"),
    ("13", "Georgia"),
    ("15", "Hawaii"),
    ("16", "Idaho"),
    ("17", "Illinois"),
    ("18", "Indiana"),
    ("19", "Iowa"),
    ("20", "Kansas"),
    ("21", "Kentucky"),
    ("22", "Louisiana"),
    ("23", "Maine"),
    ("24", "Maryland"),
    ("25", "Massachusetts"),
    ("26", "Michigan"),
    ("27", "Minnesota"),
    ("28", "Mississippi"),
    ("29", "Missouri"),
    ("30", "Montana"),
    ("31", "Nebraska"),
    ("32", "Nevada"),
    ("33", "New Hampshire"),
    ("34", "New Jersey"),
    ("35", "New Mexico"),
    ("36", "New York"),
    ("37", "North Carolina"),
    ("38", "North Dakota"),
    ("39", "Ohio"),
    ("40", "Oklahoma"),
    ("41", "Oregon"),
    ("42", "Pennsylvania"),
    ("43", "Puerto Rico"),
    ("44", "Rhode Island"),
    ("45", "South Carolina"),
    ("46", "South Dakota"),
    ("47", "Tennessee"),
    ("48", "Texas"),
    ("49", "Utah"),
    ("50", "Vermont"),
    ("51", "Virginia"),
    ("52", "Virgin Islands"),
    ("53", "Washington"),
    ("54", "West Virginia"),
    ("55", "Wisconsin"),
    ("56", "Wyoming"),
    ("91", "Not Reported"),
    ("92", "No Registration"),
    ("93", "Multiple State Registrations"),
    ("94", "U.S. Government Tags (Includes Military)"),
    ("95", "Canada"),
    ("96", "Mexico"),
    ("97", "Other Foreign Country"),
    ("98", "Other Registration"),
    ("99", "Unknown/Reported as Unknown (Since 2018)")
]

OWNER = [
    ("0", "Not Applicable, Vehicle Not Registered"),
    ("1", "Driver (in This Crash) Was Registered Owner"),
    ("2", "Driver (in This Crash) Not Registered Owner (Other Private Owner)"),
    ("3", "Vehicle Registered as Commercial/Business/Company/Government Vehicle"),
    ("4", "Vehicle Registered as Rental Vehicle"),
    ("5", "Vehicle Was Stolen (Reported by Police)"),
    ("6", "Driverless/Motor Vehicle Parked/Stopped off Roadway"),
    ("9", "Unknown")
]

VPICBODYCLASS = [
    ("1", "Convertible/Cabriolet"),
    ("2", "Minivan"),
    ("3", "Coupe"),
    ("4", "Low Speed Vehicle (LSV)/Neighborhood Electric Vehicle (NEV)"),
    ("5", "Hatchback/Liftback/Notchback"),
    ("6", "Motorcycle - Standard"),
    ("7", "Sport Utility Vehicle (SUV)/Multi-Purpose Vehicle (MPV)"),
    ("8", "Crossover Utility Vehicle (CUV)"),
    ("9", "Van"),
    ("10", "Roadster"),
    ("11", "Truck"),
    ("12", "Motorcycle - Scooter"),
    ("13", "Sedan/Saloon"),
    ("15", "Wagon"),
    ("16", "Bus"),
    ("60", "Pickup"),
    ("62", "Incomplete - Cutaway*"),
    ("63", "Incomplete - Chassis Cab (Single Cab)*"),
    ("64", "Incomplete - Glider*"),
    ("65", "Incomplete*"),
    ("66", "Truck-Tractor"),
    ("67", "Incomplete - Stripped Chassis*"),
    ("68", "Streetcar/Trolley"),
    ("69", "Off-Road Vehicle - All Terrain Vehicle (ATV) (Motorcycle-Style)"),
    ("70", "Incomplete - Chassis Cab (Double Cab)*"),
    ("71", "Incomplete - School Bus Chassis*"),
    ("72", "Incomplete - Commercial Bus Chassis*"),
    ("73", "Bus - School Bus"),
    ("74", "Incomplete - Chassis Cab (Number of Cab Unknown)*"),
    ("75", "Incomplete - Transit Bus Chassis*"),
    ("76", "Incomplete - Motor Coach Chassis*"),
    ("77", "Incomplete - Shuttle Bus Chassis*"),
    ("78", "Incomplete - Motor Home Chassis*"),
    ("80", "Motorcycle - Sport"),
    ("81", "Motorcycle - Touring/Sport Touring"),
    ("82", "Motorcycle - Cruiser"),
    ("83", "Motorcycle - Trike"),
    ("84", "Off-Road Vehicle - Dirt Bike/Off-Road"),
    ("85", "Motorcycle - Dual Sport/Adventure/Supermoto/On/Off-Road"),
    ("86", "Off-Road Vehicle - Enduro (off-road long-distance racing)"),
    ("87", "Motorcycle - Small/Minibike"),
    ("88", "Off-Road Vehicle - Go Kart"),
    ("90", "Motorcycle - Side Car"),
    ("94", "Motorcycle - Custom"),
    ("95", "Cargo Van"),
    ("97", "Off-Road Vehicle - Snowmobile"),
    ("98", "Motorcycle - Street"),
    ("100", "Motorcycle - Enclosed Three Wheeled/Enclosed Autocycle"),
    ("103", "Motorcycle - Unenclosed Three Wheeled/Open Autocycle"),
    ("104", "Motorcycle - Moped"),
    ("105", "Off-Road Vehicle - Recreational Off-Road Vehicle (ROV)"),
    ("107", "Incomplete - Bus Chassis*"),
    ("108", "Motorhome"),
    ("109", "Motorcycle - Cross Country"),
    ("110", "Motorcycle - Underbone"),
    ("111", "Step Van/Walk-in Van"),
    ("112", "Incomplete - Commercial Chassis*"),
    ("113", "Off-Road Vehicle - Motocross (Off-Road Short-Distance, Closed-Track Racing)"),
    ("114", "Motorcycle - Competition"),
    ("117", "Limousine"),
    ("119", "Sport Utility Truck (SUT)"),
    ("124", "Off-Road Vehicle - Golf Cart"),
    ("125", "Motorcycle - Unknown Body Type"),
    ("126", "Off-Road Vehicle - Farm Equipment"),
    ("127", "Off-Road Vehicle - Construction Equipment"),
    ("996", "Motorized Bicycle (discontinued in 2022)"),
    ("997", "Other"),
    ("998", "Not Reported"),
    ("999", "Unknown")
]

ICFINALBODY = [
    ("0", "Not Applicable"),
    ("2", "Minivan"),
    ("4", "Low-Speed Vehicle (LSV)"),
    ("7", "Sport Utility Vehicle (SUV)/Multi-Purpose Vehicle (MPV)"),
    ("8", "Crossover Utility Vehicle (CUV)"),
    ("9", "Van"),
    ("11", "Truck"),
    ("15", "Wagon"),
    ("16", "Bus"),
    ("60", "Pickup"),
    ("66", "Truck-Tractor"),
    ("68", "Streetcar/Trolley"),
    ("73", "Bus-School Bus"),
    ("95", "Cargo Van"),
    ("108", "Motorhome"),
    ("111", "Step Van/Walk-in Van"),
    ("117", "Limousine"),
    ("119", "Sport Utility Truck"),
    ("128", "Ambulance"),
    ("129", "Street Sweeper"),
    ("130", "Fire Apparatus"),
    ("997", "Other"),
    ("998", "Not Reported"),
    ("999", "Unknown")
]

GVWR = [
    ("0", "No Trailer GVWR Required"),
    ("11", "Class 1: 6,000 lbs or less (2,722 kg or less)"),
    ("12", "Class 2: 6,001 - 10,000 lbs (2,722 - 4,536 kg)"),
    ("13", "Class 3: 10,001 - 14,000 lbs (4,536 - 6,350 kg)"),
    ("14", "Class 4: 14,001 - 16,000 lbs (6,350 - 7,258 kg)"),
    ("15", "Class 5: 16,001 - 19,500 lbs (7,258 - 8,845 kg)"),
    ("16", "Class 6: 19,501 - 26,000 lbs (8,845 - 11,794 kg)"),
    ("17", "Class 7: 26,001 - 33,000 lbs (11,794 - 14,969 kg)"),
    ("18", "Class 8: 33,001 lbs and above (14,969 kg and above)"),
    ("77", "No Trailing Units"),
    ("98", "Not Reported"),
    ("99", "Reported as Unknown")
]

J_KNIFE = [
    ("0", "Not an Articulated Vehicle"),
    ("1", "No"),
    ("2", "Yes, First Event"),
    ("3", "Yes, Subsequent Event")
]

V_CONFIG = [
    ("0", "Not Applicable"),
    ("1", "Single-Unit Truck (2 Axles and GVWR More Than 10,000 lbs)"),
    ("2", "Single-Unit Truck (3 or More Axles)"),
    ("4", "Truck Pulling Trailer(s)"),
    ("5", "Truck Tractor (Bobtail)"),
    ("6", "Truck Tractor/Semi-Trailer"),
    ("7", "Truck Tractor/Double"),
    ("8", "Truck Tractor/Triple"),
    ("10", "Vehicle 10,000 lbs. or Less Placarded for Hazardous Materials"),
    ("19", "Vehicle More Than 10,000 lbs., Other"),
    ("20", "Bus/Large Van (Seats for 9-15 Occupants, Including Driver)"),
    ("21", "Bus (Seats for More Than 15 Occupants, Including Driver, 2010-Later)"),
    ("70", "Light Truck (Van, Mini-Van, Panel, Pickup, Sport Utility Vehicle Displaying a Hazardous Materials Placard)"),
    ("80", "Passenger Car (Only When Displaying a Hazardous Materials Placard)"),
    ("88", "Qualifying Vehicle, Unknown Configuration"),
    ("98", "Not Reported"),
    ("99", "Unknown")
]

CARGO_BT = [
    ("0", "Not Applicable"),
    ("1", "Van/Enclosed Box"),
    ("2", "Cargo Tank"),
    ("3", "Flatbed"),
    ("4", "Dump"),
    ("5", "Concrete Mixer"),
    ("6", "Auto Transporter"),
    ("7", "Garbage/Refuse"),
    ("8", "Grain/Chips/Gravel"),
    ("9", "Pole-Trailer"),
    ("10", "Log (Since 2007)"),
    ("11", "Intermodal Container Chassis"),
    ("12", "Vehicle Towing Another Motor Vehicle (Since 2007)"),
    ("22", "Bus"),
    ("28", "Not Reported (2010-2012)"),
    ("96", "No Cargo Body Type"),
    ("97", "Other"),
    ("98", "Unknown Cargo Body Type"),
    ("99", "Unknown")
]

HAZ_INV = [
    ("1", "No"),
    ("2", "Yes")
]

HAZ_PLAC = [
    ("0", "Not Applicable"),
    ("1", "No"),
    ("2", "Yes"),
    ("8", "Not Reported")
]

HOSPITAL = [
    ("0", "Not Transported for Treatment"),
    ("1", "EMS Air"),
    ("2", "Law Enforcement"),
    ("3", "EMS Unknown Mode"),
    ("4", "Transported Unknown Source"),
    ("5", "EMS Ground"),
    ("6", "Other"),
    ("8", "Not Reported"),
    ("9", "Reported as Unknown")
]
