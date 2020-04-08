# This script is for a one off import of all the old ONS codes to a MapIt
# containing only the new ones from a modern Boundary-Line.

import codecs
import csv
import os.path
import sys
from django.core.management.base import BaseCommand
from mapit.models import Area, CodeType
from psycopg2 import IntegrityError

python_version = sys.version_info[0]


def open_csv(filename):
    if python_version < 3:
        o = open(filename)
    else:
        o = codecs.open(filename, 'r', 'utf-8')
    mapping = csv.reader(o)
    next(mapping)
    return mapping


def process(afr_code, c_code, c_codetype):
    try:
        area = Area.objects.get(codes__code=afr_code, codes__type__code='AFR')
    except Area.DoesNotExist:
        # An area that existed at the time of the mapping, but no longer
        return

    # Check if already has the right code
    if c_codetype in area.all_codes and area.all_codes[c_codetype] == c_code:
        return

    try:
        area.codes.create(type=CodeType.objects.get(code=c_codetype), code=c_code)
    except IntegrityError:
        raise Exception("Key already exists for %s, can't give it %s" % (area, c_code))


class Command(BaseCommand):
    help = 'Inserts country specific codes into mapit'

    def handle(self, **options):
        for row in open_csv(os.path.join('geo/countrygeoid.csv')):
            afr_code, c_codetype, c_code = row[0], row[1], row[2]
            process(afr_code, c_code, c_codetype)
