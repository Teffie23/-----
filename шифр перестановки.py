def main():
    mymessage='hello igor tyrin '
    mykey=4
    chiptext=entry(mymessage,mykey)
    print(chiptext +'|')
def entry(message,key):
    chiptext=['']*key
    for column in range(key):
        cur=column
        while cur < len(message):
            chiptext[column] += message[cur]
            cur +=key
            
    return ''.join(chiptext)       
main()
