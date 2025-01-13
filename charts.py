import data
import processing
import csv


def vaccineData(): 
  VacRead = data.read_values("saved_data.csv")
  header = []
  with open("saved_data.csv") as f:
    reader = csv.reader(f)
    header = next(reader)
  vaccine_dict = data.dic_list_gen(header, VacRead)
  return vaccine_dict

# Bar Chart
def BarChartData():
  VacRead = vaccineData()
  highest_dates = processing.max_value(VacRead, "date")
  updated_vac_info = processing.copy_matching(VacRead, "date", highest_dates)
  return updated_vac_info  


def PieChartData():
  vaccines = ["administered_janssen", "administered_moderna", "administered_pfizer", "administered_unk_manuf"]
  # Get the dictionaries with the highest dates
  max_dates = BarChartData()
  sums = [0,0,0,0] 
  for dicts in max_dates:
    str_to_float = data.make_values_numeric(vaccines, dicts)
    # Get the sum of all of the administered vaccines
    sums[0] += dicts["administered_janssen"]
    sums[1] += dicts["administered_moderna"]
    sums[2] += dicts["administered_pfizer"]
    sums[3] += dicts["administered_unk_manuf"]
  result = {"Jansen": sums[0], "Moderna": sums[1], "Pfizer": sums[2], "Other": sums[3]}
  return result

#Line graph
def sort_by_date(dicts):
  return dicts["date"]

def LineGraphData(location):
  VacRead = vaccineData()
  Vac_Date = []
  for dicts in VacRead:
    if location['location'] == dicts['location']:
      Vac_Date.append(dicts)
  Vac_Date.sort(key=sort_by_date)
  return Vac_Date
