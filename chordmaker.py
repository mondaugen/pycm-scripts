#!/usr/bin/env python
__doc__ = '''
Generates some chords of the size described below
args are: contourmaker.py <depth> <num_sections> <number_of_divisions>
<resolution> <num_notes_in_chord> <note_offset>
num_sections must be less than or equal to number of divisions
Chords are chosen from the chromatic scale for now
'''
import form_trees
import sys
from vhtrees import *
from formgenerator import *
from fractions import *
from sectionfiller import *
import random
from cmrandom import *

if len(sys.argv) != 7:
    sys.stderr.write(__doc__)
    exit()

depth = int(sys.argv[1])
numsections = int(sys.argv[2])
number_of_divisions = int(sys.argv[3])
resolution = int(sys.argv[4])
num_notes_in_chord = int(sys.argv[5])
note_offset = int(sys.argv[6])

if numsections > number_of_divisions:
    sys.stderr.write("numsections must be less than number of divisions\n")
    exit()

def temp_form_gen(depth, minlen,node):
    formfreqs = n_randoms_that_sum_to_k(numsections,minlen)
    return generate_random_form_from_frequencies(formfreqs)

def another_vert_generator(depth,node):
    column = []
    for i in xrange(1):
	column.append(Sequential(chr(ord('A') + i)))
    return column

def temp_len_gen(depth,node):
    return number_of_divisions

def lenfun(aux):
    return Fraction(random.randint(1,resolution),resolution)

def datumfunc(aux):
    return random.sample(xrange(note_offset+0,note_offset+12), num_notes_in_chord)

tree = Simultaneous('a')

tree.grow_vh_tree_w_lengths(depth, temp_form_gen, another_vert_generator, temp_len_gen)

seqary = []
curlen = Fraction(0)
tree.fill_w_seq(seqary, curlen)

for i in xrange(len(seqary)):
    t, l, d = seqary[i]
    seqary[i] = d

seqdict = dict()

random.seed()

sf = SectionFiller(lenfun, datumfunc)

for s in set(seqary):
    seqdict[s] = sf.get_list_of_data()

for s in seqary:
    for l, d in seqdict[s]:
	print str(l)+',',
	for c in d:
	    print str(c),
	print

