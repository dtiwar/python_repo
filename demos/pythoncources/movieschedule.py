
import pandas as pd
current_movies={'kal ho na ho': '11:00 am',
                'Don': '1:00 pm',
                'forest gump': '3:00 pm',
                'Appollo 13': '5:00 pm'
                }
print('we are currently showing following moview')
count=1
for moviews in current_movies:
    print(f"{count}.{moviews}")
    count+=1
selected_moviews= input("which moview you would like to book \n> ")
print(selected_moviews)

showtime = current_movies.get(selected_moviews)

if not showtime :
    print("the requested moview is not in the playlist")
else:
    print(f"{selected_moviews} is playing at {showtime}")



