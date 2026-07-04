# Piro25_PythonGame_1
> 혼자하는 python 술게임

---

## 👥 팀원 & 역할 분담
| 이름 | 담당 게임 | 파일명 | 함수명 |
| :--- | :--- | :--- | :--- |
| **서영은** | 시장에 가면 | `games/game_sye.py` | `play_market_game(names, turn_idx)` |
| **임현아** | 폭탄 돌리기 | `games/game_lha.py` | `play_bomb_game(names, turn_idx)` |
| **이환희** | 김밥말이/훈민정음 | `games/game_lhh.py` | `play_gimbap_game(names, turn_idx)` |
| **정승현** | 기억력 게임 | `games/game_jsh.py` | `play_memory_game(names, turn_idx)` |
| **신은아** | 지하철 게임 | `games/game_sea.py` | `play_subway_game(names, turn_idx)` |

---

## 폴더 구조

```text
Piro25_PythonGame_1/
│
├── main.py              # 메인 게임 실행 파일 (전체 흐름 및 플레이어 상태 제어)
│
└── games/               # 개별 미니게임 소스코드 폴더
    ├── __init__.py      # 폴더를 패키지로 인식하게 하는 빈 파일
    ├── game_sye.py   # 시장에 가면 (서영은)
    ├── game_lha.py     # 폭탄 돌리기 (임현아)
    ├── game_lhh.py   # 김밥말이/훈민정음 (이환희)
    ├── game_jsh.py   # 기억력 게임 (정승현)
    └── game_sea.py   # 지하철 게임 (신은아)
```

---

## 🌿 Git Branch 전략

* **`main`** : 최종 완성본 브랜치 (**⚠️ 직접 커밋 절대 금지**)
* **`feature/성포함이니셜`** : 각자 기능을 작업하는 개인 브랜치
  * *예시:* `feature/sye` (서영은), `feature/lha` (임현아)
* **작업 흐름:** 개인 브랜치에서 작업 완료 ➔ GitHub에 Push ➔ **Pull Request(PR)** 생성 ➔ 팀원 리뷰 후 `main`으로 Merge

---

## 💬 Commit Message Convention

> **형식:** `타입: 내용`

* **`feat`**: 새로운 기능/섹션 구현
  * *예시:* `feat: 시장에 가면 게임 실제 로직 구현`
* **`fix`**: 코드 버그 및 예외 처리 오류 수정
  * *예시:* `fix: 지하철 게임 인덱스 바운드 에러 수정`
* **`style`**: 코드 포맷팅, 단순 줄바꿈, 텍스트 출력 문구 수정 (로직 변경 없음)
  * *예시:* `style: 게임 오버 아스키 아트 문구 수정`
* **`docs`**: 문서 수정 및 업데이트
  * *예시:* `docs: README 역할 분담 표 업데이트`

---

## 🛠️ 게임 함수 구현 가이드

### 📥 인자 (매개변수) 규칙
* `names` (list) : 참가자들의 이름이 담긴 문자열 리스트 (예: `['유저', '은서', '하연']`)
* `turn_idx` (int) : 현재 게임을 선택하여 시작한(선공) 사람의 index 번호

### 📤 리턴값 규칙
* `losers` (list) : 게임에서 패배하여 술을 마셔야 하는 사람들의 이름 리스트 (str 타입의 요소)
* **주의:** 패배자는 0명(공동 생존), 1명(독박), 혹은 여러 명(동시 탈락)일 수 있으므로 **반드시 리스트 형식**으로 반환해야 합니다. 아무도 안 걸렸을 때는 빈 리스트 `[]`를 반환합니다.
