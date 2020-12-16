import logging
import sys
import timeit

docname = ""
rwswitch= ""
userinput = ""


# User starts the program
start_time = timeit.timeit()

log_m_format = "%(asctime)s (%(module)s --> %(funcName)s[%(lineno)d]) [%(levelname)s]: %(message)s"
log_level = logging.DEBUG
logging.basicConfig(filename=f"consoleapp.log", filemode='w', format= log_m_format, level=log_level)

def main():
    
        
        #log.info("[INFO]: Program starting")
        

        args = sys.argv[1:]
        print(args)
        print("Number of args :: ", format(len(args)))
        for arg in args:
            print("Passed argument in :: ", format(arg))
        
        if (args[1].lower() == 'r'):
            readfile(args[0])
        elif(args[1].lower() == 'w'):
            writefile(args[0])

        #if len(userinput) < 2:
            #log.error("[ERROR]: 2 arguments are required")
        #else:
            # docname = sys.argv[1]
             #rwswitch = sys.argv[2]

#This function reads the document, counts how many times the word
#"imperdiet" appears in the document, and how many lines it appears in
#param: docname (the name of the document)
def readfile(docname):
    wordcount = 0
    finalwordcount = 0
    linecount = 0
    totallinecount = 0

    #start time for function
    start_time2 = timeit.timeit()

    #Program starts to read file
    fileread = open(docname, 'r')

    #Program starts to read each line
    line = fileread.readline()
    while line != "":
        #Program searches for the word "imperdiet"
        wordcount = line.count("imperdiet")
        finalwordcount += wordcount
        #If line contains the word
        if wordcount > 0:
            linecount += 1

        #Counts each line as it finishes reading the line
        totallinecount += 1
        line = fileread.readline()
    print("Imperdiet appears in the document ", finalwordcount, " times")
    print("Imperdiet appears in ", linecount, " lines.")
    #log.debug("[DEBUG]: Program has finished reading the document")

    fileread.close()

    #Time that document stops reading the file
    end_time2 = timeit.timeit()

    #Gets execution time
    execute_time_r = end_time2-start_time2

    #function to get average time of each line read
    def average(content):

        #Divides execution time by total number of lines
        avglineread = execute_time_r/content
        return avglineread

    #prompts user to get program metrics
    getmetrics = input("Would you like to see the metrics? Press 'y' if you would like to: ")

    #If the user wants metrics
    if getmetrics == 'y':
        #log.debug("[DEBUG]: The user would like to review program metrics")

        #Calls the averageline method
        avgline= average(totallinecount)
        print("The average time to read each line is: ", avgline, " seconds")

        avgword = average(finalwordcount)
        print("The average time to find the word 'imperdiet' is: ", avgword, " seconds")

def writefile(docname):
    wordcount = 0
    finalwordcount = 0
    linecount = 0
    sentencecount = 0

    newfile = open(docname, 'w')

    userinput = input("Enter a sentence: ")
    #log.debug("[DEBUG]: User has entered input")

    newfile.write(userinput)
    #log.debug("[DEBUG]: Input entered into file")

    wordcount = userinput.count("imperdiet")
    
    if wordcount > 0:
        linecount += 1
    finalwordcount += wordcount
    #sentencecount += 1

    
    
    while userinput != "n":
        start_time_w = timeit.timeit()
        userinput = input("Enter another sentence or type 'n' to quit: ")
        wordcount = userinput.count('imperdiet')
        finalwordcount += wordcount
        if wordcount > 0:
            linecount += 1
        #sentencecount += 1
        #userinput = input("Enter another sentence or type 'n' to quit: ")
    newfile.close()
    end_time_w = timeit.timeit()
    execute_time = end_time_w - start_time_w
    print("The number of times 'imperdiet' appeared in the file is: ", wordcount)
    print("The number of sentences that contain 'imperdiet': ", linecount)
    #print("The number of sentences in the document is: ", sentencecount)

    #initiates variable of average lines read
    #avglinewrite = 0

    #function to get average time of each line read
    #def average(content):

        #Divides execution time by total number of lines
        #avglinewrite = execute_time/content
        #return avglinewrite

    #prompts user to get program metrics
    #getmetrics = input("Would you like to see the metrics? Press 'y' if you would like to: ")

    #If the user wants metrics
    #if getmetrics == 'y':
        #log.debug("[DEBUG]: The user would like to review program metrics")

        #Calls the averageline method
        #avgwriteline= average(sentencecount)
        #print("The average time to write each line is: ", avgwriteline, " seconds")

        #avgwriteword = average(wordcount)
        #print("The average time to find the word 'imperdiet' is: ", avgwriteword, " seconds")
    
if __name__ == '__main__':
    main()
end_time = timeit.timeit()
#print(end_time)
execute_time = (end_time - start_time)
print("Total execution time for the file: %12.12f seconds " % execute_time)
#log.info("[INFO]: End of program")