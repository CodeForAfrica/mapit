import json

from mapit.models import Area


def split_geo_file(filename):
    """
    dump wazimap.geography table for a specific app and use that file to create
    a child_parent_dict
    {"ward-46": "district-4"}
    :param filename:
    :return:
    """
    f = open(filename, 'r')
    geos = json.load(f)
    child_parent_map = {}
    for i in geos:
        fields = i.get("fields")
        current_code = '{}-{}'.format(fields.get('geo_level'), fields.get('geo_code'))
        if fields.get('parent_code') and fields.get('parent_level'):
            parent_code = '{}-{}'.format(fields.get('parent_level'), fields.get('parent_code'))
            child_parent_map[current_code] = parent_code

    return child_parent_map


def get_code_area_id(country):
    """
    [{'ward-43': 3231}, ..... ]
    :param country:
    :return:
    """
    code_area_id = {}
    for area in Area.objects.filter(country__name=country, parent_area__isnull=True):
        codes = [code.code for code in area.codes.select_related('type')]
        cod = str(codes[0])
        code_area_id[cod] = area.id

    return code_area_id


def load_code_area_map(filename):
    """
    instead of querying the areas from prod DB, I dumped the code_area_id_map into
    json from the local db and load them instead of querying the remote
    :param filename:
    :return:
    """
    f = open(filename, 'r')
    return json.load(f)


def replace_parent_id(child_parent_map, code_area_id_map):
    for i in code_area_id_map.keys():
        parent = child_parent_map.get(i)
        if parent:
            parent_id = code_area_id_map.get(parent)
            if parent_id:
                print parent_id
                area_id = code_area_id_map.get(i)
                area = Area.objects.get(id=area_id)
                print area
                area.parent_area_id = parent_id
                area.save()


if __name__ == '__main__':
    child_parent_map = split_geo_file('/Users/ahereza/geo_ug.json')
    code_area_id_map = get_code_area_id('Uganda')
    code_area_id_map = load_code_area_map('ug_area_id.json')
    replace_parent_id(child_parent_map, code_area_id_map)

    # TZ

    child_parent_map = split_geo_file('/Users/ahereza/geo_tz.json')
    code_area_id_map = get_code_area_id('Tanzania')
    code_area_id_map = load_code_area_map('tz_rem_area.json')
    replace_parent_id(child_parent_map, code_area_id_map)





