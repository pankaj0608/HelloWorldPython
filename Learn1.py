from collections import *

import webbrowser
import time
import os

text = "Donald Trump’s leading economic adviser says the president wants " \
       "to strike separate, bilateral trade deals with Canada and Mexico rather" \
       " than continue renegotiating the North American Free Trade Agreement." \
       "Larry Kudlow, the director of Trump’s National Economic Council, says the " \
       "president indicated that preference to him when they spoke on Monday.Kudlow was " \
       "speaking Tuesday on the Fox News morning program, Fox and Friends.He also says he" \
       " relayed that message to a senior member of the Prime Minister " \
       "Justin Trudeau’s office.The remarks are likely to create more economic " \
       "uncertainty between Canada and the U.S. following Trump’s imposition " \
       "of steel and aluminum tariffs that now affect imports from this country," \
       " Mexico and Europe. Donalds pankaj pankaj pankaj pankaj pankaj pankaj pankaj"

words = text.split()

print(words)

counter = Counter(words)

top_five = counter.most_common(4)


# Hello
print(top_five)
print(top_five.__getitem__(1))

url = 'http://www.python.org/'

time.sleep(3)

# webbrowser.open_new_tab(url)
os.rename("./HelloMe1.py","./HelloMe.py" )