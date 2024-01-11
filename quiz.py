import random
quiz ={"Q1":"What's my name","Q2":"What's my birth date","Q3":"What's my hight","Q4":"What's my phone",
"Q5":"What's my laptop","Q6":"What's my last name","Q7":"What's the most hated thing for me","Q8":"What's my favourite food","Q9":"What's my age" };
quizAnswers={"Q1":"Ziad","Q2":"8-6-2002","Q3":"175","Q4":"Galaxy","Q5":"Surface pro","Q6":"Barnawi","Q7":"Cockaroch","Q8":"Pizza","Q9":"21"};
selectedQ=[];
selectedAnswers=[];
score=0;
x=0;
while len(selectedQ)<3:
    questionIndex=random.randint(1, 9)
    question =quiz[f"Q{questionIndex}"];
    if question in selectedQ:
        continue
    else:
        selectedQ.append(question);
        selectedAnswers.append(quizAnswers[f"Q{questionIndex}"])
for i in selectedQ:
    
    print(i)
    answer=input("your answer: ");
    if answer==selectedAnswers[x]:
        score+=1
    x+=1;
    
print(score);