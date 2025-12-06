import sys
import json
import logging

class Bridge:
    def __init__(self):
        self.ready = False

    def send_ready(self):
        """게임에 준비 신호를 보냄 (CommunicationMod 규약)"""
        print("ready", flush=True)
        self.ready = True

    def receive_state(self):
        """표준 입력(stdin)으로부터 게임 상태 JSON을 읽음"""
        try:
            line = sys.stdin.readline()
            if not line:
                return None
            
            # CommunicationMod가 가끔 빈 줄을 보낼 때 처리
            if not line.strip():
                return None

            state = json.loads(line)
            return state
        except json.JSONDecodeError:
            logging.error("Failed to decode JSON from game.")
            return None
        except Exception as e:
            logging.error(f"Connection error: {e}")
            return None

    def send_command(self, command):
        """게임으로 명령어 전송"""
        print(command, flush=True)