import time
import random

def play_game_2(names, turn_idx):   
    print("\n" + "=" * 50)
    print(" ██████╗  █████╗ ███╗   ███╗███████╗    ███████╗████████╗ █████╗ ██████╗ ████████╗")
    print("██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝")
    print("██║  ███╗███████║██╔████╔██║█████╗      ███████╗   ██║   ███████║██████╔╝   ██║   ")
    print("██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ╚════██║   ██║   ██╔══██║██╔══██╗   ██║   ")
    print("╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ███████║   ██║   ██║  ██║██║  ██║   ██║   ")
    print(" ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝    ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ")
    print("\n" + "=" * 50)
    print("\n👉 [폭탄 돌리기] 게임 시작!")
    losers = []
    
    # 선공 랜덤 설정
    turn_idx = random.randint(0, len(names) - 1)
    print(f"[{names[turn_idx]}]님 부터 폭탄 돌리기 시작합니다!")

    # 게임 로직 구현 (폭탄 돌리기)
    normal_question_list = [
        "가장 좋아하는 음식은?", 
        "가장 싫어하는 것은?(뭐든 상관없음)", 
        "오늘 먹은 것은?",
        "최근에 본 영화나 드라마는?", 
        "피자 토핑을 하나만 고른다면?(치즈제외)", 
        "고등학교 시절 가장 싫어했던 과목은?",
        "가장 좋아하는 색은?(여러 색 가능)", 
        "좋았던 여행지 or 가고 싶은 여행지는?", 
        "편의점 가면 꼭 사는 건?",
        "한 가지 음식을 평생 공짜로 먹을 수 있다면 어떤 거 선택?", 
        "좀비가 나타나면 가장 먼저 연락할 사람은?",
        "좀비를 발견했을 때 나의 행동은?", 
        "최애 캐릭터가 있다면?(이모티콘, 애니 등)", 
        "평생 한 계절만 살아야 한다면 어떤 계절?(간단한 이유도)",
        "평생 한 month만 살아야 한다면 몇 월달?", 
        "무인도에 물건 하나만 가져갈 수 있다면 어떤 물건?(사람제외)",
        "인생 영화or드라마or책이 있다면?(택1)", 
        "가장 최근에 소비한 것은?", 
        "요즘 가장 많이 듣는 노래 제목은?",
        "하루 동안 원하는 능력을 가질 수 있다면 어떤 능력?", 
        "가장 좋아하는 동물과 간단한 이유는?",
        "산vs바다? 이유는?", 
        "본인의 MBTI는? (나는 ****)", 
        "지금 가장 먹고 싶은 것은?",
        "가장 좋아하는 과자는?", 
        "최애 음료수는?(종류도 가능)", 
        "이상형 조건 중 하나는?(외면,내면 모두 가능)",
        "엽떡 어떤 맛 시켜먹어?(나는 **맛)", 
        "나랑 잘맞는 사람들의 특징은?(ex. 연락빈도, 성격 등)"
    ]

    special_question_list = [
        "타임 어택 시작! 3초 안에 아무 숫자 하나를 누르고 엔터를 치세요!!!",
        "폭탄 불량으로 인해 질문 없이 즉시 다음 사람에게 넘어갑니다! 행운의 폭탄!",
        "이상한 폭탄이 걸렸습니다! 시간이 2배로 빠르게 흐릅니다.. 지금 드는 생각은?(5글자 이상)"
    ]

    special_rules = [-1, -2, -3]

    bomb_timer = random.randint(60, 180)
    print("폭탄 타이머가 세팅되었습니다! 남은 시간은 비밀입니다.. 행운을 빕니다!\n")

    current_idx = turn_idx
    game_over = False
    shuffled_questions = normal_question_list.copy()

    while not game_over:
        player = names[current_idx]
        human = (current_idx == 0)

        print("-" * 50)
        print(f"[{player}]님 차례입니다! 폭탄 도착했습니다!!!")

        chance = random.randint(1, 10)
        start_time = time.time()
        elapsed_time = 0
        
        if chance == 1:
            special_idx = random.randint(0, len(special_question_list) - 1)
            rule = special_rules[special_idx]

            print(f"!!이벤트 발생!! {special_question_list[special_idx]}")

            if rule == -2:
                print("폭탄 불량으로 안전하게 넘어갔습니다..")
                elapsed_time = 0
                current_idx = (current_idx + 1) % len(names)
                continue
            
            elif rule == -1:
                if human:
                    input("[여기에 아무 숫자나 누르고 엔터]: ")
                    end_time = time.time()
                    elapsed_time = end_time - start_time
                else:
                    computer_num = random.randint(0, 9)
                    time.sleep(1.0)
                    print(f"[여기에 아무 숫자나 누르고 엔터]: {computer_num}")
                    elapsed_time = random.uniform(1.0, 4.0)  # 타임 어택 규칙에 맞게 1~4초로 밸런스 조정

                if elapsed_time > 3:
                    print(f"실패... 3초가 초과되었습니다.. ({int(elapsed_time)}초 소요..)")
                else:
                    print(f"성공!!! {elapsed_time:.2f}초만에 성공!")
            
            elif rule == -3:
                if human:
                    while True:
                        user_answer = input("답변 입력: ").strip()
                        if len(user_answer) >= 5:
                            break
                        print("답변이 너무 짧습니다! 5글자 이상이어야 합니다. 다시!!")   
                    end_time = time.time()
                    elapsed_time = (end_time - start_time) * 2
                else:
                    computer_answers = ["너무 떨려요!", "빨리 넘어가라!!", "폭탄 터지는 거 아니야?"]
                    print(f"답변 입력: {random.choice(computer_answers)}")
                    elapsed_time = random.uniform(2.0, 5.0) * 2  # 시간 계산 후 2배 적용
                    time.sleep(1)

                print(f"이상한 폭탄으로 인해 폭탄 시간이 {int(elapsed_time)}초 차감되었습니다")
        else:
            if not shuffled_questions:
                shuffled_questions = normal_question_list.copy()

            question = random.choice(shuffled_questions)
            shuffled_questions.remove(question)
            required_length = 5

            print(f"질문: {question}")
            print(f"{required_length}글자 이상 입력해야 통과!!")

            if human:  
                while True:
                    user_answer = input("답변: ").strip()
                    if len(user_answer) >= required_length:
                        print("통과!! 다음 사람에게 폭탄이 넘어갑니다..")
                        break
                    else:
                        print(f"답변이 너무 짧아요.. 글자 수를 지켜주세요\n다시 입력하세요!")
                end_time = time.time()
                elapsed_time = end_time - start_time
            else:             
                computer_answers = ["비밀이어서 말 못해..", "다 좋아해!!", "갑자기 생각이 잘 안나", "패스하겠습니다!!", "그닥 다 별로 안좋아해.."]
                time.sleep(1.0) 
                print(f"답변: {random.choice(computer_answers)}")
                print("통과!! 다음 사람에게 폭탄이 넘어갑니다..")
                elapsed_time = random.uniform(5.0, 9.0)

        print(f" 이번 차례에 {int(elapsed_time)}초를 소모했습니다.")
        bomb_timer -= elapsed_time

        if bomb_timer <= 0:
            print("\n" + "=" * 50)
            print("!!!!!!폭탄이 터졌습니다!!!!!!!!!!!!!!!!!!!!!!!!")
            print(f"[{player}]님 당첨!")
            print("=" * 50)
                
            losers.append(player)  
            game_over = True       
            break

        current_idx = (current_idx + 1) % len(names)

    return losers