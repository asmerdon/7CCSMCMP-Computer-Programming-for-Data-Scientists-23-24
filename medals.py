import csv
import json

#countryMedals class definition
class CountryMedals:
    def __init__(self, countryName, goldMedals, silverMedals, bronzeMedals, total):
        self.name = countryName
        self.gold = goldMedals
        self.silver = silverMedals
        self.bronze = bronzeMedals
        self.total = total

    def to_json(self):
        # converts to json
        data = {"gold": self.gold, "silver": self.silver, "bronze": self.bronze, "total": self.total}
        return data

    def get_medals(self, medal_type):
        #gets medal count
        if medal_type == "gold":
            return self.gold
        elif medal_type == "silver":
            return self.silver
        elif medal_type == "bronze":
            return self.bronze
        elif medal_type == "total":
            return self.total
        else:
            return None

    def print_summary(self):
        print(f"{self.name} received {self.total} medals in total; {self.gold} gold, {self.silver} silver, and {self.bronze} bronze.")

    def compare(self, country_2):
        print("Medals comparison between " + self.name + " and " + country_2.name + ":")
        c2gold = country_2.gold
        c2silver = country_2.silver
        c2bronze = country_2.bronze
        c2total = country_2.total
        # medal comparison function:
        def medalComparison(medalColour, medal, otherMedal):
            medalColour = medalColour
            if medal == otherMedal:
                print(f"Both {self.name} and {country_2.name} received {medal} {medalColour} medal(s).")
            elif medal < otherMedal:
                difference = int(otherMedal) - int(medal)
                print(f"{self.name} received {medal} {medalColour} medals(s), {difference} fewer than {country_2.name} which received {otherMedal}.")
            elif medal > otherMedal:
                difference = int(medal) - int(otherMedal)
                print(f"{self.name} received {medal} {medalColour} medals(s), {difference} more than {country_2.name} which received {otherMedal}.")
        #call for each medal type
        medalComparison("gold", self.gold, c2gold)
        medalComparison("silver", self.silver, c2silver)
        medalComparison("bronze", self.bronze, c2bronze)

        # total comparison
        if self.total < c2total:
            totalDifference = int(c2total) - int(self.total)
            print(f"Overall, {self.name} received {self.total} medal(s), {totalDifference} less than {country_2.name}, which received {c2total} medal(s).")
        else:
            totalDifference = int(self.total) - int(c2total)
            print(f"Overall, {self.name} received {self.total} medal(s), {totalDifference} more than {country_2.name}, which received {c2total} medal(s).")

#declare dictionary
countries = {}
#read csv (parse data)
with open('medals.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        countryObj = CountryMedals(row['Team/NOC'], row['Gold'], row['Silver'], row['Bronze'], row['Total']) #creates instance of object
        countries[row['Team/NOC']] = countryObj #adds object to countries dict with country name as key

#helper functions:
#sorts alphebetically
def get_sorted_list_of_country_names(countries):
    cSorted = sorted(countries.keys())
    return cSorted
#sorts ascending
def sort_countries_by_medal_type_ascending(countries, medal_type):
    ascSorted = sorted(countries.items(), key=lambda x: int(x[1].get_medals(medal_type))) #converts to int before sorting to get actual asc order.
    return dict(ascSorted)
#sorts descending
def sort_countries_by_medal_type_descending(countries, medal_type):
    sorted_countries = sorted(countries.items(), key=lambda x: int(x[1].get_medals(medal_type)), reverse=True) #same as above but reversed
    return dict(sorted_countries)

#checks int is positive
def read_positive_integer():
    positive = False
    while positive == False:
        userInput = input("Enter a positive integer (or 0): ")
        if userInput.isnumeric():
            userInput = int(userInput)
            positive = True
    return userInput

#checks country name is valid
def read_country_name():
    positive = False
    while positive == False:
        userInput = input("Enter the name of a country in the Olympics: ")
        if userInput in countries:
            positive = True
        else:
            print("Name of country not in the Olympics!")
    return userInput

#checks medal type is valid
def read_medal_type():
    positive = False
    while positive == False:
        userInput = input("Enter medal type (gold, silver, bronze) or total: ")
        if userInput == 'gold' or userInput == 'silver' or userInput == 'bronze' or userInput == 'total':
            positive = True
        else:
            print("Enter a valid input.")
    return userInput

#main program
def main_loop():
    positive = False
    while positive == False:
        userInput = input("Insert a command (Type 'H' for help): ")
        if userInput == 'h' or userInput == 'H':
            print("List of commands:")
            print("- (H)elp shows the list of comments;")
            print("- (L)ist shows the list of countries present in the dataset;")
            print("- (S)ummary prints out a summary of the medals won by a single country;")
            print("- (C)ompare allows for a comparison of the medals won by two countries;")
            print("- (M)ore, given a medal type, lists all the countries that received more medals than a threshold;")
            print("- (F)ewer, given a medal type, lists all the countries that received fewer medals than a threshold;")
            print("- (E)xport, save the medals table as '.json' file;")
            print("- (Q)uit.")
        #lists countries alphaptically
        elif userInput == 'l' or userInput == 'L':
            countryList = get_sorted_list_of_country_names(countries)
            print("Dataset contains: ")
            print(countryList)
        #summary
        elif userInput == 's' or userInput == 'S':
            summaryInput = read_country_name()
            countries[summaryInput].print_summary() #finds country in dict, calls print_summary method
        #comparison of 2 countries
        elif userInput == 'c' or userInput == 'C':
            country1 = read_country_name()
            country2 = read_country_name()
            countries[country1].compare(countries[country2])
        #more medals
        elif userInput == 'm' or userInput == 'M':
            threshold = read_positive_integer() #make sure input is positive
            medalType = read_medal_type() #make sure valid medal type
            countriesByType = sort_countries_by_medal_type_descending(countries, medalType)
            for countryName, medals in countriesByType.items(): #iterate through sorted countries
                if int(medals.get_medals(medalType)) > threshold: # prit if medal count above threshold
                    print(countryName + " recieved " + medals.get_medals(medalType))
        #fewer medals
        elif userInput == 'f' or userInput == 'F':
            threshold = read_positive_integer()
            medalType = read_medal_type()
            countriesByType = sort_countries_by_medal_type_descending(countries, medalType)
            for countryName, medals in countriesByType.items():
                if int(medals.get_medals(medalType)) < threshold: #same as above but below threshold
                    print(countryName + " recieved " + medals.get_medals(medalType))
        #export json file
        elif userInput == 'e' or userInput == 'E':
            jsonList = []
            for countryName, medals in countries.items(): #iterate through dict
                medalInfo = {"name": countryName, "medals": medals.to_json()}  #convert to json format
                jsonList.append(medalInfo) #append to list
            filename = input("Enter file name for JSON export: ")
            with open(filename, 'w') as json_file:
                json.dump(jsonList, json_file, indent=4) #indent 4 for formatting 
            print(f"The data has been exported to {filename}.json.")
        #quit
        elif userInput == 'q' or userInput == 'Q':
            print("Bye!")
            positive = True

main_loop()