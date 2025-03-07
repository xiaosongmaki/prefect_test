from prefect import flow
from example_flow import example_flow

if __name__ == "__main__":
    # 使用 serve 方法创建部署并立即开始监听
    example_flow.serve(
        name="简单流程部署",
        #work_pool_name="my_mac",  # 指定工作池名称
        cron="*/1 * * * *"  # 每5分钟运行一次
    ) 