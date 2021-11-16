from pandas.core.frame import DataFrame
import requests
import json
import xmltodict
import pandas as pd

#Tenable page for newest RSS feed
response = requests.get('https://api.msrc.microsoft.com/cvrf/v2.0/updates')
#creates dictionary from XML
dictObj = json.loads(response.text)

#Writes to outfile for testing
with open("MicrosoftUpdates.json", 'w') as jsonFile:
    json.dump(dictObj, jsonFile, indent=1)

#normalizes with pandas for data under 'value'
df = pd.json_normalize(dictObj, 'value')
#here is where you can manipulate the dataframe
# i.e print(df.tail(20))



# DOES NOT WORK YET!! puts most recent 20 to json file
#with open("JSONmostRecentSecurityUpdates.json", 'w') as tailFile:
#    json.dump(, tailFile)

    
