from prefect import flow, task
import time
from datetime import datetime

@task
def print_hello():
    current_time = datetime.now().strftime("%H:%M:%S")
    print(f"Hello from Prefect! 当前时间: {current_time}")
    return "Hello 任务完成"

@task
def wait_a_bit(seconds):
    print(f"等待 {seconds} 秒...")
    time.sleep(seconds)
    return f"等待了 {seconds} 秒"

@flow(name="示例流程")
def example_flow(wait_seconds=5):
    """这是一个简单的示例流程，用于演示如何部署到工作池"""
    message = print_hello()
    result = wait_a_bit(wait_seconds)
    print(f"流程完成! 结果: {message} 和 {result}")
    return {"message": message, "result": result}

if __name__ == "__main__":
    example_flow() 