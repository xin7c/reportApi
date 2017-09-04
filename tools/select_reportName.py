#!/usr/bin/env python
# encoding: utf-8

import json
import reportURI

uri = reportURI.uri

print len(uri)
for i,j in enumerate(uri):
    print i+1, j["reportname"]