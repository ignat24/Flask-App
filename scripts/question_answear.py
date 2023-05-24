import re
import random

answear_mass = []

with open("quest.txt", "r") as question:
    text = question.readlines()

with open("answear.txt", "r") as answear:
    ans = answear.readlines()

def random_answear():
    count = random.randint(0, len(ans)) - 1 
    return ans[count]

    

for i in range(40):
    quest_random = random.randint(0, len(text)) - 1
    quest = re.sub("\n", "", text[quest_random])
    text.remove(text[quest_random])
    ans_random = random_answear()
    ans.remove(ans_random)
    ans_random = re.sub("\n", "", ans_random)
    
    print(quest + ans_random)
    if i % 5 == 0:
        print()
    # input()
    
    

    