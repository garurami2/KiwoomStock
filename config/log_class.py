import logging
import traceback
import datetime
import os

class Logging():
    def __init__(self):
        self.logger = logging.getLogger(__name__)

        # 핸들러가 없을 때만 추가
        if not self.logger.handlers:
            formatter = logging.Formatter("%(asctime)s | %(filename)s | lines: %(lineno)d | %(levelname)s -> %(message)s")

            streamHandler = logging.StreamHandler()
            streamHandler.setFormatter(formatter)
            self.logger.addHandler(streamHandler)

            # log 디렉토리 없으면 생성
            if not os.path.exists('log'):
                os.makedirs('log')

            d_time = datetime.datetime.now()
            d_str = d_time.strftime("%Y-%m-%d")
            fileHandler = logging.FileHandler(f"log/{d_str}.log", encoding="utf-8")
            fileHandler.setFormatter(formatter)
            self.logger.addHandler(fileHandler)

            self.logger.setLevel(logging.DEBUG)

    def _handle_request_error(self, func_name: str, e: Exception) -> None:
        self.logger.error(f"{func_name} 오류: {e}", exc_info=True)
        traceback.print_exc()