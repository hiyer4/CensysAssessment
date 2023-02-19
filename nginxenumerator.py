from censys.search import CensysHosts
import re
import json

h = CensysHosts()

#search expression filters for HTTP service and nginx software
query = h.search("services.service_name: HTTP and services.software.product=nginx and services.software.version=*", per_page=25,pages=25)

#do regex expression on hostData to extract each version and add to list
hostData=str(query.view_all())
cpeList=re.findall('cpe:2.3:a:nginx:nginx:\*?[0-9]?\.?[0-9]?[0-9]?\.?[0-9]?',hostData)
    
serviceDictionary={}

#traverse list of cpe and make count of each distinct cpe version
for cpe in cpeList:
    if cpe in serviceDictionary.keys():
        serviceDictionary[cpe]+=1
    else:
            
        serviceDictionary[cpe]=1

#write dictionary to file
with open('FinalReport.txt', 'w') as convert_file:
     convert_file.write(json.dumps(serviceDictionary))

print(serviceDictionary)
