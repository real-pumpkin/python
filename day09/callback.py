def a(x):
    print("a함수 실행")
    x()
def b():
    print("b함수 실행")

a(b)

#게임 몬스터 프로그램
def killing_monster(monster, eventNumber):
    print(f"{monster}를 처지 했습니다.!")
    #골드, 음식, 경험치 or 팀원 획득 or ? or ?
    if eventNumber == 1:
        print("골드 획득")
    elif eventNumber == 2:
        print("음식 획득")
    elif eventNumber == 3:
        print("경험치 획득")

def killing_monster(monster, event):
    print(f"{monster}를 처지 했습니다.!")
    event()
def getGold():
    print("골드 획득!")

def getFood():
    print("음식 획득!")

killing_monster( monster."슬라임", getGold)
killing_monster( monster."늑대", getFood)