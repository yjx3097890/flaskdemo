
### 环境设置

#### 依赖
* python 3.6+
* postgresql 11
* git

#### linux
* export FLASK_APP = flasky.py
* export SECRET_KEY （可选）

### 数据库迁移
* 初始化（已初始化migrations目录则跳过）：flask db init
* 创建迁移脚本：flask db migrate -m 'message'
* 迁移到指定或最新版本数据库：flask db upgrade <revision>
* 还原到指定或本数据库：flask db downgrade <revision>

### 运行

#### 开发环境运行
1. export FLASK_ENV = development
2. python3 -m venv venv
3. source venv/bin/active 
4. pip install -r requirements.txt
5. 新建数据库 flaskdemo
6. 数据库迁移
7. flask run

