raw_ips = [
    "192.168.1.1", "10.0.0.5", "192.168.1.1", 
    "172.16.0.1", "10.0.0.5", "8.8.8.8"
]
def get_unique_ips(ips:list[str])-> list[str]:
    ips_unique = list(set(ips))
    return ips_unique
print(get_unique_ips(raw_ips))

#remember JSON only supports strings.numbers.bool,null,obj,dicts and lists not set. so you have to convert your return in to other data types if it is a set type to use it in a backend
