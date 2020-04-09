import os # operating system

# 讀取檔案
def read_file(filename):
    products = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if '商品, 價格' in line:
                continue
            name, price = line.strip().split(',')
            products.append([name, price])
    return products

# 輸入商品
def user_input(products):
    while True:
        name = input('商品名稱: ')
        if name == 'q':
            break
        price = input('商品價格: ')
        products.append([name, price])
    return products

# 印出紀錄
def print_products(products):
    for p in products:
        print(p[0], '的價格是', p[1], '元')

# products[0][0] 第一大框裡的第一小框

# 寫入檔案
def write_file(filename, products):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('商品, 價格 \n')
        for p in products:
            f.write(p[0] + ',' + p[1] + '\n')


def main():
    filename = 'products.csv'
    if os.path.isfile(filename):
        print('fuck yea boi')
        products = read_file(filename)
    else:
        print('nah man')

    products = user_input(products)
    print_products(products)
    write_file('products.csv', products)

main()