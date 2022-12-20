string = "20*2/3" 

list_numbers=[]
list_characters=[]
number=""
for nums in string: 
     if nums == "*" or nums=="+" or nums=="-" or nums=="/":
        list_characters+=[nums] 
        list_numbers+= [number]
        number="" 
     else:
        number+=nums
list_numbers+= [string[-1]]
print(list_numbers) 
print(list_characters) 

ans = 20*2/3 
print(ans)

