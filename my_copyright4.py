from datetime import date
TODAY = str(date.today())

def my_copyright4(name, email, date=TODAY):
    line1 = "***  programmed by "+name+ " for MSDM5002  ***"
    length = len(line1)
    line3 = 'date: '+ date
    text_length = length - 10    
    
    if (length - (len(line3)+6)) % 2 == 1:
        space_gap1 = (length - (len(line3)+6)) // 2
        space_gap2 = (length - (len(line3)+6)) // 2 + 1
    else:
        space_gap1 = (length - (len(line3)+6)) // 2
        space_gap2 = (length - (len(line3)+6)) // 2
        
    line4 = '***' + '-' * (length - 6) + '***'
    
    text = 'You can use it as you like, but there might be many bugs. If you\
 find some bugs, please send them to "'+email+'""'
    word_list = text.split(' ')
            
    print("*" * length)
    print(line1)
    print('***'+' '*space_gap1+line3+' '*space_gap2+'***')  #center!
    print(line4)

    while word_list :
        i = 0 
        current_length = 0
        while(current_length <= text_length):
            i += 1
            current_length = 0
            
            for j in range(i):
                if j < len(word_list):                    
                    if j == 0: 
                        current_length += (len(word_list[j]))
                    else:
                        current_length += (len(word_list[j])+1)
                else:
                    current_length = text_length + 1
                    break
                        
        line11 =''
        for j in range(i-1):
            if j == 0:
                line11 += (word_list[j])
            else:
                line11 += (' '+word_list[j])
            
        
        del word_list[0:i-1]
        
        if len(word_list) == 1: #the situation that email it too long
            remaining = word_list[0][(text_length-len(line11)-1):len(word_list[0])-1]
            line11 += ' '+word_list[0][0:(text_length-len(line11)-1)]
            print('***  '+line11+'  ***')
            
            if len(remaining) <= text_length:
                print('***  '+remaining+' '*(text_length-len(remaining))+'  ***')
                del word_list[0]
            else:
                while(len(remaining) > text_length):
                    print('***  '+remaining[0:text_length]+'  ***')
                    remaining = remaining[text_length:]
                if len(remaining) <= text_length:
                    print('***  '+remaining+' '*(text_length-len(remaining))+'  ***')
                    print("*" * length)
                    return #that is the end!
                
        else:
            line11 += ' '*(text_length-len(line11))
            print('***  '+line11+'  ***')
                
    #ending--------------------------------        
    print("*" * length)
         
    return