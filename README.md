1 ЗАДАНИЕ (ДОБАВЛЕНИЕ ОБЪЕКТОВ И ПОЛУЧЕНИЕ ВСЕХ ЗАПИСЕЙ МОДЕЛИ)

СОЗДАНИЕ ОБЪЕКТОВ

Product.objects.create(name='Танцующий кактус', price=1200.00, stock=10)                    
<Product: Танцующий кактус>
Product.objects.create(name='Книга "Кизару. Дежавю."', price=1100.00, stock=6)   
<Product: Книга "Кизару. Дежавю.">
Product.objects.create(name='Футболка Patagonia', price=1800.00, stock=20)                             
<Product: Футболка Patagonia>
Product.objects.create(name='Кепка MLB', price=4000.00, stock=10)           
<Product: Кепка MLB>
Product.objects.create(name='Смартфон POCO X3 PRO ULTRA SUPER MAXIMUM', price=16000.00, stock=1) 
<Product: Смартфон POCO X3 PRO ULTRA SUPER MAXIMUM>
Product.objects.create(name='Маска Дима Билан', price=400.00, stock=10)    
<Product: Маска Дима Билан>
Product.objects.create(name='Джойстик для PS5', price=7000.50, stock=1)    
<Product: Джойстик для PS5>
Product.objects.create(name='Коробок спичек', price=21.50, stock=100)      
<Product: Коробок спичек>
Product.objects.create(name='Носки NEKI', price=70.50, stock=20)          
<Product: Носки NEKI>
Product.objects.create(name='Сумка La Routine', price=5000.00, stock=2)     
<Product: Сумка La Routine>

ВЫВОД ВСЕХ ПРОДУКТОВ

all_products = Product.objects.all()                                       

for product in all_products:

  print(product)

Танцующий кактус

Книга "Кизару. Дежавю."

Футболка Patagonia

Кепка MLB

Смартфон POCO X3 PRO ULTRA SUPER MAXIMUM

Маска Дима Билан

Джойстик для PS5

Коробок спичек

Носки NEKI

Сумка La Routine

2 ЗАДАНИЕ (запросы с filter(),exclude(),order_by()

filter()
![image](https://github.com/user-attachments/assets/d1d7ef17-7d92-4845-b02f-baa5af126df5)
![image](https://github.com/user-attachments/assets/feecdc14-68a8-45f5-ba84-883897f9bff9)
![image](https://github.com/user-attachments/assets/5049a2ef-ebef-400c-a7a6-9458d666878c)

exclude()
![image](https://github.com/user-attachments/assets/5677985a-80d0-4303-bf91-e3ca667995c8)
![image](https://github.com/user-attachments/assets/d6b7f460-c39b-4875-8050-fab6544ef600)
![image](https://github.com/user-attachments/assets/c9685f02-8b86-4b62-9069-61a9601a633a)

order_by()
![image](https://github.com/user-attachments/assets/f24e6d1b-a4e0-4ad3-91d7-9b1029f080c5)
![image](https://github.com/user-attachments/assets/efa301c3-1de5-44ed-946b-38bf04919452)
![image](https://github.com/user-attachments/assets/cbaff8e8-4467-43d4-bb50-7048ec911e14)

3 ЗАДАНИЕ СОЗДАНИЕ НЕСКОЛЬКИХ МОДЕЛЕЙ, values() И values_list()
![image](https://github.com/user-attachments/assets/a9f0cd71-2372-4214-ac1a-f5179eb04c01)

![image](https://github.com/user-attachments/assets/113ae6fc-e931-47fe-ad01-82cc05bb101e)

![image](https://github.com/user-attachments/assets/38c4ba3c-ae30-477d-8ff9-30dc8688a9ef)

values()

![image](https://github.com/user-attachments/assets/ed147c47-5201-45e7-bd0c-dd27d7610d2f)

![image](https://github.com/user-attachments/assets/ba9bbcbc-3bf9-4b04-8026-19966d1bd588)

![image](https://github.com/user-attachments/assets/17ed78b8-c4d5-4447-b91f-72088225635f)

value_list()

![image](https://github.com/user-attachments/assets/14f9f8cd-e696-4f09-a0f3-6db61ea1f606)


![image](https://github.com/user-attachments/assets/8e6b1631-87e2-4b79-878b-0c60150f3b4c)

![image](https://github.com/user-attachments/assets/b5d220d0-657b-463c-b21f-3d3b45b2ddfd)

4 ЗАДАНИЕ ЗАПРОСЫ С Q ОБЪЕКТАМИ

![image](https://github.com/user-attachments/assets/01ebd92e-75c5-4ca1-bd3f-e665a864618c)

![image](https://github.com/user-attachments/assets/f9fb8c2c-cc10-47c6-8ca7-cfc8df87a8c0)

![image](https://github.com/user-attachments/assets/8ff16f00-e628-464b-8ec0-50c6f0312b81)

![image](https://github.com/user-attachments/assets/5c8b808f-b88b-4385-9d9d-93faaa6386fb)

![image](https://github.com/user-attachments/assets/d3fbaebd-c16f-4ea1-bf26-bfd6b2ce2eeb)

![image](https://github.com/user-attachments/assets/c4f7df2a-e328-42ba-82ea-11b3afb4b2dc)

![image](https://github.com/user-attachments/assets/b36c09e0-82cc-4111-a87d-b79e6eb2e25e)

![image](https://github.com/user-attachments/assets/0726ba2a-9fb3-446e-8464-4cefa578f51e)

![image](https://github.com/user-attachments/assets/63d95df9-e0c2-40b1-9ef7-2a52f7322eb3)

5 ЗАДАНИЕ 

aggregate()

![image](https://github.com/user-attachments/assets/b15fa1f5-d93a-4d9d-a0fd-8f1e4967fa41)

![image](https://github.com/user-attachments/assets/c6e33c5c-ec9f-4420-8bf9-3b2b6ee3e312)

![image](https://github.com/user-attachments/assets/28d7dd3b-4112-4d49-b4e1-0f96b5abb0b2)

annotate()

![image](https://github.com/user-attachments/assets/887f6d54-884e-442d-ba3c-c4ec3f785277)

![image](https://github.com/user-attachments/assets/66a60de2-cbfc-4da4-aaad-699458ca7258)

![image](https://github.com/user-attachments/assets/484174a6-ab16-4269-bd2c-648cb8167208)
