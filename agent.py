import os
import sys
import yaml
import logging
from connect.bridge import Bridge

# 로깅 설정
# 1. 현재 스크립트(agent.py)의 절대 경로를 찾음
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 2. logs 폴더와 config 폴더의 절대 경로 생성
LOG_DIR = os.path.join(BASE_DIR, 'logs')
CONFIG_PATH = os.path.join(BASE_DIR, 'config', 'config.yaml')

# 3. logs 폴더가 없으면 생성 (안전장치)
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# 4. 로깅 설정 (절대 경로 사용)
logging.basicConfig(
    filename=os.path.join(LOG_DIR, 'agent.log'), 
    level=logging.DEBUG, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def load_config():
    with open(CONFIG_PATH, 'r') as f:
        return yaml.safe_load(f)

def main():
    # 1. 설정 로드
    config = load_config()
    logging.info(f"Agent {config['agent']['name']} Starting...")

    # 2. 통신 브릿지 연결
    bridge = Bridge()
    bridge.send_ready() # 게임에게 "나 준비됐어!" 외침

    # 3. 메인 루프
    while True:
        state = bridge.receive_state()
        
        if state:
            logging.info(f"Received State: Turn {state.get('turn')}")
            
            # (임시) 게임이 진행되도록 턴만 넘겨봄
            # 실제로는 여기서 AI가 판단을 내려야 함
            if state.get('in_combat'):
                bridge.send_command("action: end_turn")
            else:
                # 전투 중이 아니면(지도 등) 일단 대기 or 랜덤 선택 (추후 구현)
                pass

if __name__ == "__main__":
    main()