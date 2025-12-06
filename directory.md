SpireAgent/
├── config/                 # 설정 파일 관리
│   └── config.yaml         # (요청) 게임 경로, 모드 설정, 에이전트 파라미터
├── connect/                # (요청) 게임 통신 모듈
│   ├── __init__.py
│   └── bridge.py           # CommunicationMod와 표준 입출력(Stdin/out) 통신 담당
├── environment/            # (요청) 가상 환경 설정
│   └── environment.yaml    # Conda 환경 설정 파일
├── docs/                   # 문서화
│   └── manuals/            # 추후 매뉴얼 등
├── logs/                   # 게임 로그 저장 (디버깅용)
├── agent.py                # 메인 실행 진입점 (Entry Point)
└── README.md               # (요청) 필수 모드 및 설치 가이드