import requests
import json
import xmltodict

#Gets the information from Tenable website
#data = requests.get('https://tenable.com/plugins/newest')

#Tenable page for newest RSS feed
response = requests.get('https://www.tenable.com/plugins/feeds?sort=newest&type=nessus')
#Saves it to an XML file?
#with open('TenableNewPlugins.xml', 'w', encoding="utf-8") as xmlFile:
#    xmlFile.write(request.text)

#Parse response.text and convert it to json
jsonData = xmltodict.parse(response.text)

#Saves it to a JSON file
with open('JSONTenbleNewPlugin.json', 'w') as jsonFile:
    jsonFile = json.dump(jsonData, jsonFile, indent=4)