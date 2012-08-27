#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import time
import pdb

from genshi.template import TextTemplate

def templatize():

    infile = sys.argv[1]
    infiledata = open(infile, 'r')

    env = os.environ.copy()
    #print env

    # use lenient mode to prevent errors on missing vars
    tmpl = TextTemplate(infiledata, lookup='lenient')

    # fill in values with env variables
    stream = tmpl.generate(**env)

    # print rendered template
    print stream.render('text')

if __name__ == '__main__':
    templatize()
