def max_value(data , value):
  empty = ""
  for dicts in data:
    if (dicts[value]) > empty :
      empty = dicts[value]
  return empty 

def init_dictionary (data, value):
  empty = {}
  for dicts in data:
    if value in dicts :
      var= dicts[value]
      empty[var] = 0
  return empty
#print(init_dictionary([{'date': '2021-05-02T00:00:00.000','location': 'FL', 'local': 'Florida', 'administered_janssen': 555456, 'administered_moderna': 6733913, 'administered_pfizer': 8177075, 'administered_unk_manuf': 25210, 'series_complete_pop_pct': '29.9'},{'date': '2021-07-02T00:00:00.000','location': 'MI', 'local': 'Florida', 'administered_janssen': 0, 'administered_moderna': 475593, 'administered_pfizer': 883331, 'administered_unk_manuf': 0, 'series_complete_pop_pct': '0'}], 'location')) 

def sum_matches (lod, k, v, tgt):
  empty= 0
  for dicts in lod:
    k_value = dicts[k] 
    if k_value == v:
      empty += dicts[tgt]
  return empty 


#print(sum_matches([{'date': '2021-05-02T00:00:00.000','location': 'FL', 'local': 'Florida', 'administered_janssen': 555456, 'administered_moderna': 6733913, 'administered_pfizer': 8177075, 'administered_unk_manuf': 25210, 'series_complete_pop_pct': '29.9'},{'date': '2021-07-02T00:00:00.000','location': 'MI', 'local': 'Florida', 'administered_janssen': 0, 'administered_moderna': 475593, 'administered_pfizer': 883331, 'administered_unk_manuf': 0, 'series_complete_pop_pct': '0'}], 'location', 'MI', 'administered_moderna'))

def copy_matching (lod, k, v):
  empty= []
  for dicts in lod:
    k_value = dicts[k] 
    if k_value == v:
      empty.append(dicts) 
  return empty

#print(copy_matching([{'date': '2021-05-02T00:00:00.000','location': 'MI', 'local': 'Florida', 'administered_janssen': 555456, 'administered_moderna': 6733913, 'administered_pfizer': 8177075, 'administered_unk_manuf': 25210, 'series_complete_pop_pct': '29.9'},{'date': '2021-07-02T00:00:00.000','location': 'MI', 'local': 'Florida', 'administered_janssen': 0, 'administered_moderna': 475593, 'administered_pfizer': 883331, 'administered_unk_manuf': 0, 'series_complete_pop_pct': '0'}], 'location', 'MI'))
