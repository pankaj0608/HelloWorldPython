strHtml = "<b>fo o</b>"
inTag=False;
out="";

for c in strHtml:
    if c == "<":
        inTag = True
    elif c == ">":
        inTag = False
    elif not inTag:
        out = out + c

print("out : ", out)