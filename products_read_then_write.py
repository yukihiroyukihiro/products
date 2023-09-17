import os #operating system

products = []

#讀取檔案
if os.path.isfile('products.csv'): #檢查相對路徑有沒有這個檔案
	print('有找到檔案！')
	with open('products.csv', 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue #結束這一回，直接去下一回
			name, price = line.strip().split(',') #strip() -> 去掉空格跟'\n'換行
			                                      #split',' -> 將字串逗號分割，變成清單存入s.
			products.append([name, price])
	print(products)

else:
	print('找不到檔案...')




#輸入商品跟價錢，二維清單
while True:
	name = input('請輸入商品名稱：')
	if name == 'q':
		break
	price = input('請輸入商品價格：')
	products.append(([name, price]))
print('印出清單裡所有的商品與價格：', products)#印出清單裡所有的商品與價格



#用for loop一行一行印出products
print('------------------')
print('一行一行印出清單的商品與價格：')
for p in products:
	print(p[0], '的價格是', p[1])



with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品' + ',' + '價格' + '\n') #檔案先加入Title，寫成f.write('商品,價格\n')也行
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')



