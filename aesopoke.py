import urllib2
from lxml import etree

content = urllib2.urlopen("http://ets.aeso.ca/ets_web/ip/Market/Reports/SMPriceReportServlet?contentType=html").read()

table = etree.HTML(s).find("body/table")
rows = iter(table)
headers = [col.text for col in next(rows)]
for row in rows:
    values = [col.text for col in row]
    print dict(zip(headers, values))