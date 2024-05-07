# (기본타입) a= 1, b = 3.14, c= True, d= "hello"
# e = [] , f = {} set or dict



# k[str or int] - v [any]
person = {
    'name' : "엄준식",
    'age' : 22,
    'town' : "동탄시",
    'coffeeList' : ["아메리카노", "라떼", "민트"],
    'academy' : {
        "first" : "java",
        "second" : "c-langauge",
        "third" : "c-langauge",
    },

}

print(f"이름 : {person["name"]} 동네:{person["town"]} 좋아하는 커피 3번째:{person["coffeeList"][2]}"
      f" 학원 세번째 수업:{person["academy"]["third"]}")