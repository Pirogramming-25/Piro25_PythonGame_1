import random

def play_game_4(names, turn_idx):
    """
    names: 전체 플레이어 이름 리스트
    turn_idx: 이번에 게임을 고른 사람의 인덱스 (0번이 사용자, 나머지는 컴퓨터)
    return: 술 마실 대상자 이름 리스트
    """
    print(" ██████╗  █████╗ ███╗   ███╗███████╗    ███████╗████████╗ █████╗ ██████╗ ████████╗")
    print("██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝")
    print("██║  ███╗███████║██╔████╔██║█████╗      ███████╗   ██║   ███████║██████╔╝   ██║   ")
    print("██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ╚════██║   ██║   ██╔══██║██╔══██╗   ██║   ")
    print("╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ███████║   ██║   ██║  ██║██║  ██║   ██║   ")
    print(" ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝    ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ")
    print("\n👉 [배스킨라빈스 31] 게임 시작!")
    print("순서대로 1~3개씩 숫자를 순서대로 세어나가되 직전 사람이 부른 개수는 다시 부를 수 없습니다!")
    print("31을 부르는 사람이 벌칙입니다! 전략적으로 숫자를 골라보세요~\n")
    
    current_num = 0
    order = names[turn_idx:] + names[:turn_idx]
    idx = 0
    last_pick = None # 직전 사람이 부른 개수 기록
    
    while current_num < 31:
        player = order[idx % len(order)]
        is_computer = (player != names[0])
        
        remaining = 31 - current_num
        max_pick = min(3, remaining)
        
        #이번 턴에 고를 수 있는 개수 목록(직전에 부른 개수는 제외)
        available_picks = [n for n in range(1, max_pick+1) if n!= last_pick]
        
        #선택지가 하나도 없다면 제한 없이 진행
        if not available_picks:
            available_picks = list(range(1, max_pick + 1))
        if not is_computer: 
            while True:
                try:
                    pick = int(input(f"\n{player}님, 몇 개를 세시겠습니까? (1~{max_pick}): "))
                    if pick in available_picks:
                        break
                    elif pick == last_pick:
                        print(f"[오류] 직전에 {last_pick}개를 불렀으니 이번엔 다른 개수를 골라주세요! ")
                    else:
                        print(f"[오류] {available_picks} 중에서만 선택 가능합니다.")
                except ValueError:
                    print("[오류] 숫자만 입력해주세요.")
        #내가 아닐 경우(컴퓨터)
        else:
            pick = random.choice(available_picks)
            print(f"\n🤖{player}님이 {pick}개를 세기로 했습니다!")
        
        start_num = current_num +1
        current_num += pick
        counted_numbers = list(range(start_num, current_num+1))
        print(f"->{player}: {' '.join(map(str, counted_numbers))}")
        
        last_pick = pick #이번에 부른 개수를 기록해서 다음 사람에게 제한으로 넘김
        
        if current_num >= 31:
            print(f"\n💥 31을 부른 사람은 {player}입니다!\n")
            print(f"🤭{player}님, 오늘 좀 취하셔야겠네요! 벌주 한 잔!")
            return [player]
        
        idx += 1
    
    return []               
