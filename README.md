# SpireAgent: RL-based + AI Slay the Spire

## 🛠 Prerequisites

1. **Java 8+ Installed**: `java -version` 확인 필요.
2. **Slay the Spire (Steam Ver)**

## 📦 Required Mods (Steam Workshop)

게임 실행 전, Steam 창작마당에서 다음 모드들을 반드시 구독(설치)해야 합니다.

1. **ModTheSpire**: 모드 로더 (게임을 이걸로 실행해야 함)
2. **BaseMod**: 기본 라이브러리
3. **CommunicationMod**: 외부 프로세스와 통신을 담당하는 핵심 모드

## ⚙️ Configuration (CommunicationMod Setup)

AI와 게임을 연결하기 위해 `CommunicationMod` 설정이 필요합니다.

1. `SlayTheSpire` 설치 폴더로 이동.
2. `mts-launcher.jar` (또는 ModTheSpire) 실행.
3. 모드 목록에서 `CommunicationMod` 체크.
4. **(중요)** `CommunicationMod`의 설정(Config)을 열거나, 게임 폴더 내 생성된 `communication_mod_config.properties` 파일을 엽니다.
5. `command` 항목을 우리의 Python 에이전트로 지정해야 합니다.
   - 예: `command=C:\Users\User\anaconda3\envs\spire_agent\python.exe C:\Projects\SpireAgent\agent.py`
   - **주의:** Conda 환경의 python 경로를 절대 경로로 적어주는 것이 확실합니다.

## 🚀 How to Run
게임을 실행하면(ModTheSpire 이용), 게임이 자동으로 위 `command`에 설정된 Python 스크립트를 자식 프로세스로 실행합니다.


## (optional) wsl 개발 환경에서 window-java와 통신하기
1. run_wsl.bat 파일 작성
2. 