from utils.test import run_test
from utils.send2traq import send2traq
from utils.stop_instance import stop_instance
from config import TEST_NAME

if __name__ == '__main__':
    send2traq(f"計測開始: {TEST_NAME}")

    run_test()

    stop_instance()