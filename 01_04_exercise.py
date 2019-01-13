import requests
import collections

#Problem description
#Find out if there are any duplicate urls used in the
#json placeholder photo data

url = 'https://jsonplaceholder.typicode.com/photos'

#get the data about the photos
response = requests.get(url)

#read that data into a variable
json_data = response.json()

url_list = dict()
for photo in json_data:
    url_list["id_" + str(photo["id"])] = photo["url"]

#print(url_list)

value_occurrences = collections.Counter(url_list.values())

#print(len(value_occurrences))

filtered_dict = {key: value for key, value in url_list.items()
                 if value_occurrences[value] > 1}

print(len(filtered_dict))