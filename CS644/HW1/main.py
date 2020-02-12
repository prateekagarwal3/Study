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
    ip = ip.lower()
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
    ip = ip.lower()
    if ip.find("yes") != -1:
        return 1
    else:
        return 0
    
ft_confirm = False
p_confirm = False
l_confirm = False

while(1):
    if ft_confirm is False:
        print("What type of restaurant do you want?")
        ip = raw_input()
        any_found, ft, p, l = process_input(ip)

        if ft is None and any_found is False:
            continue
        else:
            print("You said you want {} restaurant?".format(ft))
            ip = raw_input()
            ft_confirm = process_confirmation_ip(ip)
            print("confirmation:", ft_confirm)
        
        if ft_confirm is 0:
            continue

    if p_confirm is False:
        print("How expensive a restaurant do you want?")
        ip = raw_input()
        any_found, ft, p, l = process_input(ip)

        if p is None and any_found is False:
            continue
        else:
            print("You said you want {} restaurant?".format(p))
            ip = raw_input()
            p_confirm = process_confirmation_ip(ip)
            print("confirmation:", p_confirm)
        
        if p_confirm is 0:
            continue

    if l_confirm is False:
        print("Ok where do you want the restaurant to be located?")
        ip = raw_input()
        any_found, ft, p, l = process_input(ip)

        if l is None and any_found is False:
            continue
        else:
            print("You said you want restaurant in {}?".format(l))
            ip = raw_input()
            l_confirm = process_confirmation_ip(ip)
            print("confirmation:", l_confirm)
        
        if l_confirm is 0:
            continue