def shopping(shop_file):
    shop_dict = {}
    with open(f"data/{shop_file}", mode='r', encoding='utf-8') as f:
        for line in f:
            shop_list = line.strip().split()
            if shop_list == []:
                pass
            elif shop_list[0] != '#쇼핑몰':
                name, score = shop_list[0], int(shop_list[1].replace("원", ""))
                shop_dict[name] = score


    return shop_dict

def item_price(shop_file, item):
    shop_dict = shopping(shop_file)
    price = shop_dict[item] 

    return price
