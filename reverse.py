#!/usr/bin/env python

import sys
import re

word_re = re.compile(r'(\w+)')

mappings = {}
for (male, female) in (
    ('he', 'she'),
    ('his', 'her'),
    ('him', 'her'),   # tough one
    ('man', 'woman'),
    ('men', 'women'),
    ('guy', 'girl'),
    ('guys', 'girls'),
    ('himself', 'herself'),
    ('husband', 'wife'),
    ('husbands', 'wives'),
    ('boyfriend', 'girlfriend'),
    ('boyfriends', 'girlfriends'),
):
    mappings[male] = female
    mappings[male.title()] = female.title()
    mappings[male.upper()] = female.upper()
    mappings[female] = male
    mappings[female.title()] = male.title()
    mappings[female.upper()] = male.upper()


content = open(sys.argv[1]).read()
words = word_re.split(content)
for word in words:
    other = mappings.get(word, word)
    sys.stdout.write(other)
