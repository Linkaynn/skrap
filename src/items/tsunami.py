import scrapy

YEAR_INDEX = 0
DATE_INDEX = 1
TIME_INDEX = 2
LATITUDE_INDEX = 3
LONGITUDE_INDEX = 4
DEPTH_INDEX = 5
SURFACE_WAVE_MAGNITUDE_INDEX = 6
ABE_MAGNITUDE_INDEX = 8
INTENSITY_INDEX = 9
MAX_HEIGHT_INDEX = 10
MOMENT_MAGNITUDE_INDEX = 11
AVAILABLE_OBSERVATIONS_INDEX = 12
DAMAGE_CODE_INDEX = 13
CAUSE_INDEX = 14
VALIDITY_INDEX = 15
WARNING_STATUS_INDEX = 16
REGION_CODE_INDEX = 17
BASIC_REFERENCE_INDEX = 18
SOURCE_REGION_INDEX = 19

COLUMN_NAMES = [
    'year',
    'date',
    'time',
    'latitude',
    'longitude',
    'depth',
    'surface_wave_magnitude',
    'abe_magnitude',
    'intensity',
    'max_height',
    'moment_magnitude',
    'available_observations',
    'damage_code',
    'cause',
    'validity',
    'warning_status',
    'region_code',
    'basic_reference',
    'source_region'
]

class Tsunami(object):

    def __init__(self, row):
        self.year = self.extract(row[YEAR_INDEX])
        self.date = self.extract(row[DATE_INDEX])

        # Time is in GMT timezone
        self.time = self.extract(row[TIME_INDEX])

        self.latitude = self.extract(row[LATITUDE_INDEX])  # Latitude in ('-' for southern latitude)
        self.longitude = self.extract(row[LONGITUDE_INDEX])  # Longitude ('-' for western longitude)

        self.depth = self.extract(row[DEPTH_INDEX])  # Depth in the source coordinates in km

        self.surface_wave_magnitude = self.extract(row[SURFACE_WAVE_MAGNITUDE_INDEX])
        self.abe_magnitude = self.extract(row[ABE_MAGNITUDE_INDEX])  # Abe's tsunami magnitude

        self.intensity = self.extract(row[INTENSITY_INDEX])  # Tsunami intensity on Soloviev scale

        self.max_height = self.extract(row[MAX_HEIGHT_INDEX])  # Maximum observed or measured wave height in meters

        self.moment_magnitude = self.extract(row[MOMENT_MAGNITUDE_INDEX])
        self.available_observations = self.extract(row[AVAILABLE_OBSERVATIONS_INDEX],
                                                   0)  # Total number of available run-up and tide-gauge observations

        # N - nondamaging
        # S - slight damage
        # M - moderate damage
        # L - large(severe) damage
        self.damage_code = self.extract(row[DAMAGE_CODE_INDEX], 0)

        # T – tectonic
        # V – volcanic
        # L – landslide
        # M – meteorological
        # S – seiches
        # E – explosion
        # I – impact
        # U – unknown
        self.cause = self.extract(row[CAUSE_INDEX], 'U')

        # 4 - definite tsunami (probability near 1.0)
        # 3 - probable tsunami (probability approximately. 0.75)
        # 2 - questionable tsunami (probability approximately. 0.50)
        # 1 - very doubtful tsunami (probability approximately. 0.25)
        # 0 - false entry (probability near. 0.00) [0]
        self.validity = self.extract(row[VALIDITY_INDEX])

        # noW - no warning was issued (missed tsunami) [5]
        # PTW - Pacific-wide Tsunami Warning issued by PTWC [4]
        # RTW - Regional Tsunami Warning issued by PTWC for areas having no TWS [3]
        # LTW - Local Tsunami Warning issued by regional or national TWC [2]
        # TIB - Tsunami Information or Attention Bulletin issued by any agency [1]
        # N/A - status unknown [0]
        self.warning_status = self.extract(row[WARNING_STATUS_INDEX])

        # Alaska and US Pacific coast (35°N - 63°N, 167°E - 112°W)
        # CAM - Central America (7° N - 35° N, 127° W - 75° W)
        # SAM - South America (58° S - 7° N, 100° W - 60° W)
        # NZT - New Zealand and Tonga (57° S - 11° S, 160° E - 166° W)
        # NGS - New Guinea and Solomon Is. (11° S - 5° N, 130° E - 165° E)
        # IND – Indonesia (11° S - 11°N, 92° E - 130° E)
        # PHI – Philippines (5° N - 28° N, 104° E - 134° E)
        # JAP – Japan (21° N - 48° N, 114° E - 156° E)
        # K-K - Kuril-Kamchatka (40° N - 63° N, 131° E - 167° E)
        # HAW – Hawaii (15° N - 35° N, 171° E - 145° W)
        # INO - Indian Ocean
        # NOA - Northern Atlantic
        # NEA - Northeast Atlantic
        # NWA - Northwest Atlantic
        # SEA - Southeast Atlantic
        # SWA - Southwest Atlantic
        # CAR - Caribbean
        # MED - Mediterranean
        # EMD - Eastern Mediterranean
        # CMD - Central Mediterranean
        # WMD - Western Mediterranean
        # BLA - Black Sea
        # CAS - Caspian Sea
        # NRT - North Sea
        # NRW - Norwegian Sea
        # BAL - Baltic Sea
        self.region_code = self.extract(row[REGION_CODE_INDEX])

        self.basic_reference = self.extract(row[BASIC_REFERENCE_INDEX])  # It refers the tsunami catalog or primary publication where this event is described

        self.source_region = self.extract(row[SOURCE_REGION_INDEX])  # Descriptive indication of the tsunami source area (maximum 24positions)

    def extract(self, param, default="N/A"):
        value = param.extract()
        return default if "<td" in value else value
