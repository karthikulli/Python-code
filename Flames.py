def flames_game(name1,name2):
    name1=name1.replace(" ","").lower()
    name2=name2.replace(" ","").lower()
    name1_list=list(name1)
    name2_list=list(name2)
    for char in name1[:]:
        if char in name2_list:
            name1_list.remove(char)
            name2_list.remove(char)
    count=len(name1_list)+len(name2_list)
    flames=['F','L','A','M','E','S']
    while len(flames)>1:
        index=(count%len(flames))-1
        if index>=0:
            flames=flames[index+1:]+flames[:index]
        else:
            flames.pop()
    result={
        "F":"FRIENDSHIP",
        "L":"LOVERS",
        "A":"ATTRACTION",
        "M":"MARRIAGE",
        "E":"ENEMIES",
        "S":"SIBBLINGS"
    }
    return result[flames[0]]
    
name1=input("Enter 1st name: ")
name2=input("\nEnter 2nd Name: ")
result=flames_game(name1,name2)
print("\nRelationship ends with :",result)
