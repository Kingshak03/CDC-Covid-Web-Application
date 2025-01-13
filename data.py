#part2
import csv
def dic_list_gen(list1, list2):
  list3 = []
  
  for value in list2:
    dict = {}
    for key in range  (len(list1)):
      dict.update({list1[key]: value[key]})
    list3.append(dict)
      
     
  return list3


def read_values(filename):
  with open(filename) as f:
    list = []
    reader = csv.reader(f)
    next(reader)
    for row in reader:
      list.append(row)
    return list



def make_lists(keys,lists):
  list = []
  for lst in lists:
    list2 =[]
    for key in keys:
      if (key in lst):
          list2.append(lst[key])
    list.append(list2)
  return list
 


def write_values(filename, lists):
  with open(filename,"a") as f:
    writer = csv.writer(f)
    for item in lists:
      writer.writerow(item)
     


#part3

import json 
import urllib.request
def json_loader(url):
 response = urllib.request.urlopen(url)
 content = response.read().decode()
 value = json.loads(content)
 return value
  
  

def make_values_numeric(keys,dictionary):
  for k in keys:
    for key in dictionary:
      if(key == k):
        dictionary.update({key:float(dictionary[key])})
     
  return dictionary



import csv
def save_data(keys,lists,filename):
  list = []
  for lst in lists:
    list2 =[]
    for key in keys:
      if (key in lst):
        list2.append(lst[key])
    list.append(list2)

  
        
  
 
 

    
  with open(filename, "w") as f:
    
    writer = csv.writer(f)
    writer.writerow(keys)
    for item in list:
      writer.writerow(item)




def load_data(filename):
  list = []
  list1= []
  list2 = []
  list3 = []
  with open(filename) as f:
    reader = csv.reader(f)
    header = next(reader)
    for item in reader:
      list2.append(item)
  
  list.append(header)
  for keys in list:
    for key in keys:
      list1.append(key)
  
  for value in list2:
    dict = {}
    for key in range  (len(list1)):
      dict.update({list1[key]: value[key]})
    list3.append(dict)
  return list3
      

