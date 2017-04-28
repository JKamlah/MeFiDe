#Program Merge Filter Deduplicate Textfiles
#WARNING: The textfile for this program should be an output of an hocr-file
#         through "hocr-tools"-WordFreq
#Program:  **MeFiDe**
#Info:     **Python 2.7**
#Project:  **Aktienführer II**
#Author:   **Jan Kamlah**
#Date:     **26.04.2017**

import os
import re
# Start of the main-function
# Iterate over the years
# Init
voc_typ = 'Voc'
year_start = 1956
year_end = 1978
word_min_len =1
for i in range(year_start, year_end):
    # Textfile
    txt_file = open("U:\\Eigene Dokumente\\Aktienfuehrer_Dokumente\\Aktienfuehrer_PostOCR_Format\\%d\\%s_%d.txt" % (i,voc_typ,i), 'r')
    # Open outputfile
    output_file = open("U:\\Eigene Dokumente\\Aktienfuehrer_Dokumente\\Aktienfuehrer_PostOCR_Format\\%s_MeFiDe_%d_%d.txt" % (voc_typ,year_start,year_end), 'a+')
    # Read the Comparelist
    compare_list = list()
    for word in output_file:
        compare_list.append(word)
    # Search in every line of the datafile the given words of the vocabulary
    for line in txt_file:
        if re.search(r"([^0-9:;.(),-]+)", line):
            if re.search(r"([^0-9:;.(),-]+)", line).group(0) == line:
                if len(line) > 2:
                    if not compare_list:
                        output_file.write(line)
                    else:
                        for word in compare_list:
                            if line == word:
                                break
                            if word == compare_list[-1]:
                                output_file.write(line)
    output_file.close()
    txt_file.close()
