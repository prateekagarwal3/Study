restaurants = {}
f = open('restaurantDatabase.txt')

for res in f.readlines():
    res = res.split('\t')
    restaurants[res[0].lower()] = {"number":res[1].lower(), "foodtype":res[2].lower(), "price":res[3].lower(), "location":res[4].split('\n')[0].lower()}

# print(restaurants)
foodTypes = ["chinese", "japanese", "mexican", "italian", "greek"]
prices = ["cheap", "medium-priced", "expensive"]
locations = ["marina del ray", "korea town", "venice", "playa vista", "santa monica", "hollywood"]

def process_input(ip):
    any_found = False
    ft = None
    p = None
    l = None

    if ip.find("any") != -1:
        any_found = True

    for i in foodTypes:
        if ip.find(i) != -1:
            ft = i
            break

    for i in prices:
        if ip.find(i) != -1:
            p = i
            break

    for i in locations:
        if ip.find(i) != -1:
            l = i
            break
    return any_found, ft, p, l

def process_confirmation_ip(ip):
    if ip.find("Yes") != -1:
        return 1
    else:
        return 0
    
while(1):
    print("What type of restaurant do you want?")
    ip = raw_input()
    any_found, ft, p, l = process_input(ip)

    if ft is None and any_found is False:
        continue
    else:
        print("You said you want {} restaurant?".format(ft))
        ip = raw_input()
        ft_confirm = process_confirmation_ip(ip)
        print(ft_confirm)
    
    if ft_confirm is 0:
        continue
    
