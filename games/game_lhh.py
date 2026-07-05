import random


def play_game_3(names, turn_idx):  
    print("\n" + "=" * 50)
    print(" ██████╗  █████╗ ███╗   ███╗███████╗    ███████╗████████╗ █████╗ ██████╗ ████████╗")
    print("██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝")
    print("██║  ███╗███████║██╔████╔██║█████╗      ███████╗   ██║   ███████║██████╔╝   ██║   ")
    print("██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ╚════██║   ██║   ██╔══██║██╔══██╗   ██║   ")
    print("╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ███████║   ██║   ██║  ██║██║  ██║   ██║   ")
    print(" ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝    ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ")
    print("\n" + "=" * 50)
    print("👉 [김밥말이] 게임 시작! \n")
    print("규칙: 현재 턴인 사람에게 '김밥이 몇 줄?' 물어보면,")
    print("      n줄! 이라고 답하고, 그 다음 n명이 순서대로 '김밥말아!'를 외칩니다.")
    print("      당신은 그중 내 차례가 언제인지 스스로 판단해서 반응해야 합니다!")
    print()
    order_display = " -> ".join(n if n != names[0] else f"{n}(나)" for n in names)
    print(f"[게임 순서] {order_display} -> (다시 처음으로 순환)\n")
    print("=" * 50 + "\n")

    total = len(names)
    max_n = total - 1  # n의 최댓값: 전체 인원 수 - 1

    while True:
        current_player = names[turn_idx]

        if turn_idx == 0:  # 내 턴이라면
            while True:
                play_n = int(input(f"김밥이 몇 줄? (숫자만 입력해주세요.): ").strip())
                if 1 <= play_n <= max_n:  # 숫자인지와 범위 체크
                    break
                print(f"1~{max_n} 사이의 숫자를 입력하세요. (숫자만 입력해주세요.)")
            print(f"\n 🙋 {current_player}: \"{play_n}줄!\"\n")
        else:
            play_n = random.randint(1, max_n)
            print("김밥이 몇 줄?")
            print(f"🙋 {current_player}: \"{play_n}줄!\"\n")


        performers = []  # 외칠 사람들
        idx = turn_idx
        for _ in range(play_n):
            idx = (idx + 1) % total
            performers.append(names[idx])  

        print(f"[다음 {play_n}명이 '김밥말아!'를 외칩니다]\n")

        mistake_chance = 0.1 + 0.05 * (play_n - 1) 

        losers = []  

        answer = input(f" {names[0]} 님의 반응은? (김밥말아 / 침묵): ").strip()

        for p in performers:
            if p == names[0]:  # 내 차례라면 -> 아까 받은 answer로 채점
                if answer == "김밥말아 \n":
                    print(f"   -> ✅ 정답! 잘 외쳤습니다.\n")
                else:
                    print(f"   -> 😵 실수! 당신 차례였는데 못 외쳤습니다.\n")
                    losers.append(names[0])
            else:  # 내 차례가 아니라면 -> 그 사람이 실제로 외치는 걸 보여줌
                if random.random() < mistake_chance: 
                    print(f"   - {p}: (😵 헷갈려서 침묵... 실수!)\n")
                    losers.append(p)
                else:
                    print(f"   - {p}: \"김밥말아!\"")

        # 내 차례가 이번 라운드 performers에 없었는데 '김밥말아'라고 답한 경우
        if names[0] not in performers and answer == "김밥말아":
            print(f"   -> 😵 실수! 침묵해야 했는데 '김밥말아'라고 외쳐버렸습니다!\n")
            losers.append(names[0])

        next_turn_idx = (turn_idx + play_n + 1) % total

        print()
        if losers:
            print(f"😵 실수한 사람: {', '.join(losers)}")
            print("\n[게임 종료] 실수한 사람이 나와서 여기서 마칩니다!")
            return losers

        print("😌 아무도 실수하지 않고 무사히 넘어갔습니다!")
        print(f"➡️ 다음 턴: {names[next_turn_idx]}\n")
        turn_idx = next_turn_idx