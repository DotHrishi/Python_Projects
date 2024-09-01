from replit import clear
#HINT: You can call clear() to clear the output in the console.
participants=[]

def add_participant(name,bid):
  new_participant={}
  new_participant[name]=bid
  participants.append(new_participant)

print("Welcome to the secret auction program.")
name=input("What is your name?: ")
bid=int(input("What's your bid?: $"))
add_participant(name,bid)
other_bidders=input("Are there any other bidders?")
while other_bidders=="yes":
  clear()
  name=input("What is your name?: ")
  bid=int(input("What's your bid?: $"))
  add_participant(name,bid)
  other_bidders=input("Are there any other bidders?")

max_bid=0
for participant in participants:
  for key in participant:
    if participant[key]>max_bid:
      max_bid=participant[key]
      winner=key
print(f"The winner is {winner} with a bid of ${max_bid}")

  