#First we can get the input from the nominees
nominee1=input("Enter your name:")
nominee2=input("Enter your name:")

#Intially vote of each nominees will be zero till voting
nm1_votes=0
nm2_votes=0

#We should generate the all the valid voter id 
voter_id=[1,2,3,4,5,6]

#With voter_id we can find the no_of_candidates
no_of_voters=len(voter_id)
 
while voter_id!=[]:
    if voter_id==[]:#to check when voter list is completed
        print("voting session is over!!!")
        if nm1_votes>nm2_votes:
            percent=(nm1_votes/no_of_voters)*100 # to calculate the percentange
            print(nominee1,"Has won the election!! with",percent,"%")
            break
        elif nm2_votes>nm1_votes:
            percent=(nm2_votes/no_of_voters)*100 # to calculate the percentange
            print(nominee2,"Has won the election!! with",percent,"%")
            break
        else:
            print(nominee1," and ",nominee2 ,"have secured equal number of votes !! so,govermnet decide who will rule" )
            break
        
    voter=int(input("enter your voter id:"))
    if voter in voter_id:
        #Check wheather the enter voter_id is valid or not 
        #If it is valid print you can vote 
        print("your voter id is valid,You can vote")
        voter_id.remove(voter)#we can remove the current enter valid voter id so that the same voter can't vote
        print("*************************************************************")
        #Diplay the voting number of the candidate 
        print("To give vote to",nominee1,"press 1")
        print("To give vote to",nominee2,"press 2")
        print("*************************************************************")
        vote=int(input("Enter your prescious vote:"))
        if vote==1:
            nm1_votes +=1
            print(nominee1,"Thank you for registering your vote")
        elif vote==2:
            nm2_votes +=1
            print(nominee1,"Thank you for registering your vote")
        elif vote>2:
            print("invalid,check your pressed key!!")
        else:
            print("you are not a voter else you have voted already")
    
