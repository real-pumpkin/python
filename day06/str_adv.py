language = "python is a great language."
#find
a = language.find("great")
print(a)

#replace
b = language.replace("python", "java")
print(b)

#upper, lower
c= language.upper()
print(c)

# great 기준으로 양옆으로 찢어줘
#split(찢다)
d = language.split("great")
print(d)

# join
e = " ". join(["hello","world!"])
print(e)
