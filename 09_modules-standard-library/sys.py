#!/usr/bin/env python

import re

#print re.search('a', 'apple').group()
#print re.search('a(.*)e', 'apple').group(1)

print re.findall('\w+@\w+\.com','bumjin@gmail.com and neobumjin@naver.com')
