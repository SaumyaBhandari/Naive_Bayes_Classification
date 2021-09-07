def getUniqueWords(allWords) :
    uniqueWords = [] 
    for i in allWords:
        if not i in uniqueWords:
            uniqueWords.append(i)
    return len(uniqueWords)

data_words ={
                "Sports"    : ["Goal is scored", "A clean but forgetable goal", "A very clean match", "First goal of the match", "Team A won the match with n goals"],
                "Politics": ["Election is complete", "It was a close election", "A lost the election", "Minister Resigned from the office.", "A won the election with n votes"]
            }

classify = input()


temp_list_sports = []
temp_list_politics = []
sports_words = []
politics_words = []


for i in data_words:
    if i == "Sports":
        temp_list_sports += data_words[i]
    else:
        temp_list_politics += data_words[i]


for i in temp_list_sports:
    sports_words += i.lower().split()

for i in temp_list_politics:
    politics_words += i.lower().split()


unique_words = getUniqueWords(politics_words) + getUniqueWords(sports_words)
p_of_classify_in_sports = 1
p_of_classify_in_politics = 1

for i in classify.lower().split():
    p_of_classify_in_sports *= (sports_words.count(i)+1)/(len(sports_words)+unique_words)
    p_of_classify_in_politics *= (politics_words.count(i)+1)/(len(politics_words)+unique_words)

if p_of_classify_in_sports > p_of_classify_in_politics:
    data_words["Sports"].append(classify)
    print("\nThe given statement may belong to sports category.\n")
else:
    print("\nThe given statement may belong to politics category.\n")
    data_words["Politics"].append(classify)

print(data_words,"\n")