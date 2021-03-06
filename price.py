from pathlib import Path
from urllib.request import urlretrieve

base_url = "https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/data/"

# 저장위치 지정과 생성
data_path = Path() / "data"
data_path.mkdir(parents=True, exist_ok=True)

def myWget(filename):
    # 다운로드 대상 파일 경로
    file_url = base_url + filename

    # 저장 경로와 파일명
    target_path = data_path / filename

    return urlretrieve(file_url, target_path)


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
