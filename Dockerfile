FROM python:3.9-slim

WORKDIR /app

# 复制项目文件
COPY . /app/

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 设置环境变量
ENV PYTHONUNBUFFERED=1

# 暴露Prefect服务端口
EXPOSE 4200

# 默认命令
CMD ["python", "example_flow.py"] 