# 함수 : input -> output
# 마술 상자 : [100 -> 500, 200 -> 1000, 300 -> x]
# f(x) => len(x), str(x), int(x), print(x). input(x)

# "python".count("p")
# count("p")

"python".upper()

"python". isupper

def koreaIt(x):
    return x + "코리아아이티"
a = koreaIt("인천점")
print(a)


def makeEmojiList(x,y):
    return [y for x in range(x)]

def changeEmoji(x):
    if x == '🥚' :
        return '🍔'
    elif x == '🍔':
        return '🍕'
    elif x == '🍕':
        return '🍳'
    else:
        return "에러"

print(changeEmoji('🍕'))