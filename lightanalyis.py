from censys.search import SearchClient

c = SearchClient()

#aggregate data to show number of nginx servers with HTTP/HTTPS
httpreport = c.v2.hosts.aggregate(
    "services.software.product: nginx",
    "services.extended_service_name",
    num_buckets=2,
)

#aggregate data to show number of nginx servers hosted using different ports
portreport = c.v2.hosts.aggregate(
    "services.software.product: nginx",
    "services.port",
    num_buckets=5,
)

print(httpreport)
print(portreport)
