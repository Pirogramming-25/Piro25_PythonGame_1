import time
import random


def play_game_5(names, turn_idx):   
    
    print("\n" + "="*50)
    print("👏 [369 게임] 시작! 3, 6, 9에는 박수를 치세요! 👏")
    print("="*50)
    
    # 현재 참여자 수
    num_players = len(names)
    
    # turn_idx부터 시작할 수 있도록 현재 인덱스 설정
    current_idx = turn_idx
    
    # 게임은 1부터 시작합니다.
    number = 1
    
    # 패배자를 담을 리스트
    losers = []
    
    # 컴퓨터의 정답 확률 (0.85 = 85% 확률로 올바르게 대답, 15% 확률로 실수)
    bot_accuracy = 0.85

    while True:
        current_player = names[current_idx]
        
        # 1. 현재 숫자에 3, 6, 9가 몇 개 들어있는지 계산
        count_369 = str(number).count('3') + str(number).count('6') + str(number).count('9')
        
        # 실제 정답 설정 (3,6,9가 있으면 개수만큼 👏, 없으면 숫자 문자열)
        if count_369 > 0:
            correct_answer = "👏" * count_369
        else:
            correct_answer = str(number)
            
        # 2. 플레이어 차례 (turn_idx가 0인 유저가 첫 플레이어라고 가정, 여기선 '유저' 단어가 포함되면 유저로 인식)
        # 실제 프로젝트 구조에 맞춰 유저 이름 체크 방식을 변경해도 좋아.
        if "유저" in current_player or current_idx == 0:
            print(f"\n[내 턴!] 현재 숫자: {number}")
            user_input = input(f"👉 {current_player}의 선택 (숫자 입력 또는 짝/👏 등 입력): ").strip()
            
            # 유저가 친 '짝'이나 '👏'을 동일하게 처리하기 위한 보정
            if "짝" in user_input:
                user_input = user_input.replace("짝", "👏")
                
            player_answer = user_input
        
        # 3. 컴퓨터(봇) 차례
        else:
            time.sleep(0.8) # 게임 생동감을 위한 약간의 딜레이
            
            # 확률에 따라 컴퓨터가 정답을 말하거나 오답을 말함
            if random.random() < bot_accuracy:
                player_answer = correct_answer
            else:
                # 오답 유도: 👏 칠 타이밍에 숫자를 말하거나, 숫자 타이밍에 👏를 침
                if count_369 > 0:
                    player_answer = str(number)
                else:
                    player_answer = "👏"
            
            print(f"🤖 {current_player}: {player_answer}")

        # 4. 정답 검증
        if player_answer != correct_answer:
            print(f"\n🚨 [틀렸습니다!] {current_player}(이)가 잘못된 대답을 했습니다!")
            print(f"💡 정답은 [{correct_answer}] 이었습니다!")
            losers.append(current_player)
            break # 게임 종료
            
        # 5. 다음 상태로 업데이트
        number += 1
        current_idx = (current_idx + 1) % num_players