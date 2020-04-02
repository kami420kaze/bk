products = []
while True:
	name = input('你買什麼辣: ')
	if name == 'q':
		break
	price = input('多少錢捏: ')
	p = [name, price, '元']
	products.append(p)

print(products)

# products[0][0] 第一大框裡的第一小框