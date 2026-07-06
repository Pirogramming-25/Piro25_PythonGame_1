
import random
import time
from games.game_sye import play_game_1
from games.game_lha import play_game_2
from games.game_lhh import play_game_3
from games.game_jsh import play_game_4
from games.game_sea import play_game_5

# ==============================================================================
# [개별 플레이어 클래스] 
# ==============================================================================
class Player:
    def __init__(self, name, drink_limit):
        self.name = name                 # 플레이어 이름 (str)
        self.drink_limit = drink_limit   # 주량 수 (int)
        self.current_drinks = 0          # 현재 마신 잔 수 (int)

    def drink(self):
        """술을 한 잔 마십니다."""
        self.current_drinks += 1

    def is_dead(self):
        """치사량에 도달했는지 확인합니다."""
        return self.current_drinks >= self.drink_limit

    def get_remaining_drinks(self):
        """치사량까지 남은 잔 수를 반환합니다."""
        return self.drink_limit - self.current_drinks



# ==============================================================================
# [메인 게임 클래스]
# ==============================================================================
class AlcoholGame:
    def __init__(self):
        self.players = []       # Player 객체 리스트 [user, 컴1, 컴2, 컴3]
        self.user_name = ""
        
        # 게임 리스트
        self.mini_games = {
            1: ('시장에 가면 (서영은)', play_game_1),
            2: ('폭탄 돌리기 (임현아)', play_game_2),
            3: ('김밥말이 (이환희)', play_game_3),
            4: ('배스킨라빈스 31 (정승현)', play_game_4),
            5: ('지하철 게임 (신은아)', play_game_5)
        }

    # 1. 게임 시작(인트로)
    def print_intro(self):
        intro_art = r"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    _     _      ____    ___   _   _   ___   _         ____     _     _      _  _____   
   / \   | |    / ___|  / _ \ | | | | / _ \ | |       / ___|   / \   | \   / | | ____|  
  / _ \  | |   | |     | | | || |_| || | | || |      | |  _   / _ \  |  \_/  | |  _|    
 / ___ \ | |___| |___  | |_| ||  _  || |_| || |___   | |_| | / ___ \ | |\_/| | | |___   
/_/   \_\|_____|\____|  \___/ |_| |_| \___/ |_____|   \____|/_/   \_\|_|   |_| ||_____|  
                                                                                                 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  ヽ(≥o≤)ノ ヽ(≥o≤)ノ       안주 먹을🍗 시간은⏰ 없어요❌ 마시면서🍻 배우는 술게임🎮       ヽ(≥o≤)ノ ヽ(≥o≤)ノ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        """
        print(intro_art)
        
        choice = input("👉 게임을 진행할까요? (y/n) : ").strip().lower()
        if choice != 'y':
            print("게임을 종료합니다. 다음에 만나요! 👋")
            exit()

    def setup_user(self):
        # 2. 사용자의 이름 받기
        user_name = input("\n오늘 거하게 취해볼 당신의 이름은?: ").strip()

        # 3. 본인의 주량 선택하기
        print("\n================ 소주 기준 당신의 주량은? ================")
        print("1. 소주 반병(2잔)\n2. 소주 반병에서 한병 (4잔)\n3. 소주 한병에서 한병반 (6잔)")
        print("4. 소주 한병 반에서 두병(8잔)\n5. 소주 두병 이상 (10잔)")
        print("==========================================================")

        while True:
            try:
                capacity_choice = int(input("💡 당신의 치사량(주량)은 얼마만큼인가요?(1~5을 선택해주세요): "))
                if capacity_choice in [1, 2, 3, 4, 5]:
                    user_capacity = capacity_choice * 2
                    break
                else:
                    print("[오류] 1부터 5 사이의 숫자만 입력해주세요.")
            except ValueError:
                print("[오류] 올바른 숫자를 입력해주세요.")
        
        user_player = Player(name=user_name, drink_limit=user_capacity)
        self.players.append(user_player)
        self.user_name = user_name

    # 4. 같이 대결할 사람 초대하기
    def invite_friends(self):
        print("\n💬 함께 취할 친구들은 얼마나 필요하신가요?(최대 3명)")
        
        while True:
            try:
                invite_count = int(input("초대할 인원 수 (1~3명): "))
                if invite_count in [1,2,3]:
                    break
                else:
                    print("[오류] 1명에서 3명까지만 초대 가능합니다.")
            except ValueError:
                print("[오류] 올바른 숫자를 입력해주세요.")
        
        candidate_names = ["은아", "영은", "승현", "현아", "환희"]
        if self.user_name in candidate_names: # 유저 이름 중복 제거
            candidate_names.remove(self.user_name)
            
        chosen_names = random.sample(candidate_names, invite_count)
        
        print("\n✨ [초대 완료] 오늘 함께 취할 멤버입니다!")
        for name in chosen_names:
            random_limit = random.choice([2, 4, 6, 8, 10]) # 주량이 2의 배수말고 다른 숫자도 되면 수정 필요
            friend = Player(name=name, drink_limit=random_limit)
            self.players.append(friend)
            print(f"👤 {name} (치사량: {random_limit}잔)")
            time.sleep(0.4)

        self.print_status()

    # 현재 상태 출력 기능
    def print_status(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        for p in self.players:
            print(f"{p.name}은(는) 지금까지 {p.current_drinks}잔 ! 치사량까지 {p.get_remaining_drinks()}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    # 4. 게임 리스트 출력
    def print_game_list(self):
        print("\n ~~~~~~~~~~~~~ 오늘의 Alcohol GAME 리스트 ~~~~~~~~~~~~~~  ")
        for key, game_info in self.mini_games.items():
            print(f"{key}. {game_info[0]}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


    def game_loop(self):
        turn_idx = 0  # 0은 플레이어(유저), 그 외는 컴퓨터 친구들의 턴
        
        while True:
            self.print_game_list()
            
            current_turn_player = self.players[turn_idx]
            
            # 게임 시작 전 진행 의사 체크 
            time.sleep(1.0)
            print(f"\n술게임 진행중! 현재는 {current_turn_player.name}의 게임 선택 턴입니다.") 
            exit_choice = input("그만하고 싶으면 'exit'를, 계속하고 싶으면 아무 키나 입력해 주세요!: ").strip().lower() 
            if exit_choice == 'exit':
                print("게임을 종료합니다.")
                break
                
            selected_game_num = None
            # 플레이어 턴일 때 직접 선택
            if turn_idx == 0:
                while True:
                    try:
                        selected_game_num = int(input(f"\n{current_turn_player.name}(이)가 좋아하는 랜덤 게임~ 무슨 게임? (1~5): ")) 
                        if selected_game_num in self.mini_games:
                            break
                        else:
                            print("[오류] 1부터 5 사이의 숫자를 선택해 주세요.")
                    except ValueError:
                        print("[오류] 숫자만 입력 가능합니다.")
            # 컴퓨터 턴일 때 랜덤 선택
            else:
                selected_game_num = random.randint(1, 5) 
                print(f"\n🤖 {current_turn_player.name}(이)가 좋아하는 랜덤 게임~ 랜덤 게임~ 무슨 게임?: {selected_game_num}") 
            
            game_name, game_func = self.mini_games[selected_game_num]
            print(f"\n📢 [{current_turn_player.name}] 님이 [{game_name}]을 선택하셨습니다!") 
            
            
            player_names = [p.name for p in self.players]            
            # 미니게임 실행 및 loser 받아오기
            loser_names = game_func(player_names, turn_idx)
            
            # 벌주 마시기
            if loser_names:
                print("\n아~ 누가누가 술을 마셔! 🍷")
                for name in loser_names:
                    for p in self.players:
                        if p.name == name:
                            p.drink()
                            print(f" └ [{p.name}]이(가) 술을 마셔! 원~~~샷! 🍷 (현재: {p.current_drinks}/{p.drink_limit}잔)")
            else:
                print("\n휴~ 아무도 술을 마시지 않고 무사히 넘어갔습니다! 😌")    
            
            # 현재 결과 출력
            self.print_status()
            
            # 7. 누군가 치사량에 도달한다면 -> 게임 종료 
            dead_players = [p for p in self.players if p.is_dead()]
            if dead_players:
                print("\n" + "="*80)
                print("   ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ ")
                print("  ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗")
                print("  ██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝")
                print("  ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗")
                print("  ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║")
                print("   ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝")
                print("="*80)
                for dp in dead_players:
                    print(f"💀 [{dp.name}]이(가) 치사량에 도달하여 전사했습니다... 꿈나라에서는 편히 쉬시길..zzz")
                print("👋 다음에 술 마시면 또 불러주세요~ 안녕! (^^) 수고하셨습니다 (^~^)")
                break
            
            # 다음 턴으로 토스
            turn_idx = (turn_idx + 1) % len(self.players)


    def start(self):
        """ 전체 게임 루프 """
        self.print_intro()
        self.setup_user()
        self.invite_friends()
        self.game_loop()




# ==============================================================================
# 프로그램 시작점
# ==============================================================================
if __name__ == "__main__":
    game_manager = AlcoholGame()
    game_manager.start()