#This small project works with lists and dictionaries. It takes in a user input (in this case a certain language)
#and inputs it into the list of languages. After N/A is inputted, the popular_languages function takes
#in the list and inputs the name of the langs as well as their frequencies inside a dictionary. At the end,
#the dictionary is printed. Very barebones project, didnt do any error handling or checks. Just a quick little
#project in order to familiarize myself with the Python syntax as well as some of its built in data structures.
def popular_languages(langs):
	print("Popularity Count:")
	frequency = {}
	for lang in langs:
		#If a languages is in the dictionary
		if lang in frequency:
			frequency[lang] += 1
		#If a languages isnt in the dictionary
		else:
			frequency[lang] = 1
	print(frequency)

def main():
	print("This is my first Python project!")
	active = True
	languages = []
	while active is True:
		print("\nType N/A in order to see the total list of languages and their popularities :)")
		language = input("What's your favorite language?")
		if language == "N/A":
			active = False
		languages.append(language)
	#Deletes the 'N/A' at the end of the list
	del languages[-1]
	popular_languages(languages)
main()