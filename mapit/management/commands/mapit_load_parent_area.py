# This script is for a one off import of all the old ONS codes to a MapIt
# containing only the new ones from a modern Boundary-Line.

import codecs
import csv
import os.path
import sys
from django.core.management.base import BaseCommand
from mapit.models import Area

python_version = sys.version_info[0]


def open_csv(filename):
    if python_version < 3:
        o = open(filename)
    else:
        o = codecs.open(filename, 'r', 'utf-8')
    mapping = csv.reader(o)
    next(mapping)
    return mapping


def process(area_code, parent_area_code):
    parent = None
    try:
        area = Area.objects.get(codes__code=area_code, codes__type__code='AFR')
    except Area.DoesNotExist:
        # An area that existed at the time of the mapping, but no longer
        return

    try:
        parent = Area.objects.get(codes__code=parent_area_code, codes__type__code='AFR')
    except Area.DoesNotExist:
        # parent_area does not exist
        pass

    if not parent:
        raise Exception("Area %s does not have a parent?" % (self.pp_area(area)))
    if area.parent_area != parent:
        self.stdout.write("Parent for %s was %s, is now %s" % (
            self.pp_area(area), self.pp_area(area.parent_area), self.pp_area(parent)))

        area.parent_area = parent
        area.save()

def pp_area(self, area):
        if not area:
            return "None"
        return "%s [%d] (%s)" % (area.name, area.id, area.type.code)

class Command(BaseCommand):
    help = 'Load parent area'

    def handle(self, **options):
        for row in open_csv(os.path.join('geo/geos_parent_map.csv')):
            area_code = row[0]
            parent_area_code = row[1]

            process(area_code, parent_area_code)
