#!/usr/bin/env python3

question_data = [
    {"category": "Entertainment: Television",
     "type": "boolean",
     "difficulty": "medium",
     "question": "On AMC's 'The Walking Dead', Rick, "
                 "Carl, Daryl, Morgan, Carol and Maggie were "
                 "introduced to us in Season 1.",
     "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "Science & Nature",
     "type": "boolean",
     "difficulty": "medium",
     "question": "A person can get sunburned on a cloudy day.",
     "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Science & Nature",
     "type": "boolean",
     "difficulty": "medium",
     "question": "The Doppler effect applies to light.",
     "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Science: Computers",
     "type": "boolean",
     "difficulty": "medium",
     "question": "The common software-programming acronym "
                 "'I18N' comes from the term "
                 "'Interlocalization'.",
     "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "Animals",
     "type": "boolean",
     "difficulty": "medium",
     "question": "An octopus can fit through any hole larger than its "
                 "beak.",
     "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Geography",
     "type": "boolean",
     "difficulty": "medium",
     "question": "The flag of South Africa features 7 colours.",
     "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "Science: Mathematics",
     "type": "boolean",
     "difficulty": "medium",
     "question": "The Pythagorean theorem states that the square of "
                 "the hypotenuse is equal to the product of the "
                 "squares of the other two sides.",
     "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "Entertainment: Music",
     "type": "boolean",
     "difficulty": "medium",
     "question": "Soulja Boy's 'Crank That' won a "
                 "Grammy for Best Rap Song in 2007.",
     "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "History",
     "type": "boolean",
     "difficulty": "medium",
     "question": "The two atomic bombs dropped on Japan by the United "
                 "States in August 1945 were named 'Little "
                 "Man' and 'Fat Boy'.",
     "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "General Knowledge",
     "type": "boolean",
     "difficulty": "medium",
     "question": "'Typewriter' is the longest word that can "
                 "be typed using only the first row on a QWERTY "
                 "keyboard.",
     "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Geography",
     "type": "boolean",
     "difficulty": "medium",
     "question": "The surface area of Russia is slightly larger than "
                 "that of the dwarf planet Pluto.",
     "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Science: Computers",
     "type": "boolean",
     "difficulty": "medium",
     "question": "All program codes have to be compiled into an "
                 "executable file in order to be run. This file can "
                 "then be executed on any machine.",
     "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "Entertainment: Music",
     "type": "boolean",
     "difficulty": "medium",
     "question": "Norwegian producer Kygo released a remix of the "
                 "song 'Sexual Healing' by Marvin Gaye.",
     "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Sports",
     "type": "boolean",
     "difficulty": "medium",
     "question": "Soccer player Cristiano Ronaldo opened a museum "
                 "dedicated to himself.",
     "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Entertainment: Video Games",
     "type": "boolean",
     "difficulty": "medium",
     "question": "The first Maxis game to feature the fictional "
                 "language 'Simlish' was The Sims (2000).",
     "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "Entertainment: Music",
     "type": "boolean",
     "difficulty": "medium",
     "question": "The country song 'A Boy Named Sue' was "
                 "written by Shel Silverstein.",
     "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Geography",
     "type": "boolean",
     "difficulty": "medium",
     "question": "The longest place named in the United States is "
                 "Lake Chargoggagoggmanchauggagoggchaubunagungamaugg, "
                 "located near Webster, MA.",
     "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Science: Mathematics",
     "type": "boolean",
     "difficulty": "medium",
     "question": "111,111,111 x 111,111,111 = 12,345,678,987,654,321",
     "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Entertainment: Film",
     "type": "boolean",
     "difficulty": "medium",
     "question": "The colour of the pills in the Matrix were Blue and "
                 "Yellow.",
     "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "Science & Nature",
     "type": "boolean",
     "difficulty": "medium",
     "question": "Type 1 diabetes is a result of the liver working "
                 "improperly.",
     "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "Vehicles",
     "type": "boolean",
     "difficulty": "medium",
     "question": "The Chevrolet Corvette has always been made "
                 "exclusively with V8 engines only.",
     "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "General Knowledge",
     "type": "boolean",
     "difficulty": "medium",
     "question": "An eggplant is a vegetable.",
     "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "General Knowledge",
     "type": "boolean",
     "difficulty": "medium",
     "question": "Cucumbers are usually more than 90% water.",
     "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Sports",
     "type": "boolean",
     "difficulty": "medium",
     "question": "Tennis was once known as Racquetball.",
     "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "General Knowledge",
     "type": "boolean",
     "difficulty": "medium",
     "question": "The average woman is 5 inches shorter than the "
                 "average man.",
     "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Entertainment: Video Games",
     "type": "boolean",
     "difficulty": "medium",
     "question": "In 'Team Fortress', "
                 "the 'Bill's Hat'; is a reference to "
                 "the game 'Dota 2'.",
     "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "Science: Computers",
     "type": "boolean",
     "difficulty": "medium",
     "question": "AMD created the first consumer 64-bit processor.",
     "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Geography",
     "type": "boolean",
     "difficulty": "medium",
     "question": "'Mongolia' was a part of the now "
                 "non-existent U.S.S.R.",
     "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "Animals",
     "type": "boolean",
     "difficulty": "medium",
     "question": "The average lifespan of a wildcat is only around "
                 "5-6 years. ",
     "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "Entertainment: Music",
     "type": "boolean",
     "difficulty": "medium",
     "question": "'Twenty One Pilots' made the song "
                 "'The Motion' featuring Sampha.",
     "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "Geography",
     "type": "boolean",
     "difficulty": "medium",
     "question": "Liechtenstein does not have an airport.",
     "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Entertainment: Music",
     "type": "boolean",
     "difficulty": "medium",
     "question": "For his performance at ComplexCon 2016 in Long "
                 "Beach, California, Skrillex revived his "
                 "'Mothership' set piece for one night only.",
     "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Entertainment: Video Games",
     "type": "boolean",
     "difficulty": "medium",
     "question": "Mortal Kombat was almost based on Jean-Claude Van "
                 "Damme movie.",
     "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "General Knowledge",
     "type": "boolean",
     "difficulty": "medium",
     "question": "Fast food restaurant chains Carl's Jr. and "
                 "Hardee's are owned by the same company.",
     "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Entertainment: Video Games",
     "type": "boolean",
     "difficulty": "medium",
     "question": "In Monster Hunter Generations, guild style is a "
                 "type of hunting style.",
     "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Entertainment: Cartoon & Animations",
     "type": "boolean",
     "difficulty": "medium",
     "question": "Nickelodeon rejected the pilot to Adventure Time.",
     "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Entertainment: Music",
     "type": "boolean",
     "difficulty": "medium",
     "question": "Pink Guy's debut album was 'Pink "
                 "Season'.",
     "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "Entertainment: Video Games",
     "type": "boolean",
     "difficulty": "medium",
     "question": "In the video game 'Transistor', "
                 "'Red' is the name of the main character.",
     "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Science: Mathematics",
     "type": "boolean",
     "difficulty": "medium",
     "question": "A 'Millinillion' is a real number.",
     "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Entertainment: Television",
     "type": "boolean",
     "difficulty": "medium",
     "question": "Klingons once had a period of Democracy in their "
                 "history, they referred to it as the 'Dark "
                 "Times'.",
     "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Entertainment: Television",
     "type": "boolean",
     "difficulty": "medium",
     "question": "In 'Star Trek', Klingons are commonly "
                 "referred to as 'Black Elves'.",
     "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "Sports",
     "type": "boolean",
     "difficulty": "medium",
     "question": "Wilt Chamberlain scored his infamous 100-point-game "
                 "against the New York Knicks in 1962.",
     "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Entertainment: Video Games",
     "type": "boolean",
     "difficulty": "medium",
     "question": "In 'League of Legends', there exists four "
                 "different types of Dragon.",
     "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "Science & Nature",
     "type": "boolean",
     "difficulty": "medium",
     "question": "Pneumonoultramicroscopicsilicovolcanoconiosis is a "
                 "synonym for the disease known as silicosis.",
     "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "General Knowledge",
     "type": "boolean",
     "difficulty": "medium",
     "question": "The scientific name for the Southern Lights is "
                 "Aurora Australis?",
     "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Entertainment: Cartoon & Animations",
     "type": "boolean",
     "difficulty": "medium",
     "question": "Donald Duck played the role of Bob Cratchit in "
                 "Disney's 1983 adaptation of A Christmas Carol.",
     "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "Geography",
     "type": "boolean",
     "difficulty": "medium",
     "question": "The title of the 1969 film 'Krakatoa, East_of "
                 "Java' is incorrect, as Krakatoa is in fact west "
                 "of Java.",
     "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Science: Computers",
     "type": "boolean",
     "difficulty": "medium",
     "question": "A Boolean value of '0' represents which of "
                 "these words?",
     "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "Entertainment: Film",
     "type": "boolean",
     "difficulty": "medium",
     "question": "The original ending of 'Little Shop Of "
                 "Horrors' has the plants taking over the world.",
     "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Entertainment: Video Games",
     "type": "boolean",
     "difficulty": "medium",
     "question": "In 'Resident Evil', only Chris has access "
                 "to the grenade launcher.",
     "correct_answer": "False",
     "incorrect_answers": ["True"]}]
