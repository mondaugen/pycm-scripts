#!/usr/bin/env python
__doc__ = '''
Creates a rhythm of notes or rests
args are: contourmaker.py <depth> <num_sections> <number_of_divisions>
num_sections must be less than or equal to number of divisions
'''
import form_trees
import sys
from vhtrees import *
from formgenerator import *
from fractions import *
from sectionfiller import *
import random
from cmrandom import *
import argparse
import formfiller

__doc__ = "\
generate a form file which is just a list of strings separated by newlines,\
some of which are the same."

parser = argparse.ArgumentParser(\
	description=__doc__)

__depth_help__ = 'How deep the form tree grows.'
parser.add_argument('--depth', dest='depth', nargs='?',\
	const=2, default=2, help=__depth_help__, type=int)

__nsections_help__ = 'The number of distinct sections at a given layer of the\
tree.'

parser.add_argument('--nsections', dest='nsections', nargs='?',\
	const=1, default=1, help=__nsections_help__, type=int)

__rest_prob_help__ = 'see source'
#__rest_prob_help__ = '\
#A number between 0 and 1 dictating the probability that a note will be a rest.\
#So 0.1 means a 10% chance of being a rest.'

parser.add_argument('--rest-prob', dest='restprob', nargs='?',\
	const=0.0, default=0.0, help=__rest_prob_help__, type=float)

args = parser.parse_args()

def lenfun(aux):
    return Fraction(random.randint(1,resolution),resolution)

def datumfunc(aux):
    if random.random() < restprob:
	return 'rest'
    else:
	return 'note'

if formfile == None:
    f = sys.stdin
else:
    f = open(formfile, 'r')

lines = f.readlines()

for i in xrange(len(lines)):
    lines[i] = lines[i].strip()


random.seed()

sf = SectionFiller(lenfun, datumfunc)

seqdict = formfiller.make_sequence_dict(lines, sf)

for s in seqary:
    for l, d in seqdict[s]:
	print str(l)+',', d

