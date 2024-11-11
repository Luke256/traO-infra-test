from utils.test import run_test
from utils.send2traq import send2traq

if __name__ == '__main__':
    print("Webhook test")
    send2traq("Ping")

    run_test()