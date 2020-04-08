
import json
import csv

with open('Morocco/district.geojson') as f:
  data = json.load(f)

features = data['features']

# with open('morocco.csv', mode='a+') as geofile:
#   geowriter = csv.writer(geofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#   geolevel = "level3"
#   parentlevel = "level2"

#   for feature in features:
#     prop = feature['properties']

#     code = prop["ID_3"]
#     geocode = "MA_3_00"
#     if int(code) >= 100:
#       geocode = geocode + str(code)
#     elif int(code) >= 10:
#       geocode = geocode + "0" + str(code)
#     else:
#       geocode = geocode + "00" + str(code)

#     parentcode = prop["ID_2"]
#     parentgeocode =  "MA_2_00"
#     if int(parentcode) >= 10:
#       parentgeocode = parentgeocode + str(parentcode)
#     else:
#       parentgeocode = parentgeocode + "0" + str(parentcode)

       
#     geowriter.writerow([geolevel, geocode, parentlevel, parentgeocode, "2009", prop["name"].encode('utf-8').strip(), prop["name"].encode('utf-8').strip(), ""])
 
with open('countrygeoid.csv', mode='a+') as geo_file:
  geo_writer = csv.writer(geo_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

  for feature in features:
    prop = feature['properties']
    code = prop["ID_3"]
    geoid = "district-" + str(code)
    # geoid = prop["geoid"]
    afr_geoid = "level3-MA_3_00"

    if int(code) >= 100:
      afr_geoid = afr_geoid  + str(code)
    # elif int(prop["code"]) >= 100:
    #   afr_geoid = afr_geoid + str(prop["code"])
    elif int(code) >= 10:
      afr_geoid = afr_geoid + "0"+ str(code)
    else:
      afr_geoid =afr_geoid + "00" + str(code)

    prop["afr_geoid"] = afr_geoid
    prop["geoid"] = geoid

    # afr_geoid = prop["afr_geoid"]
    # geoid = "municipality-" + str(int(afr_geoid[13:]))
    # prop["geoid"] = geoid

    geo_writer.writerow([prop['afr_geoid'], 'MAR', prop['geoid'], prop['name'].encode('utf-8').strip()])

#Serializing json  
json_object = json.dumps(data) 
  
# Writing to sample.json 
with open("sample.json", "w") as outfile: 
    outfile.write(json_object) 
