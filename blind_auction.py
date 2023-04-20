from replit import clear

#Printing logo
from art import logo
print(logo)

auction = {}

continue_bid = True

while continue_bid:
  bidder = input(f"What is your name?: ")
  bid_val = int(input(f"What is your bid?: $"))
  
  auction[bidder] = bid_val
  
  question = input(f"Are there any other bidders? Type 'yes' or 'no'.")

  if question == 'no':
    highest_bid = max(auction.values())
    
    for key in auction:
       if highest_bid == auction[key]:
         print(f"The winner is {key} with a bid of ${highest_bid}")
    #print(auction)    
    continue_bid = False
  else:
    clear() #For replit page