from datetime import datetime

def get_current_time():
    now = datetime.now()
    return now.strftime("%Y年%m月%d日 %H:%M:%S")

if __name__ == "__main__":
    print("程序运行时间：", get_current_time())