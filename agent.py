import os
import yaml
import logging
from connect.bridge import Bridge

# 로깅 설정
logging.basicConfig(filename='logs/agent.log', level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def load_config():
    with open('config/config.yaml', 'r') as f:
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