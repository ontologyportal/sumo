/* This code is copyrighted by Articulate Software (c) 2004.
It is released underthe GNU Public License <http://www.gnu.org/copyleft/gpl.html>.
Users ofthis code also consent, by use of this code, to credit Teknowledge in any
writings, briefings,publications, presentations, or other representations of any
software which incorporates, builds on, or uses this code.*/


This directory contains knowledge base files written in KIF, and files in WordNet
data file format (see <http://www.cogsci.princeton.edu/~wn/man/wndb.5WN.html>).
Several alternative WordNet mapping files are present.  Note that currently, the
names of the files that Sigma uses are fixed.  The noun mappings are in MergeMappings.txt,
and verbs in WordNetMappings-verbs.txt.  If you use the alternate mappings, you will
need to rename the files.  Adjectives and adverbs are not currently used by Sigma.
Note also that Sigma assumes these files are in the same directory as the knowledge
base files.

There are four alternative sets of mapping files

1.  Original mappings between SUMO and WordNet 1.6

WordNetMappings-adjectives.txt
WordNetMappings-adverbs.txt
WordNetMappings-Top.txt
WordNetMappings-verbs.txt

2.  Mappings to SUMO and MILO (SUMO mapping is overridden if a mapping to MILO exists)

WordNetMappings-adj-MILO.txt
WordNetMappings-nouns-MILO.txt
WordNetMappings-verbs-MILO.txt
WordNetMappings-adv-MILO.txt

3.  WordNet-SUMO mappings automatically updated to WordNet 2.0

WordNetMappings2-adj.txt
WordNetMappings2-adv.txt
WordNetMappings2-nouns.txt
WordNetMappings2-verbs.txt

4.  WordNet-SUMO-MILO mappings automatically updated to WordNet 2.0

WordNetMappings2-adj-MILO.txt
WordNetMappings2-adv-MILO.txt
WordNetMappings2-nouns-MILO.txt
WordNetMappings2-verbs-MILO.txt


This directory also contains a subdirectory called "Translations" which contains the
natural language format files for languages other than English.

