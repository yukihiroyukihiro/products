#二維清單
products = []
while True:
	name = input('請輸入商品名稱：')
	if name == 'q':
		break
	price = input('請輸入商品價格：')
	products.append(([name, price]))
print('印出清單裡所有的商品與價格：', products)#印出清單裡所有的商品與價格
print('印出清單0的所有的商品與價格',products[0]) #印出清單0的所有的商品與價格
print('印出清單[0][0] -> 清單0的商品：', products[0][0]) #印出清單[0][0] -> 清單0的商品
print('印出清單[0][1] -> 清單0的價格：', products[0][1]) #印出清單[0][1] -> 清單0的價格

#用for loop一行一行印出products
print('------------------')
print('一行一行印出清單：')
for p in products:
	print(p)


#用for loop一行一行印出products
print('------------------')
print('一行一行印出清單的商品與價格：')
for p in products:
	print(p[0], '的價格是', p[1])


with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品' + ',' + '價格' + '\n') #檔案先加入Title，寫成f.write('商品,價格\n')也行
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')



