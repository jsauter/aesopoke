import urllib2
content = urllib2.urlopen("http://ets.aeso.ca/ets_web/ip/Market/Reports/SMPriceReportServlet?contentType=html").read()
print content