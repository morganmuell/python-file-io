#! /usr/bin/env python3

"A module for searching text files for words"

import sys
import re



def search_text_for_strings(textfile, string):
    """
    Searches a text file for a given search string and writes results to an output file.

    Parameters
    ----------
    textfile: textIO
        The text file to search.

    string: string
            The search string to look for. Can be a regular expression.
            It is best to enter your expression within r'' to use a raw string.
    
    Returns
    -------
    output file
        Output file with hits. One hit per line, listing the line number and the hit.

    Examples
    --------
    >>> search_text_for_strings(origin.txt, r'inherit[a-z]+')
    input file is closed?
    output file is closed?

    >>> search_text_for_strings(origin.txt, r'inheritable')
    input file is closed?
    output file is closed?

    The first example returns all variations on the word heritable, while the second returns only the word heritable.
    """


    line_number = 0
    bait_string = string
    re_string = re.compile(bait_string, re.IGNORECASE)


    with open(textfile, 'r') as in_stream:
        print('Opening' textfile)

        with open('output_search.txt', 'w') as out_stream:

            for line in in_stream:
                line = line.strip()
                word_list = line.split()
                matched_words = list(filter(re_string.findall, word_list))
                for word in matched_words:
                    out_stream.write('{0}\t{1}\n'.format(line_number, word))
                line_number += 1


    print('input file is closed', in_stream.closed)
    print('output file is closed', out_stream.closed)





if __name_+ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(sys.argv[0] + ": Expecting the following command lines in order: text file, search string")

    search_file = search_text_for_strings(textfile, string)

    print('Search complete')
