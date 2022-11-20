qua={"hello": "hi","how are you ": "fine","where are you live" :"spain"
                                                                }
while True:
    try :
             wrt=input()

             if wrt == 'quit' :
            break
           else :
          print(qua[wrt])

     except :
          print("try again")

