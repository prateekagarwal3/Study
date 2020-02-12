restaurants = {}
f = open('restaurantDatabase.txt')

for res in f.readlines():
    res = res.split('\t')
    restaurants[res[0].lower().strip()] = {"mobile":res[1].lower().strip(), "foodtype":res[2].lower().strip(), "price":res[3].lower().strip(), "location":res[4].split('\n')[0].lower().strip()}

print(restaurants)

foodTypes = set()
prices = set()
locations = set()

for k in restaurants.keys():
    foodTypes.add(restaurants[k]["foodtype"])
    prices.add(restaurants[k]["price"])
    locations.add(restaurants[k]["location"])

def process_confirmation_ip(ip):
    ip = ip.lower().strip()
    if ip.find("yes") != -1:
        return 1
    else:
        return 0
    
def process_ft_input(ip, ft, p, l):
    ip = ip.lower().strip()

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
    if ft is None:
        if ip.find('any') != -1:
            ft = 'any'
    return ft, p, l

def process_p_input(ip, ft, p, l):
    ip = ip.lower().strip()

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
        
    if p is None:
        if ip.find('any') != -1:
            p = 'any'

    return ft, p, l

def process_l_input(ip, ft, p, l):
    ip = ip.lower().strip()

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
        
    if l is None:
        if ip.find('any') != -1:
            l = 'any'

    return ft, p, l

def get_foodtype(ft, p, l):
    while(1):
        if ft is None:
            print("What type of restaurant do you want?")
            ip = raw_input()
            ft, p, l = process_ft_input(ip, ft, p, l)

        if ft is None:
            continue
        else:
            print("You said you want {} foodtype restaurant?".format(ft))
            ip = raw_input()
            ft_confirm = process_confirmation_ip(ip)
        
        if ft_confirm == 0:
            ft = None
            continue
        else:
            return ft, ft_confirm, p, l

def get_price(ft, p, l):
    while(1):
        if p is None:
            print("How expensive a restaurant do you want?")
            ip = raw_input()
            ft, p, l = process_p_input(ip, ft, p, l)

        if p is None:
            continue
        else:
            print("You said you want {} priced restaurant?".format(p))
            ip = raw_input()
            p_confirm = process_confirmation_ip(ip)
        
        if p_confirm is 0:
            p = None
            continue
        else:   
            return ft, p_confirm, p, l
        
def get_location(ft, p, l):
    while(1):
        if l is None:
            print("Ok where do you want the restaurant to be located?")
            ip = raw_input()
            ft, p, l = process_l_input(ip, ft, p, l)

        if l is None:
            continue
        else:
            print("You said you want restaurant in {} location?".format(l))
            ip = raw_input()
            l_confirm = process_confirmation_ip(ip)
        
        if l_confirm is 0:
            l = None
            continue
        else:   
            return ft, l_confirm, p, l

def show_results(ft, p, l):
    results = []
    if ft is not 'any':
        for k in restaurants.keys():
            if restaurants[k]["foodtype"] == ft:
                results.append(k)
    else:
        for k in restaurants.keys():
            results.append(k)
    
    for k in results:
        print(k, restaurants[k])
    
    temp = results
    if p is not 'any':
        for k in temp:
            if restaurants[k]['price'] != p:
                print(restaurants[k]['price'], p)
                print('price not matching')
                print('res:', results)
                results.remove(k)
                print('res after removal:', results)
    print(results)        
    
    temp = results
    if l is not 'any':
        for k in temp:
            if restaurants[k]['location'] != l:
                results.remove(k)
    print(results)
    
    print("Restaurants found based on your preferences of {} foodtype {} priced restaurant in {} location are as follows: ".format(ft, p, l))
    for k in results:
        print(k, restaurants[k]["mobile"], restaurants[k])

def fill_slots():
    ft = None
    p = None
    l = None
    ft, ft_confirm, p, l = get_foodtype(ft, p, l)    
    ft, p_confirm, p, l = get_price(ft, p, l)
    ft, l_confirm, p, l = get_location(ft, p, l)
    return ft, ft_confirm, p, p_confirm, l, l_confirm

ft, ft_confirm, p, p_confirm, l, l_confirm = fill_slots()
print(ft, ft_confirm, p, p_confirm, l, l_confirm)

show_results(ft, p, l)