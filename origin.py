print('Opening origin.txt')
with open('origin.txt', 'r') as in_stream:
    print('Opening output_origin.txt')
    with open('output_origin.txt', 'w') as out_stream:
        for line in in_stream:
            #variable for line number
            #parse apart words for that line (with line.strip() and line.split ()?)
            #search for the related words
            #store search results of words into another variable, separated by a comma and space
            for word in word_list:
                out_stream.write('{0}\n'.format(word))
                #also write the line number first

print("done!")
print('origin.txt is closed?', in_stream.closed)
print('output_origin.txt is closed?', out.stream.closed)

#search for the words in the line
#output line number and the word
#need variable for line number

