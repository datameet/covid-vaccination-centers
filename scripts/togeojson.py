import json
import csv

input = csv.DictReader(open('data/raw.csv', 'r'))
fc = {
  'type': 'FeatureCollection',
  'features': []
}

for row in input:
  name = row['name']
  city = row['city']
  district = row['district']
  state = row['state']
  block = row['block']
  nin_pmjay = row['nin_pmjay']
  address = row['address']
  categoryno = row['categoryno']
  categoryname = row['categoryname']
  mobile = row['mobile']
  pincode = int(row['pincode']) if row['pincode'] != '' else None
  coordinates = [float(row['longitude']), float(row['latitude'])]

  feature = {
    'type': 'Feature',
    "properties": {
      'name': name,
      'city': city,
      'district': district,
      'state': state,
      'block': block,
      'nin_pmjay': nin_pmjay,
      'address': address,
      'categoryname': categoryname,
      'categoryno': categoryno,
      'mobile': mobile,
      'pincode': pincode
    },
    'geometry': {
      'type': 'Point',
      'coordinates': coordinates
    }
  }

  fc['features'].append(feature)

print(json.dumps(fc))