#!/usr/bin/python
import sys                                                                                                                                      
import json      
import urllib2
#print('START')                                                                                                
if len(sys.argv) == 1:                                                                                                                                                         
    try:
      req = urllib2.Request('http://127.0.0.1:5984/_all_dbs')                                
      stats_json = urllib2.urlopen(req)                                                    
      #print('TRY')
    except urllib2.URLError, e:                                                                                                                     
      print e.reason
      exit(1)
    
    dbs_res = json.load(stats_json)
    dbs = []
    for x in range(0, len(dbs_res)):
      #print(dbs_res[x])
      dbs.append(dbs_res[x])
    result_dbs = []

    for t in dbs:
      result_dbs.append({"{#SNAME}": str(t)})
    dbs_items = dict(data=result_dbs)
    print(json.dumps(dbs_items))
