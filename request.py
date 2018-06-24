#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 22:38:20 2018

@author: avinash
"""
import os

os.system('wget http://a4b98168d77b511e89eda023269ecb80-258532036.us-east-2.elb.amazonaws.com:8088/graph')
os.system('mv graph graph.json')

import json
json_file = open('graph.json')
json_str = json_file.read()
json_data = json.loads(json_str)
edge = json_data['edges']

        
for a in edge:
    if a['source']=='istio-ingressgateway.istio-system (unknown)' and a['target']=='productpage.default (v1)':
        t_sent_pp = float(a['labels']['reqs/sec'])
    if a['source']== 'productpage.default (v1)' and a['target']=='details.default (v1)':
        t_sent_deatils = float(a['labels']['reqs/sec'])
    if a['source']== 'productpage.default (v1)' and a['target']=='reviews.default (v1)':
        t_sent_review1 = float(a['labels']['reqs/sec'])
    if a['source']== 'productpage.default (v1)' and a['target']=='reviews.default (v2)':
        t_sent_review2 = float(a['labels']['reqs/sec'])
    if a['source']== 'productpage.default (v1)' and a['target']=='reviews.default (v3)':
        t_sent_review3 = float(a['labels']['reqs/sec'])
    if a['source']== 'reviews.default (v2)' and a['target']=='ratings.default (v1)':
        t_sent_rating2 = float(a['labels']['reqs/sec'])
    if a['source']== 'reviews.default (v3)' and a['target']=='ratings.default (v1)':
        t_sent_rating3 = float(a['labels']['reqs/sec'])
    
if round(t_sent_pp,3)==round(t_sent_deatils,3):
    print("No request loss btw pp and deatils")
else:
    print("Request loss btw pp and deatils")
if round(t_sent_pp,3)== round(t_sent_review1,3) + round(t_sent_review2,3) + round(t_sent_review3,3):
        print("No request loss btw pp and reviews")
else:
    print("Request loss btw pp and reviews")
    
print("request from rev2 to ratings" + str(t_sent_rating2) )
print("request from rev3 to ratings" + str(t_sent_rating3) )


