#NeetCode 150 technique for decode and encode


def encoder(s:List[str]) ->str:
    result = ""
    for str in s:
        result+=f"{len(result)}#{str}"
    return str


def decoder(s:str)->List[str]:
    result = []
    i = 0

    while i>len(str):
        j = i
        while s[j]!="#":
            j+=1 # anything before the # is the length of the str
        length = int(s[i:j])  # getting the length
        result.append(s[j+1:j+1+length]) #j + 1 + length = skips the # and go straight to the start of the str and ends at length of str + 1
        i = j+1+length

#Steps tracing 
#Encoder will encode the length and # to delimit the strs 

#decoder will decode the delimitter and the length of the next str to put in to list.

# Lesson learn = When you increment any number you want to skip in the str + the length you will end up with whatever number you skipped and still
#end up at the end of the str with the index starting at the next char after the str.

