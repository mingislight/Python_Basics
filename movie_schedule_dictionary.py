current_moves = {}

current_moves['The Grinch'] = '11:00am'
current_moves['Rudolph'] = '1:00pm'
current_moves['Frosty the Snowman'] = '3:00pm'
current_moves['Christmas Vacation'] = '5:00pm'

print("We are showing the following movies:")
for key in current_moves:
    print(key)

movie = input('What movie would you like the showtime for?\n')

showtime = current_moves.get(movie)

if showtime == None:
    print("Requested movie isn't playing")
else:
    print(movie, 'is playing at ', showtime)