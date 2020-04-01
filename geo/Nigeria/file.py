
import json

with open('subcounty.geojson') as f:
  data = json.load(f)

# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
features = data['features']

for feature in features:
        code = feature['properties']['code']
        afr_geoid = "level2-KE_2_" + code.replace("KE", '', 1)
        if "KE00" in code:
          geoid = "subcounty-" + code.replace("KE00", '', 1)
        else:
          geoid = "subcounty-" + code.replace("KE0", '', 1)

        feature['properties']['geoid'] = geoid
        feature['properties']['afr_geoid'] = afr_geoid

# Serializing json  
json_object = json.dumps(data, indent = 4) 
  
# Writing to sample.json 
with open("sample.json", "w") as outfile: 
    outfile.write(json_object) 



