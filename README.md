# CensysAssessment

NginxEnumerator


This is a tool that uses Censys to scrape and filter for hosts with http services and Nginx software installed. 
The tool uses regular expression to parse out the services.software.uniform_resource_identifier or the CPE 
(common platform enumeration) in order to extract the version of Nginx installed. A final report in the format
of a dictionary is returned with the count of each distinct version using a sample size of hosts. 


Usage is as follows:

#python3 nginxenumerator.py



LightAnalysis


This is a tool that performs analaysis by aggregating hosts running nginx software and divides the hosts into
two buckets (HTTP and HTTPS). The tool also divides the hosts into 5 buckers to differentiate the ports running
the nginx software. 
