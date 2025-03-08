# Prefect 示例项目

这是一个使用Prefect工作流管理系统的示例项目。

## 项目结构

- `example_flow.py`: 包含示例Prefect流程
- `serve_example.py`: 用于部署和服务化流程
- `prefect.yaml`: Prefect配置文件

## 使用Docker镜像

### 构建镜像

```bash
docker build -t prefect_test .
```

### 运行镜像

```bash
# 运行示例流程
docker run --name prefect_container prefect_test

# 或者以交互模式运行
docker run -it --name prefect_container prefect_test /bin/bash
```

### 使用自定义命令

```bash
# 运行serve_example.py
docker run --name prefect_server prefect_test python serve_example.py
```

## 注意事项

- 确保已安装Docker
- 如需连接到Prefect Cloud或自托管的Prefect服务器，请设置相应的环境变量 