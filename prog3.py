from prog2Pydantic import Item

item={"id":1,"name":"Laptop","email":"Laptop@gmail.com","description":"A student Laptop","price":999.99}
item_obj=Item(**item)
print(item_obj)
print(item)