#This file was used as a test to check if the file reading system was going to work 
# It is a copy from setupFile.py but desgined for testing

def Convert(string): 
    li = list(string.split("; ")) 
    return li 

def ConvertLocation(string):
    l = Convert(string)
    returnList = []
    for i in l:
        returnList.append(list(i.split(", "))) 
    return returnList

def main():

    # Format for File Reading 
    # 1. Provider Name
    # 2. Program Name
    # 3. Community Engagement 
    # 4. Research Oppurtinities
    # 5. Internship Oppurtunities
    # 6. Cost
    # 7. Cost Stipulations
    # 8. Description
    # 9. Url
    # 10. Areas
    # 11. Terms
    # 12. Languages
    # 13. Locations

    #References for work: 
    #https://tecadmin.net/count-number-of-lines-in-file-python/
    #https://www.geeksforgeeks.org/python-program-convert-string-list/

    fname = "DataImportFile.txt"
    lineCount = 1
    with open(fname, 'r') as f:
        for eachLine in f:
            line = eachLine.strip()
            if(lineCount % 14 == 1):
                #Provider
                providerName = line
                print(providerName)
            if(lineCount % 14 == 2):
                #Program
                programName = line
                print(programName)
            if(lineCount % 14 == 3):
                #Community Engagement
                com = line
                print(com)
            if(lineCount % 14 == 4):
                #Research Oppurtinities
                res = line
                print(res)
            if(lineCount % 14 == 5):
                #Internship Oppurtunities
                intern = line
                print(intern)
            if(lineCount % 14 == 6):
                #Cost
                cost = line 
                print(cost)
            if(lineCount % 14 == 7):
                #Cost Stipulations
                cost_stipulations = line
                print(cost_stipulations)
            if(lineCount % 14 == 8):
                #Description
                description = line
                print(description)
            if(lineCount % 14 == 9):
                #Url
                url = line
                print(url)
            if(lineCount % 14 == 10):
                #Areas
                areas = Convert(line)
                print(areas)
            if(lineCount % 14 == 11):
                #Terms
                terms = Convert(line)
                print(terms)
            if(lineCount % 14 == 12):
                #Languages
                languages = Convert(line)
                print(languages)
            if(lineCount % 14 == 13):
                #Locations
                locations = ConvertLocation(line)
                print(locations)
            if(lineCount % 14 == 0): 
                print("Next Program")
            lineCount += 1
            


if __name__ == '__main__':
    main()