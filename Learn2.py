import os
import MySquare as Teaser

counter = 0

while counter < 2:
    # if counter == 0:
    #     counter = counter + 1
    #     continue

    print("Hello 2")
    counter = counter + 1

print("Directory : " + os.getcwd())

# os.rename("./hsahd.py", "./HelloMe.py")

Teaser.Hello()