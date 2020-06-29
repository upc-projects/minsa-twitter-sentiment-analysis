from xml.etree import ElementTree
import os
import csv


def write_to_csv(csvwriter, tree):
    '''
    Function to write data from the xml to the csv file
    '''
    #Get root from xml
    root = tree.getroot()

    #Iterate beetween tweets in the xml
    for tweet in root.findall('tweet'):
        data = []
        data.append(tweet.find('content').text)
        data.append(tweet.find('sentiment/polarity/value').text)
        #Write data to csv
        csvwriter.writerow(data)

#Get data folder directory
directory = os.fsencode('corpus')
#Open csv file
output = open('corpus/corpus.csv', 'w', newline='', encoding='utf-8')
#Create a csv writer
csvwriter = csv.writer(output)
#Write first row with the data labels
csvwriter.writerow(['text', 'sentiment'])

#Iterate files on directory
for file in os.listdir(directory):
    #Get filename
    filename = os.fsdecode(file)
    #Build path
    path = ''.join(['corpus/',filename])
    print(path)

    #Check if is an xml
    if filename.endswith(".xml"): 
        tree = ElementTree.parse(path)
        #Write data to csv
        write_to_csv(csvwriter, tree)