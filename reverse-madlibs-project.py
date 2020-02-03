# allows us to clear the screen
def cls():
	print "\n" *100
	return

# Pause before screen refresh
def user_pause():
	raw_input("Press Enter to continue...")
	return

# Check for plural and punctuation. Takes the blank space and answer and returns completed word with full puncutation if applicable.
def check_puncuation(word, answer):
	if word.find("_") > 0:
		answer = word[:word.find("_")] + answer
	if word.find("_") + 4 != len(word):
		answer = answer + word[word.find("_") + 5:]
	return answer

# Input is the madlib, corresponding answer, and question number. Replaces the blank with answer and returns the changed madlib.
def reveal_words(madlib, answer, quest_num):
	madlib = madlib.split(" ")
	blank = "__" + str(quest_num+1) + "__"
	new_madlib = [] 
	for word in madlib:
		if blank in word:
			new_madlib.append(check_puncuation(word, answer))
		else:
			new_madlib.append(word)
	new_madlib = " ".join(new_madlib)
	print "Correct!"
	return new_madlib

# Contains the madlibs with answers. Input is difficulty level. Returns the appropriate madlib by difficulty.
def get_madlib(difficulty):
	difficulty_one = [ # from Dr. Seuss
					[["Today you are __1__! That is truer than __2__! There is no one __3__ who is you-er than __4__!"], ["you", "true", "alive", "you"],],
					[["The more that you __1__, the more __2__ you will know. The more that you __3__, the more places you'll __4__."], ["read", "things", "learn", "go"],],
					[["__1__ left and think __2__ and think __3__ and think high. Oh, the __4__ you can think up if you only __5__."], ["Think", "right", "low", "things", "try",],],
					]
	difficulty_two = [ # J.K. Rowlings Harry Potter and the Chamber of Secrets
					[["\"You all know, of course, that __1__ was founded over a thousand years ago - the precise date is uncertain - by the four greatest witches and __2__s of the age. The four school Houses are named after them: Godric __3__, Helga Hufflepuff, Rowena Ravenclaw, and Salazar Slytherin. They built this __4__ together, far from prying Muggle __5__s, for it was an age when magic was feared by common people, and witches and wizards suffered much persecution.\" He paused, gazed blearily around the room, and continued. \"For a few years, the founders worked in harmony together, seeking out youngsters who showed signs of magic and bringing them to the castle to be educated. But then disagreements sprang up between them. A rift began to __6__ between Slytherin and the others."],["Hogwarts", "wizard", "Gryffindor", "castle", "eye", "grow"],],
					[["__1__ wished to be more selective about the students admitted to Hogwarts. He believed that __2__ learning should be kept within all-magic families. He disliked taking students of __3__ parentage, believing them to be untrustworthy. After a while, there was a serious argument on the subject between Slytherin and Gryffindor, and Slytherin left the __4__.\" Professor Binns paused again, pursing his lips, looking like a wrinkled old tortoise. \"Reliable __5__ sources tell us this much,\" he said. \"But these honest facts have been obscured by the fanciful legend of the Chamber of __6__. The story goes that Slytherin had built a hidden chamber in the castle, of which the other founders knew nothing."],["Slytherin", "magical", "Muggle", "school", "historical", "Secrets"],],
					[["\"Slytherin, according to the __1__, sealed the Chamber of Secrets so that none would be able to open it until his own true __2__ arrived at the school. The heir alone would be able to unseal the Chamber of Secrets, unleash the horror within, and use it to __3__ the school of all who were unworthy to study magic.\" There was __4__ as he finished telling the story, but it wasn't the usual, sleepy silence that filled Professor Binns's classes. There was unease in the air as everyone continued to watch him, hoping for more. Professor __5__ looked faintly annoyed. \"The whole thing is arrant nonsense, of course,\" he said. \"Naturally, the school has been searched for evidence of such a chamber, many times, by the most learned witches and wizards. It does not exist. A tale told to frighten the __6__.\""],["legend", "heir", "purge", "silence", "Binns", "gullible"],],
					]
	difficulty_three = [ # Wikipedia - Hiryu aircraft carrier
					[["Hiryu (\"Flying Dragon\") was an __1__ carrier built for the Imperial Japanese Navy (IJN) during the __2__s. The only __3__ of her class, she was __4__ to a modified Soryu design. Her aircraft supported the Japanese __5__ of French Indochina in mid-1940. During the first __6__ of the Pacific War, she took part in the __7__ on Pearl Harbor and the Battle of Wake Island. The ship supported the __8__ of the Dutch East Indies in January 1942. "], ["aircraft", "1930", "ship", "built", "invasion", "month", "attack", "conquest"],],
					[["The following month, her __1__ bombed Darwin, Australia, and continued to assist in the Dutch __2__ Indies campaign. In April, __3__'s aircraft helped __4__ two British heavy cruisers and several merchant __5__ during the Indian Ocean raid. after a brief refit, Hiryu and three other fleet __6__s of the First Air Fleet (Kido Butai) __7__ in the Battle of __8__ in June 1942."],["aircraft", "East", "Hiryu","sink", "ships", "carrier", "participated", "Midway"],],
					[["After __1__ing American forces on the atoll, the carriers were __2__ed by aircraft from Midway and the __3__s USS Enterprise, Hornet, and Yorktown. Dive bombers from Yorktown and __4__ crippled Hiryu and set her afire. She was __5__ the following day after it became clear that she could not be salvaged. The __6__ of Hiryu and three other IJN carriers at Midway was a __7__ strategic defeat for Japan and contributed significantly to the Allies' ultimate __8__ in the Pacific."],["bombarding", "attack", "carrier", "Enterprise", "scuttled", "loss", "crucial", "victory"],],
					]
	if difficulty == 1:
		return difficulty_one
	if difficulty == 2:
		return difficulty_two
	if difficulty == 3:
		return difficulty_three
	return

# Displays the Madlib and current level for the user. Input is madlib and current level. Empty return. 
def display_madlib(madlib, level):
	cls()
	madlib_spaces = 135
	horizontal = 150
	verticle = 146
	title = "Reverse Madlibs by Steve Mahlstedt\n"
	print " " * (horizontal / 2 - len(title) / 2), title
	print "-" * horizontal
	print "|", " " * verticle, "|"
	for row in format_madlib_display(madlib, madlib_spaces):
		if len(row) < madlib_spaces:
			print "|", " " * 5, row, " " * (5 + madlib_spaces - len(row)) + "|"
		else:
			print "|", " " * 5, row, " " * 5 + "|"
	print "|", " " * verticle, "|"
	print "|", " " * (verticle - len(str(level+1))- 5 - len("Level: ")) + "Level: " + str(level + 1) + " " * 5, "|"
	print "-" * horizontal
	return

# Determines the length of the madlib row to avoid clipping. Inputs are the madlib and the max length. Returns the new row length.
def check_row_length(madlib, madlib_spaces):
	new_madlib_spaces = madlib_spaces
	if len(madlib) > madlib_spaces:
		if madlib[new_madlib_spaces] != " ":
			while madlib[new_madlib_spaces] != " ":
				new_madlib_spaces -= 1
			new_madlib_spaces += 1
	return new_madlib_spaces

# Takes the madlib list and turns it into appropriate display length. Input is the madlib and the length each row should be. Returns the newly formatted madlib.
def format_madlib_display(madlib, madlib_spaces):
	display_madlib = []
	length = len(madlib)
	i = 1
	while i > 0:
		hold_row = []
		new_madlib_spaces = check_row_length(madlib, madlib_spaces)
		hold_row.append(madlib[:new_madlib_spaces])
		length = length - new_madlib_spaces
		madlib = madlib[new_madlib_spaces:]
		i += 1
		hold_row = "".join(hold_row)
		display_madlib.append(hold_row)
		if length < madlib_spaces:
			display_madlib.append(madlib)
			return display_madlib
	return

# Asks the user for input to restart the game or end. 
def play_again():
	cls()
	print "Thanks for playing!"
	play = raw_input("Would you like to play again? y/n: ")
	if play == "y" or play == "Y":
		start_game()
	return

# Controls the levels of the game. Input is difficulty. Blank return. 
def run_levels(difficulty):
	game_levels = get_madlib(difficulty)
	level = 0
	while level < 3:
		current_level = game_levels[level]
		answer_list = current_level[1]
		madlib = "".join(current_level[0])
		fill_in_blanks(madlib, answer_list, level)
		level += 1
		user_pause()
	play_again()
	return

# Handles the blanks and user input. Inputs are the madlib, corresponding answers, and the level the user is up to.
def fill_in_blanks(madlib, answer_list, level):
	question = 0
	wrong_count = 3
	while question < len(answer_list):
		display_madlib(madlib, level)
		user_answer = raw_input("\n\n\nWhat is the answer for number " + str(question+1) + "? ")
		if user_answer == answer_list[question] or user_answer == "cheat":                
			madlib = reveal_words(madlib, answer_list[question], question)
			question += 1
			wrong_count = 3
		else:
			wrong_count -= 1
			print "Sorry, try again.", wrong_count, "tries left."
			if wrong_count == 0:
				print "The correct answer is", answer_list[question]
		user_pause()
	display_madlib(madlib, level)
	print "\nCongratulations! You completed level " + str(level + 1) + "!"
	return 

# Begins the game. No inputs. Gets user desired difficulty.
def start_game():
	cls()
	user_difficulty = 0
	while user_difficulty < 1 or user_difficulty > 3:
		user_difficulty = input("Please enter desired difficulty (1-3): ")
		if user_difficulty < 1 or user_difficulty > 3:
			print "Error. Please try again."
	run_levels(user_difficulty)
	return

start_game()
