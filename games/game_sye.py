import os
import random
import time
 
# 물건 목록들
MARKET_ITEMS = [
    "사과", "바나나", "딸기", "수박", "참외", "포도", "복숭아", "귤", "감", "배",
    "키위", "망고", "체리", "자두", "석류", "레몬", "오렌지", "메론", "무화과", "블루베리",
    "감자", "고구마", "양파", "당근", "오이", "상추", "배추", "마늘", "고추", "파",
    "시금치", "브로콜리", "애호박", "가지", "무", "콩나물", "숙주", "깻잎", "버섯", "옥수수",
    "고등어", "갈치", "오징어", "새우", "조개", "미역", "멸치", "김", "다시마", "굴",
    "소고기", "돼지고기", "닭고기", "삼겹살", "갈비", "베이컨", "소시지", "햄", "계란", "우유",
    "두부", "치즈", "김치", "라면", "국수", "만두", "떡", "어묵", "순대", "잡채",
    "참기름", "간장", "된장", "고추장", "소금", "설탕", "식초", "케첩", "마요네즈", "카레",
    "떡볶이", "닭강정", "붕어빵", "호떡", "김밥", "핫도그", "튀김", "젤리", "초콜릿", "사탕",
    "과자", "빵", "케이크", "아이스크림", "팝콘", "쿠키", "도넛", "카스텔라", "약과", "한과",
    "휴지", "세제", "치약", "칫솔", "비누", "샴푸", "수세미", "고무장갑", "종이컵", "물티슈",
]
 
 
# 화면 지우기 (이전 내용 지워야 컨닝 못 함)
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# 내 차례
def user_turn(player_name, sequence):
    print(f"[{player_name}]님의 차례입니다.")
    print(f"지금까지 나온 물건은 총 {len(sequence)}개! 순서대로 기억해서 입력하세요.")
    print("마지막에 새 물건 하나를 추가하세요. ⚠️  단어는 띄어쓰기로 구분!")
    print("모르면 '포기'를 입력하세요!")
 
    answer = input("입력: ").strip()
 
    if answer == "포기":
        print("\n❌ 포기했습니다! 🍺 원샷 각오하세요...")
        return False, None
 
    words = answer.split()
    new_item = words[-1] if words else ""
 
    #수량에 맞지 않게 입력했을 때
    if len(words) != len(sequence) + 1:
        print(f"\n❌ 틀렸습니다! 총 {len(sequence) + 1}개의 물건을 입력해야 합니다. 🍺")
        return False, None
 
    #순서 틀렸을 때
    if words[:-1] != sequence:
        print("\n❌ 틀렸습니다! 앞에 나온 물건의 순서가 틀렸습니다. 🍺")
        return False, None
 
    #물건 목록에 없을 때
    if new_item not in MARKET_ITEMS:
        print("\n❌ 틀렸습니다! 시장 물건 목록에 없는 단어입니다. 🍺")
        return False, None
 
    #이미 나온 물건 말했을 때
    if new_item in sequence:
        print("\n❌ 틀렸습니다! 이미 나온 물건을 다시 말했습니다. 🍺")
        return False, None
 
    return True, new_item
 
 
# 컴퓨터 차례
def computer_turn(player_name, sequence):
    print(f"[{player_name}]님의 차례입니다.")
    print(f"{player_name}님이 기억을 더듬는 중...")
    time.sleep(1)
 
    # 라운드가 진행될수록 실수 확률이 조금씩 올라감
    mistake_chance = min(0.10 + len(sequence) * 0.05, 0.55)
    candidates = [item for item in MARKET_ITEMS if item not in sequence]
 
    if random.random() < mistake_chance or not candidates:
        print(f"😵 {player_name}님이 순서를 까먹었습니다!")
        time.sleep(1.5)
        return False, None
 
    new_item = random.choice(candidates)
    print(f"{player_name}: 시장에 가면 " + ", ".join(sequence + [new_item]) + "도 있고!")
    print("(👀 잘 기억해두세요! 곧 화면이 지워집니다...)")
    time.sleep(3.5)
    return True, new_item
 
 
def play_game_1(names, turn_idx):
    print("\n" + "=" * 50)
    print(" ██████╗  █████╗ ███╗   ███╗███████╗    ███████╗████████╗ █████╗ ██████╗ ████████╗")
    print("██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝")
    print("██║  ███╗███████║██╔████╔██║█████╗      ███████╗   ██║   ███████║██████╔╝   ██║   ")
    print("██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ╚════██║   ██║   ██╔══██║██╔══██╗   ██║   ")
    print("╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ███████║   ██║   ██║  ██║██║  ██║   ██║   ")
    print(" ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝    ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ")
    print("\n" + "=" * 50)
    print("👉 [시장에 가면] 게임 시작!")
    print("앞사람이 말한 물건을 전부 기억하고, 새 물건 하나를 붙이는 게임입니다.")
    print("틀리거나 포기하면 벌칙으로 술을 마십니다!")
    print("~" * 60)
    input("준비되면 Enter를 눌러 시작하세요...")
 
    sequence = []
    idx = turn_idx
    round_num = 1
 
    while True:
        clear_screen()
        name = names[idx]
        print(f"[라운드 {round_num}] 지금까지 이어진 물건 수: {len(sequence)}개")
        print("~" * 60)
 
        # names[0]이면 나, 아니면 컴퓨터 -> 알맞은 함수 골라서 실행
        turn_func = user_turn if idx == 0 else computer_turn
        success, new_item = turn_func(name, sequence)
 
        if not success:
            print(f"\n💀 {name}님이 벌칙 대상입니다! 🍺")
            input("메인 게임으로 돌아가려면 Enter를 눌러주세요...")
            return [name]
 
        sequence.append(new_item)
        round_num += 1
 
        idx = (idx + 1) % len(names)