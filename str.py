def find_prefix(str_list: list) -> str:
    bank = []
    length = len(str_list)
    for str in str_list:
        for x in str:   
                if x in str_list[length-1]:
                    bank.append(x)
        
    print(f"{bank}")
str_list = ["mikihjegad","mikiahsd","mikiahsdg"]       
find_prefix(str_list)

