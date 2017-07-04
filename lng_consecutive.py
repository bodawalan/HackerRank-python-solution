# Write a function to find the longest number of consecutive appearances of a
# character in a string
#     for example: 'fzccsawetaaafb' => (a, 3)


my_str = str(input("enter the string:"))
last_char = ""
current_seq_len = 0
max_seq_len = 0
new_len_list=[]
new_ch_list=[]

for c in my_str:
    if c == last_char:
        current_seq_len += 1
        if current_seq_len > max_seq_len:
            max_seq_len = current_seq_len
            new_ch_list.append(c)
            new_len_list.append(max_seq_len)
    else:
        current_seq_len = 1
        last_char = c

print(max_seq_len)
print(new_len_list,new_ch_list)

print((new_len_list[-1],new_ch_list[-1]))