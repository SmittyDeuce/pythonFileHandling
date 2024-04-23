import re
import os


# 1. Exploring Python's OS Module
# Objective:
# The goal of this assignment is to deepen your understanding of the OS module in Python. You will engage in tasks that involve file and directory operations, path manipulations, and practical applications of these operations in real-world scenarios.

# Task 1: Directory Inspector:

# Problem Statement:
# Create a Python script that lists all files and subdirectories in a given directory. Your script should prompt the user for the directory path and then display the contents.

# Code Example:
# ```python
# import os
# def list_directory_contents(path):
#     # List and print all files and subdirectories in the given path
# ```
# Expected Outcome:
# The script should correctly list all files and subdirectories in the specified directory. Handle exceptions for invalid paths or inaccessible directories.


'''creating full file path
os.path.join(directory, file) is used because
getsize() needs full path as args
'''


def directoryInspector():
    searchPath = input("Enter the path your're looking for: ").strip()
    if os.path.exists(searchPath):
        print("File Exists...")
        try:
            if len(os.listdir(searchPath)) == 0:
                print("Directory is Empty")
            else:
                print(os.listdir(searchPath))
        except NotADirectoryError:
            print("Directory Not Found.")
    else:
        print("Path does not exist")


# directoryInspector()


# Task 2: File Size Reporter:

# Problem Statement:
# Write a Python program that reports the sizes of all files in a specific directory. The program should ask the user for a directory path and then print each file's name and size within that directory.

# Code Example:
# ```python
# def report_file_sizes(directory):
# # Iterate through files in the directory and print their names and sizes
# ```
# Expected Outcome:
# Your program should display the name and size (in bytes) of each file in the given directory. Ensure that the program only reports on files, not directories, and handles any errors gracefully.

def FileSizeReporter():
    searchPath = input("Enter the path your're looking for: ").strip()
    if os.path.exists(searchPath):
        print("File Exists...")
        try:
            #checks if directory is empty
            if len(os.listdir(searchPath)) == 0:
                print("Directory is Empty")
            else:
                # if not get list of files in directory
                files = os.listdir(searchPath)

                for file in files:
                    '''creating full file path
                        os.path.join(directory, file) is used because
                        getsize() needs full path as args
                    '''
                    filePath = os.path.join(searchPath, file)
                    # checks if file is a regular file
                    # print(type(filePath))
                    if os.path.isfile(filePath):
                        # get size of file
                        size = os.path.getsize(filePath)
                        print(f"file {file} has a size of {size} bytes")
                   
        except NotADirectoryError:
            print("Directory Not Found.")
    else:
        print("Path does not exist")

FileSizeReporter()


# Task 3: File Extension Counter:

# Problem Statement:
# Develop a Python script that counts the number of files of each extension type in a directory. For instance, in a directory with five '.txt' files and three '.py' files, the script should report "TXT: 5" and "PY: 3".

# Code Example:
# python def count_file_extensions(directory): # Count and print the number of files of each extension type in the directory
# Expected Outcome:
# The script should accurately count and display the number of files for each extension type in the specified directory. Handle different cases of file extensions (e.g., '.TXT' and '.txt' should be considered the same).

def FileExtensionCounter():
    fileExtension = {}
    searchPath = input("Enter the path your're looking for: ").strip()
    if os.path.exists(searchPath):
        print("File Exists...")
        try:
            if len(os.listdir(searchPath)) == 0:
                print("Directory is Empty")
            else:
                files = os.listdir(searchPath)
                for file in files:
                    _, extension = os.path.splitext(file)
                    extension = extension.lower()
                    filePath = os.path.join(searchPath, file)
                    # print(extension)
                    if extension in fileExtension:
                        fileExtension[extension] += 1
                    else:
                        fileExtension[extension] = 1

                    # if os.path.isfile((filePath)) and re.search(isPython, filePath):
                    #     print(filePath)
                    #     fileExtension['.py'] += 1
                    # if os.path.isfile((filePath))  and not re.search(isPython, filePath):
                    #     fileExtension['.txt'] += 1
            print(fileExtension)
        except NotADirectoryError:
            print("Directory Not Found.")
    else:
        print("Path does not exist")

    
FileExtensionCounter()



# 2. Regex-Powered Text Data Processing
# Objective:
# The purpose of this assignment is to harness the power of regular expressions (regex) in Python for advanced text data processing. You will apply regex to extract, manipulate, and analyze data from text files, combining it with efficient file handling techniques.

# Task 1: Email Extractor:

# Problem Statement:
# Write a Python script to extract all email addresses from a given text file (contacts.txt). The file contains a mix of text and email addresses.

# File Example:
# ```
# Contact List:
# John Doe - john.doe@example.com
# Jane Smith - jane.smith@gmail.com

# For inquiries, please contact info@example.com
# ```
# Code Example:
# ```python
# import re
# def extract_emails(filename):
#     # Read the file and use regex to find and return all email addresses
# ```
# Expected Outcome:
# The script should output a list of all unique email addresses found in the file. Utilize regex to accurately identify email addresses amidst other text.

with open('contacts.txt', "w+") as file:
    file.write("John Doe - john.doe@example.com")
    file.write("\nJane Smith - jane.smith@gmail.com")

def EmailExtractor():
    with open('contacts.txt') as file:
        for line in file:
            emailPattern = r'[a-z.]+@[a-z]+\.[a-z]{2,}'
            match = re.findall(emailPattern, line)
            for email in match:
                print(email)

EmailExtractor()

# 3. Advanced Python Data Processing and Analysis Challenge
# Objective:
# This assignment is aimed at challenging your skills in advanced data processing and analysis using Python. It encompasses a broad range of topics, including file handling, regular expressions, data structures, and complex problem-solving, at a medium-hard difficulty level.

# Task 1: Travel Blog Sentiment Analysis:

# Problem Statement:
# Perform sentiment analysis on a collection of travel blog entries stored in travel_blogs.txt. Identify and count the occurrences of positive words (e.g., "amazing", "enjoy", "beautiful") and negative words (e.g., "bad", "disappointing", "poor").
# - Dataset Example: <div class='oc-markdown-custom-container oc-markdown-activatable' contenteditable='false' data-value='```
# Travel Blog Entries:
# "Our recent trip to the mountains was amazing! The scenery was breathtaking and we enjoyed every moment of it."
# "The beach vacation was wonderful. We relaxed by the shore and soaked up the sun."
# "The city tour was a bit disappointing. The guide wasn't very knowledgeable, and the attractions were overcrowded."
# "Exploring the countryside was a unique experience. The landscapes were stunning, but the accommodations were poor."
# "Despite the rain, our visit to the waterfall was memorable. The cascading water was mesmerizing."
# "We had high hopes for the safari adventure, but it turned out to be lackluster. The wildlife sightings were scarce."
# "The food on our trip was excellent. We sampled delicious local cuisine at every stop."
# "The historical tour was enlightening. We learned so much about the culture and heritage of the region."
# "Overall, our travel experience was fantastic. We made unforgettable memories and can't wait for our next adventure!"
# '>
# Travel Blog Entries:
# "Our recent trip to the mountains was amazing! The scenery was breathtaking and we enjoyed every moment of it."
# "The beach vacation was wonderful. We relaxed by the shore and soaked up the sun."
# "The city tour was a bit disappointing. The guide wasn't very knowledgeable, and the attractions were overcrowded."
# "Exploring the countryside was a unique experience. The landscapes were stunning, but the accommodations were poor."
# "Despite the rain, our visit to the waterfall was memorable. The cascading water was mesmerizing."
# "We had high hopes for the safari adventure, but it turned out to be lackluster. The wildlife sightings were scarce."
# "The food on our trip was excellent. We sampled delicious local cuisine at every stop."
# "The historical tour was enlightening. We learned so much about the culture and heritage of the region."
# "Overall, our travel experience was fantastic. We made unforgettable memories and can't wait for our next adventure!"
# ```
# Code Example:
# ```
# Travel Blog Entries:
# 1. "Our recent trip to the mountains was amazing! The scenery was breathtaking and we enjoyed every moment of it."

# 2. "The beach vacation was wonderful. We relaxed by the shore and soaked up the sun."

# 3. "The city tour was a bit disappointing. The guide wasn't very knowledgeable, and the attractions were overcrowded."

# 4. "Exploring the countryside was a unique experience. The landscapes were stunning, but the accommodations were poor."

# 5. "Despite the rain, our visit to the waterfall was memorable. The cascading water was mesmerizing."

# 6. "We had high hopes for the safari adventure, but it turned out to be lackluster. The wildlife sightings were scarce."

# 7. "The food on our trip was excellent. We sampled delicious local cuisine at every stop."

# 8. "The historical tour was enlightening. We learned so much about the culture and heritage of the region."

# 9. "Overall, our travel experience was fantastic. We made unforgettable memories and can't wait for our next adventure!"
# ```
# Expected Outcome:
# A summary report indicating the number of positive and negative words in the travel blogs, demonstrating the ability to process text data and apply basic sentiment analysis.

travel_blog_entries = [
 "Our recent trip to the mountains was amazing! The scenery was breathtaking and we enjoyed every moment of it.",
 "The beach vacation was wonderful. We relaxed by the shore and soaked up the sun.",
 "The city tour was a bit disappointing. The guide wasn't very knowledgeable, and the attractions were overcrowded.",
 "Exploring the countryside was a unique experience. The landscapes were stunning, but the accommodations were poor.",
 "Despite the rain, our visit to the waterfall was memorable. The cascading water was mesmerizing.",
"We had high hopes for the safari adventure, but it turned out to be lackluster. The wildlife sightings were scarce.",
"The food on our trip was excellent. We sampled delicious local cuisine at every stop.",
"The historical tour was enlightening. We learned so much about the culture and heritage of the region.",
"Overall, our travel experience was fantastic. We made unforgettable memories and can't wait for our next adventure!"
]

def sentimentAnalysis(blog_entries):
    postiveWords = ["amazing", "enjoy", "beautiful","excellent","fantastic"]
    negativeWords = ["bad", "disappointing", "poor","lackluster"]
    positive = {'positive': 0}
    negative = {'negative': 0}
    fileName = input("Enter File Name: (include extension) ").lower().strip()
    
    #check if file exists
    if not os.path.isfile(fileName):

        #if not open\create file and append the information
        with open(f"{fileName}", "a") as file:
            for entry in blog_entries:
                file.write(f"{entry}\n")
    else:

        # if exists, open file and overwrite contents
        with open(f"{fileName}", "w") as file:
            for entry in blog_entries:
                file.write(f"{entry}\n")

    #count occurences of postive words in blog

    for entry in blog_entries:
       for word in postiveWords:
           if word in entry.lower():
               positive["positive"] += 1

    #count occurences of negative words in blog
    for entry in blog_entries:
        for word in negativeWords:
            if word in entry.lower():
                negative["negative"] += 1


    print(f"Positive Words: {positive}\nNegative Words: {negative}")

sentimentAnalysis(travel_blog_entries)

# Task 2: Historical Weather Data Compiler

# Problem Statement:
# Compile and analyze historical weather data from multiple files (weather_2020.txt, weather_2021.txt, etc.). Each file contains daily temperature data. Calculate the average temperature for each year and identify the year with the highest average.

# - Dataset Example:
# File: weather_2020.txt
# python def analyze_blog_sentiments(blog_file): # Implement sentiment analysis logic on the blog file
# Code Example:
# 2020-01-01,5°C 2020-01-15,6°C 2020-02-05,4°C 2020-02-20,7°C 2020-03-10,8°C 2020-03-25,9°C 2020-04-05,12°C 2020-04-20,14°C 2020-05-05,17°C 2020-05-20,19°C 2020-06-05,22°C 2020-06-20,25°C 2020-07-05,28°C 2020-07-20,30°C 2020-08-05,32°C 2020-08-20,31°C 2020-09-05,27°C 2020-09-20,24°C 2020-10-05,19°C 2020-10-20,16°C 2020-11-05,11°C 2020-11-20,9°C 2020-12-05,6°C 2020-12-20,4°C
# Expected Outcome:
# An aggregated view of average temperatures for each year and identification of the year with the highest average temperature, showcasing data aggregation and analysis skills.

weather_2020 = "2020-01-01,5°C 2020-01-15,6°C 2020-02-05,4°C 2020-02-20,7°C 2020-03-10,8°C 2020-03-25,9°C 2020-04-05,12°C 2020-04-20,14°C 2020-05-05,17°C 2020-05-20,19°C 2020-06-05,22°C 2020-06-20,25°C 2020-07-05,28°C 2020-07-20,30°C 2020-08-05,32°C 2020-08-20,31°C 2020-09-05,27°C 2020-09-20,24°C 2020-10-05,19°C 2020-10-20,16°C 2020-11-05,11°C 2020-11-20,9°C 2020-12-05,6°C 2020-12-20,4°C"
weather_2020List = weather_2020.split(" ")

if not os.path.isfile("weather_2020.txt"):
    with open("weather_2020.txt", "a") as file:
        for weather in weather_2020List:
            file.write(f"{weather}\n")
else:
    with open("weather_2020.txt", "w") as file:
        for weather in weather_2020List:
            file.write(f"{weather}\n")

weather_2021 = "2021-01-01,4°C 2021-01-15,5°C 2021-02-05,3°C 2021-02-20,6°C 2021-03-10,7°C 2021-03-25,8°C 2021-04-05,11°C 2021-04-20,13°C 2021-05-05,16°C 2021-05-20,18°C 2021-06-05,21°C 2021-06-20,24°C 2021-07-05,27°C 2021-07-20,29°C 2021-08-05,31°C 2021-08-20,30°C 2021-09-05,26°C 2021-09-20,23°C 2021-10-05,18°C 2021-10-20,15°C 2021-11-05,10°C 2021-11-20,8°C 2021-12-05,5°C 2021-12-20,3°C"
weather_2021List = weather_2021.split(" ")

if not os.path.isfile("weather_2021.txt"):
    with open("weather_2021.txt", "a") as file:
        for weather in weather_2021List:
            file.write(f"{weather}\n")
else:
    with open("weather_2021.txt", "w") as file:
        for weather in weather_2021List:
            file.write(f"{weather}\n")


def weatherDataCompiler(data1, data2):
    data1_Total = 0
    data2_Total = 0
    data1_Counter = 0
    data2_Counter = 0

    with open(data1) as file:
        for data in file:
            dataList = data.split(",")
            temp = dataList[1]
            temp = temp.strip()
            data1NumData = r"[0-9]{1,2}"
            match = re.findall(data1NumData, temp)
            for stats in match:
                data1_Counter += 1
                data1_Total += int(stats)
    
    with open (data2) as file:
        for data in file:
            dataList = data.split(",")
            temp = dataList[1]
            temp = temp.strip()
            data2NumData = r'[0-9]{1,2}'
            match = re.findall(data2NumData, temp)
            for stats in match:
                data2_Counter += 1
                data2_Total += int(stats)

    data1_Avg = int(data1_Total / data1_Counter)
    data2_Avg = int(data2_Total / data2_Counter)
   
    print(f"{data1} yearly avg was the highest\n{data1}: {data1_Avg}\n{data2}: {data2_Avg}")


weatherDataCompiler("weather_2020.txt", "weather_2021.txt")