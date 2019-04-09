#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#know_our_bonding_game

print('Hello, guys')
ans=input('Are you ready to play {yes/no}:')
score=0
number_of_questions=5
if ans.lower()=='yes':

#first_question
    ans=input(' My favorite sport ').lower()
    if ans.lower()=='football':
        score=score+1
        print('Correct')
    else:
        print('incorrect')
        
#second_question       
    ans=input(' My favorite mobile game ')
    if ans.lower()=='pubg':
        score=score+1
        print(' Correct')
    else:
        print(' Incorrect ')
        
#Third_question 

    ans=input('How old I am ?')
    if ans=='19':
        score=score+1
        print('Correct')
    else:
        print('incorrect')
        
#Fourth_question   

    ans=input(' My birthday? ')
    if ans.lower()=='18 august':
        score=score+1
        print('Correct')
    else:
        print('incorrect')
        
#Fifth_question       
    ans=input(' My favorite hollywood movie? ')
    if ans.lower()=='avengers':
        score=score+1
        print('Correct')
    else:
        print('incorrect')
#Sixth_question
    ans=input(' My favorite bollywood movie? ')
    if ans.lower()=='3 idiots':
        score+=1
        print(' Correct ')
    else:
        print(' Incorrect ')

#Seventh_question
    ans=input(' My favorite book? ')
    if ans.lower()== 'the kite runner':
        score+=1
        print(' Correct ')
        
    else:
        print(' Incorrect ')

#Eight_question

    ans=input(' My favorite color?' )
    if ans.lower()=='black':
        score+=1
        print(' Correct ')
    else:
        print(' Incorrect ')
        
#Ninth_question

    ans=input(' My favorite food? ')
    if ans.lower()== "dal chawal" or "dal rice" or 'rice pulses':
        score+=1
        print(' Correct ')
    else:
        print(' Incorrect ')

#Tenth_question
    ans=input(' What is my nickname ')
    if ans.lower()== 'arru':
        score+=1
        print(' Correct ')
        
    else:
        print(' Incorrect ')      
        
print(' Thank you for playing, your score is ' + str(score))

#adding_comment_on_score

if score>=9:
    print(' Awesome!, I am glad ')
elif score>5 or score<8:
    print('Wow!, Good knowledge about me ')
elif score==4 or score==3:
    print (' Woah! Not bad ')
else:
    print("'Oh! Sad :( ")


# In[ ]:





# In[ ]:




