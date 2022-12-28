# Open Trivia DB:

In order to add more questions to this quiz that we've created, we 
can go to the [Open Trivia Database](https://opentdb.com/) and 
access their API (found [here](https://opentdb.com/api_config.php)).

Using the API, we can select & set:
* Number of Questions
* Trivia Category
* Trivia Difficulty
* Trivia Question Type
* API Encoding Type

Once we have made our selections (**Encoding Type** should be set to 
"_Default Encoding_"), we simply have to click the "_Generate URL_" 
button, then navigate to that address. The data on-screen will be in 
the **.json** format. This data can actually be copied & pasted into 
our _data.py_ file. From there, we need to select all of the pasted 
data and, in PyCharm, use _Code_ --> _Reformat Code_. We need to do 
this **TWICE** to correctly have the .json data converted to usable 
Python code.

Be aware that after the importing/formatting process, the key/value 
pairs of the imported data will be different than our original 
example, so the objects/Classes that we've created (along with their 
methods & attributes) need to be edited to reflect this new data.

First, we need to ensure that the imported data is enclosed in a 
list. We can also delete the key/value pairs of "_response_code_" & 
"_results_".

Next, the remaining dictionaries have 5 sets of key/value pairs each;
for our purposes, we are interested in the "_question_" and 
"_correct_answer_" values.