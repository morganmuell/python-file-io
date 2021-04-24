import re

print('Opening origin.txt')

line_number = 0
inherit_bait_string = r'inherit[a-z]+'
inherit_string = re.compile(inherit_bait_string, re.IGNORECASE)


with open('origin.txt', 'r') as in_stream:
    print('Opening output_origin.txt')

    with open('output_origin.txt', 'w') as out_stream:

        for line in in_stream:
            line = line.strip()
            word_list = line.split()
            matched_words_inherit = list(filter(inherit_string.findall, word_list))
            for word in matched_words_inherit:
                out_stream.write('{0}\t{1}\n'.format(line_number, word))
            line_number += 1


print("done!")
print('origin.txt is closed?', in_stream.closed)
print('output_origin.txt is closed?', out_stream.closed)


