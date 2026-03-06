people_info = {}

def info(people_info):
    ask_name = input("Name of the bidder?\n").strip().lower() #key(string)
    ask_amt = abs(int(input("The Bidding Amount : $").strip())) #value(+integer)
    people_info[ask_name] = ask_amt

def max_bid(people_info):
    # highest_bid = 0
    # highest_bidder = ""
    # for person in people_info:
    #     if people_info[person] > highest_bid :
    #         highest_bid = people_info[person]
    #         highest_bidder = person
        
    # can also use max() function : 
    winner = max(people_info, key=people_info.get)
    print(f"The Highest Bidder : {winner} with the highest bidding amount: ${people_info[winner]}") 

    
#storing the name with their respective bid, inside the dictionary:
info(people_info)

#asking : are there more people involving in bidding?
proceed = input("Are there more people who want to bid? : type 'yes' or 'no' : ")

while proceed == "yes":
    print("\n" * 20)
    info(people_info)
    proceed = input("Are there more people who want to bid? : type 'yes' or 'no' : ")

print("Winner!! :")
max_bid(people_info)




