print("***************************************************")
print("*****!!! Welcome to the Student's Election !!!*****")
print("***************************************************")

candidate1=input("Please Enter the 1st Canddate name = ")

candidate2=input("Please Enter the 2nd Canddate name = ")

print("*****************************************************")
print("*****!!! All the best to the both Candidates !!!*****")
print("*****************************************************")

cand1_votes=0
cand2_votes=0

voters_id=[101,102,103,104,105,106,107,108,109,110]
no_of_voters=len(voters_id)
print("No. of Voters:",no_of_voters)

voted=[]

while 1:
    if voters_id==[]:
        print("*******!!!! Voting is Ended !!!!*******")
        if cand1_votes>cand2_votes:
            print("*****!!!! Here's the result of this Election !!!!*****")
            print(f"*****!!!! The winner of this Eletion is '{candidate1}' !!!!*****")
            print(f"*****!!!! '{candidate1}' Won the election by {cand1_votes} votes !!!!*****")
            print(f"*****!!!! '{candidate2}' Loose the election by {cand2_votes} votes !!!!*****")
            print(f"*****!!!! Congratulations 'Mr. {candidate1}' for being the new President of 'laxmanChartered Institute of Technology, Abu Road'  !!!!*****")
            break
        elif cand2_votes>cand1_votes:
            print("*****!!!! Here's the result of this Election !!!!*****")
            print(f"*****!!!! The winner of this Eletion is '{candidate2}' !!!!*****")
            print(f"*****!!!! '{candidate2}' Won the election by {cand2_votes} votes !!!!*****")
            print(f"*****!!!! '{candidate1}' Loose the election by {cand1_votes} votes !!!!*****")
            print(f"*****!!!! Congratulations 'Mr. {candidate2}' for being the new President of 'Chartered Institute of Technology, Abu Road' !!!!*****")
            break
        elif cand1_votes==cand2_votes:
            print("It's a Tied")
            break
    else:
        voter=int(input("\nEnter your voter Id: "))
        if voter in voted:
            print("Your already voted !!!!")
        elif voter in voters_id:
            print(f" 1. {candidate1}\n 2. {candidate2}\n")
            choise=int(input("Enter your choise whom you want to vote: "))

            if choise==1:
                print(f"You voted {candidate1} !!\n")
                cand1_votes+=1
                voters_id.remove(voter)
                voted.append(voter)

            elif choise==2:
                print(f"You voted {candidate2} !!\n")
                cand2_votes+=1
                voters_id.remove(voter)
                voted.append(voter)
            
            else:
                print("You have entered a wrong choise which doesn't exist !!!!")

        else:
            print("You are not allowed to vote\n")