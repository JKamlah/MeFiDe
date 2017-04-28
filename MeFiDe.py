#          Program to merge, filter and deduplicate textfiles
#WARNING:  The textfile for this program should be an output of an hocr-file
#          through "hocr-tools"-WordFreq
#Program:  **MeFiDe**
#Info:     **Python 2.7**
#Project:  **Aktienführer II**
#Author:   **Jan Kamlah**
#Date:     **28.04.2017**

import os
import re
# Start of the main-function
# Init
# Voc = [^0-9:;.(),-]+
source_typ = 'Voc'
year_start = 1956
year_end = 1978
word_min_len =1
# Iterate over the years
for i in range(year_start, year_end):
    # Open Textfile
    txt_file = open("U:\\Eigene Dokumente\\Aktienfuehrer_Dokumente\\Aktienfuehrer_PostOCR_Format\\%d\\%s_%d.txt" % (i,source_typ,i), 'r')
    # Open outputfile
    output_file = open("U:\\Eigene Dokumente\\Aktienfuehrer_Dokumente\\Aktienfuehrer_PostOCR_Format\\Alle\\%s_MeFiDe_%d_%d.txt" % (source_typ,year_start,year_end), 'a+')
    # Read the Comparelist
    compare_list = list()
    for word in output_file:
        compare_list.append(word)
    # Search in every line of the datafile the given words of the vocabulary
    # All words with numbers or :,.(),- will be ignored
    for line in txt_file:
        if re.search(r"([^0-9:;.(),-]+)", line):
            if re.search(r"([^0-9:;.(),-]+)", line).group(0) == line and len(line) > 2:
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
