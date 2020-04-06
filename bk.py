products = []
while True:
	name = input('商品名稱: ')
	if name == 'q':
		break
	price = input('商品價格: ')
	p = [name, price]
	products.append(p)
for pro in products:
	print(pro[0], '的價格是', pro[1], '元')

# products[0][0] 第一大框裡的第一小框

with open('products.csv', 'w') as f:
	f.write('商品, 價格, \n')
	for pro in products:
		f.write(pro[0] + ',' + pro[1] + '\n')