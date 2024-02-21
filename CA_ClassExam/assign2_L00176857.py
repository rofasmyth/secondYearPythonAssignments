# Name: Ronan Smyth
# Student Number: L00176857
# Filename: assign2_L00176857
# Desc: A program from handling CSV, TEXT & JSON files.

import json
import csv

#====================================================================

def displayCSVFile():
    try:
        # Save filepath for .csv file.
        csvPath = "top1000Films.csv"

        # Remove quotes from the path.
        csvPath = csvPath.strip('"')

        with open(csvPath, 'r', encoding='utf-8') as csvFile:
            # Use csv module's reader method read data.
            csvData = csv.reader(csvFile)

            # Assuming the first row has titles - which I know it does.
            title = next(csvData)  # next() chooses the first row for its first iteration.

            # Create an empty list to save rows of data from the CSV file.
            filmInfo = []

            # Iterate over each row in the .csv file.
            for row in csvData:
                # Append the entire row to data as a list.
                filmInfo.append(row)

            # data is a list of lists, sublists are rows from the .csv.

            # Create a list of dictionaries.
            # Each dictionary is a row of the .csv with titles from the 1st row as keys.
            rows = []
            for row in filmInfo:
                rows.append(dict(zip(title, row)))  # Match the title and the info from the rows.

            # Write the list of dictionaries to JSON.
            output = json.dumps(rows, indent=2)

            # Print the JSON text.
            print(output)

    # Error checking in case file cannot be found.
    except FileNotFoundError:
        print(f"Error: The file '{csvPath}' not found.")
    # Error checking in case file is in incorrect format.
    except ValueError as e:
        print(f"Value Error: {e}")
    # Error checking in case of error in csv file.
    except csv.Error as e:
        print(f"CSV Error: {e}")
    # Error checking in case of unanticipated errors.
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

#====================================================================

def displayTextFile():
    try:
        # Save filepath for .txt file.
        textFilePath = "anthem.txt"
        # Remove quotes from the path.
        textFilePath = textFilePath.strip('"')

        # Open, read and display the content of the file.
        with open(textFilePath, 'r', encoding = 'utf-8') as infile:
            content = infile.read()
            print(content)
            
    # Throw appropriate error messages if file can't be read.
    except FileNotFoundError:
        print(f"The file '{textFilePath}' was not found. Please check the path and try again.")
    except ValueError as e:
        print(f"Value Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}. Please try again.")


#====================================================================

def displayJSONFile():
    # Save filepath for json file.
    jsonFilePath = "books.json"
    # Remove quotes from the path.
    jsonFilePath = jsonFilePath.strip('"')

    try:
        # Open, read and display the content of the JSON file.
        with open(jsonFilePath, 'r') as jsonFile:
            jsonData = json.load(jsonFile)
            print(json.dumps(jsonData, indent = 4)) # indent=4 looks better in IDLE.
            
    # Throw appropriate error messages if file can't be read or decoded.
    except FileNotFoundError:
        print(f"The file '{jsonFilePath}' was not found.")
    except ValueError as e:
        print(f"Value Error: {e}")
    except json.JSONDecodeError:
        print(f"Error decoding JSON in the file '{jsonFilePath}'.")


#====================================================================

def readCSVWriteJSON():
    # Save filepath for .csv file.
    csvPath = "top1000Films.csv"

    # Remove surrounding quotes from the entered path
    csvPath = csvPath.strip('"')

    try:
        # Open and read the csv file.
        with open(csvPath, 'r', newline='', encoding='utf-8') as csvFile:
            csvData = csv.reader(csvFile)

            # Assuming the first row contains headers.
            titles = next(csvData)

            # Create a list of dictionaries.
            # Each dictionary is a row of the .csv with titles from the 1st row as keys.
            data = []
            for values in csvData:
                row = dict(zip(titles, values)) # Match the title and the info from the rows.
                data.append(row)

            # Name the output file.
            jsonPath = "top1000Films.json"
            # Remove quotes from the path.
            jsonPath = jsonPath.strip('"')

            # Write the csv data to a json file.
            with open(jsonPath, 'w', encoding='utf-8') as jsonFile:
                print(json.dump(data, jsonFile, indent=4))

        print(f"Conversion from .csv to .json successful. Output file: {jsonPath}")

    # Throw appropriate error messages if file can't be read or decoded.
    except FileNotFoundError:
        print(f"The file '{csvPath}' was not found.")
    except ValueError as e:
        print(f"Value Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
        
#=========================================
        
def createActorsList():
    try:
        # Save filepath for json file.
        jsonFilePath = "top1000Films.json"
        # Remove quotes from the path.
        jsonFilePath = jsonFilePath.strip('"')

        # Open and read .json file.
        with open(jsonFilePath, 'r', encoding='utf-8') as jsonFile:
            films = json.load(jsonFile)

            # Create a set to eliminate duplicate actor names.
            uniqueActors = set()

            # Iterate the .json file and add actors to the set.
            for film in films:
                # Assuming 'Actors' is a key in each film's dictionary
                actors = film.get('Actors', '').replace(', ', ',').split(',')
                uniqueActors.update(actors)

            # Create a list from the set - translates better, looks better in the following dictionary.
            actorsList = list(uniqueActors)
            # Create a dictionary which looks better in json.
            writeToJSON = {'actors': actorsList}

            # Create the output file path in the same directory with the input file. 
            outputPath = "actors.json"
            # Remove quotes from the path.
            outputPath = outputPath.strip('"')

            # Write the actors to a json file.
            with open(outputPath, 'w', encoding='utf-8') as jsonFile:
                json.dump(writeToJSON, jsonFile, indent=4)

        print(f"Actors list successfully created and saved to: {outputPath}")
        
    # Error handling.
    except FileNotFoundError:
        print(f"Error: The file '{jsonFilePath}' was not found.")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON in file '{jsonFilePath}': {e}")
    except ValueError as e:
        print(f"Value Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


#====================================================================

def searchAndDisplay():
    # Save filepath for .json file.
    jsonPath = "top1000Films.json"

    # Remove quotes from path.
    jsonPath = jsonPath.strip('"')

    # Input keyword and convert to lower case.
    keyword = input("Enter a word to search for: ")
    keyword = keyword.lower()
    
    try:
        # Open and read the json file.
        with open(jsonPath, 'r', encoding='utf-8') as jsonFile:
            infile = json.load(jsonFile)

            # Create a list of films whose data contains the keyword.
            matching_films = []

            for film in infile:
                # Check if the keyword is present in any of the fields.
                # Also, convert the field string data to lower case so case will not affect outcome.
                if any(keyword in field.lower() for field in [film['Title'], film.get('Director', ''), ', '.join(film.get('Actors', [])), film.get('Genre', ''), film.get('Description', '')]):
                    matching_films.append(film)

            # Display matching films as JSON dictionaries.
            print(json.dumps(matching_films, indent=4))
            
    # Standard error handling for working with json.
    except FileNotFoundError:
        print(f"The file '{jsonPath}' was not found.")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON in the file '{jsonPath}': {e}")
    except ValueError as e:
        print(f"Value Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

        ## Note that the output displays 'Rank' in the first position instead of 'Title'. I can't see why.

#====================================================================

def writeFileByYear():

    # Save filepath for .json file.
    jsonPath = "top1000Films.json"

    # Remove surrounding quotes from the entered path
    jsonPath = jsonPath.strip('"')

    targetYear = input("Enter a word to search for: ")
    targetYear = targetYear.lower()
    try:
        with open(jsonPath, 'r', encoding='utf-8') as jsonFile:
            films = json.load(jsonFile)

            # Filter films by the target year
            filmsToShow = []
            for film in films:
                if film.get('Year') == targetYear:
                    filmsToShow.append(film)

            # Check that there are films on the list from the target year.
            if not filmsToShow:
                print(f"No films found for the year {targetYear}.")
                return

            # Create the output file path in the same directory with the input file.
            outputPath = (f"top1000Films{targetYear}.json")
            # Remove quotes from the path.
            outputPath = outputPath.strip('"')

            with open(outputPath, 'w', encoding='utf-8') as outputFile:
                # Write film details as a JSON array
                json.dump(filmsToShow, outputFile, indent=4)

        print(f"Top films of {targetYear} written to '{outputPath}' in JSON format.")

    except FileNotFoundError:
        print(f"The file '{jsonPath}' was not found.")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON in the file '{jsonPath}': {e}")
    except ValueError as e:
        print(f"Value Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

#====================================================================

def frequencyDistribution():
    
    try:
        # Save filepath for .json file.
        jsonPath = "top1000Films.json"

        # Remove surrounding quotes from the entered path
        jsonPath = jsonPath.strip('"')

        if not jsonPath:
            print("Exiting the program. No file path provided.")

        with open(jsonPath, 'r', encoding='utf-8') as jsonFile:
            films = json.load(jsonFile)

            # Extract the names of directors from each record
            directorNames = []
            for film in films:
                directorNames.append(film.get('Director', None))

            # Create the frequency distribution using a dictionary.
            frequencyDistribution = {}
            for name in directorNames:
                frequencyDistribution[name] = frequencyDistribution.get(name, 0) + 1

            # Sort the dictionary by director names
            sortedDictionary = dict(sorted(frequencyDistribution.items()))

            # Create the output file path in the same directory with the input file.
            outputPath = "freqDist.json"
            # Remove quotes from the path.
            outputPath = outputPath.strip('"')
            
            with open(outputPath, 'w', encoding='utf-8') as outputFile:
                json.dump(sortedDictionary, outputFile, indent=4)

            print(f"Frequency Distribution Report for Directors written to '{outputPath}'.")
                

    except FileNotFoundError:
        print(f"The file '{jsonPath}' was not found. Please check the file path and try again.")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON in the file '{jsonPath}': {e}")
    except ValueError as e:
        print(f"Value Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
#====================================================================

while True:
    print()
    print("JSON Handling System")
    print("=============================")
    print("1. Display contents of any csv file.")
    print("2. Display contents of any text file.")
    print("3. Display contents of any JSON file.")
    print("4. Read contents of top1000Films.csv.")
    print("5. Create a unique list of actors.")
    print("6. Search on keyword.")
    print("7. Write top films of a given year to file.")
    print("8. Generate frequency distribution report.")

    print("0. Quit")
    print()
    print("Enter Zero[0] to Quit")

    selection = input("Please make a selection from the Menu: ")

    if selection == "1":
        displayCSVFile()
    elif selection == "2":
        displayTextFile()
    elif selection == "3":
        displayJSONFile()
    elif selection == "4":
        readCSVWriteJSON()
    elif selection == "5":
        createActorsList()
    elif selection == "6":
        searchAndDisplay()
    elif selection == "7":
        writeFileByYear()
    elif selection == "8":
        frequencyDistribution()
    elif selection == "0":
        print("Thank you! Goodbye!")
        break
    else:
        print("Please make a valid selection between 1 and 8 OR select 0(zero) to quit.")
