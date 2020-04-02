products = []
while True:
	name = input('你買什麼辣: ')
	if name == 'q':
		break
	price = input('多少錢捏: ')
	p = [name, price]
	products.append(p)
for p in products:
	print(p[0], '的價格是', p[1], '元')

# products[0][0] 第一大框裡的第一小框