# [] - 리스트, {} - Set, {} -dict(ionary)
# dict : key - value
lecture = {
     "java" : 1,
     "python" : 2,
     "c" : 3,
     "javascript" : 4,
}
print(lecture["java"])

coffeeShopMenu = {
    "starbucks" : [{"name" : "아메리카노"},{"name" : "라떼"}],
    "megacoffee" : [{"name" : "아메리카노", "price":2000}, {"name" : "메가라떼","price":3000}]
}

print(coffeeShopMenu["megacoffee"])