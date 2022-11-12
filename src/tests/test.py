

table_size_ref = "A13:C16"
builder = table_size_ref.split(":")

final = ""
for i,v in enumerate(builder):
    
    if v[1].isalpha():
        cur_string = v[0:2] + str(int(v[2:]) + 3)
    else:
        cur_string = v[0] + str(int(v[1:]) + 3)
    
    if i != 1:
        final += (cur_string) + ":"
    else:
        final += (cur_string)
        
    cur_string = ""

print(final)
    