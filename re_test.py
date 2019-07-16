#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 15:16:11 2018

@author: ericyang
"""
import re

string1 = "this is a aaa string and that is a bbb string"

pat1 = "a ([\s\S]*?) string"

result1 = re.compile(pat1).findall(string1)
print(result1)