### Importing Data files

1. Create new `generation` to import data into

```
python manage.py mapit_generation_create \
   --desc='Adding boundaries' --commit
```
For a fresh project, generation with id 1 will be created

2. Create mapit country, types and code types from a fixture

```
python manage.py loaddata geo/fixture.json
```

3. Then import geojson files as follows

- importing country

```
python manage.py mapit_import --commit \
        --generation_id=1 --country_code=NG --area_type_code=COUNTRY \
        --name_type_code=Binfo --name_field=name \
        --code_type=AFR --code_fiel=afr_geoid
        geo/Nigeria/country.geojson
```

- importing state

```
python manage.py mapit_import --commit \
        --generation_id=1 --country_code=NG --area_type_code=STATE \
        --name_type_code=Binfo --name_field=name \
        --code_type=AFR --code_fiel=afr_geoid
        geo/Nigeria/state.geojson
```

4. Once you finish importing all geojsons file, you can now activate generation with the following command:

```
 python manage.py mapit_generation_activate --commit

```