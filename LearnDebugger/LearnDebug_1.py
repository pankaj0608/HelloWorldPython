strHtml = "<b>fo o</b>"
inTag=False;
out="";

for c in strHtml:
    if c == "<":
        inTag = True
    elif c == ">":
        inTag = False
    elif inTag == False:
        out = out + c

print("out : ", out)