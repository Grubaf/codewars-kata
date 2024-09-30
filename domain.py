import re

def domain_name(url):
    return re.sub(r'\.[A-Za-z\./]+$', '', re.sub(r'(^[A-Za-z]+://)?(www\.)?', '', url))
