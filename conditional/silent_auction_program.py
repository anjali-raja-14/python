import os
def find_winner(bidder_details):
    highest_bid = 0
    winner = ""
    for bidder in bidder_details:  # jenny
        bidding_price = bidder_details[bidder]
        if (bidding_price > highest_bid):  # 10000
            highest_bid = bidding_price
            winner = bidder
    print(f"The winner is {winner} with a bid of {highest_bid}")

bidder_data = {}

end_of_bidders = False
while not end_of_bidders:
    name = input("What is your Name?: ")
    price = int(input("What is your bid? "))
    bidder_data[name] = price
    more_bidders = input("Do you have any bidders?: Type 'yes'or 'no'\n")

    if more_bidders == 'no':
        end_of_bidders = True
        find_winner(bidder_data)
        print(bidder_data)#print dictionary of all data

    elif more_bidders == 'yes':
        os.system('cls')

