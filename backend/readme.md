# Flask 后端

## Flask-Login

## Flask-SQLAlchemy

## Flask-Migrate

### 安装

```shell
pip install Flask-Migrate
```

### 配置

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
```

### 查看帮助

`注： flask 命令需要在 flask 应用根目录执行`

```shell
flask db --help
```

### 初始化迁移脚本 (仅执行一次)

```shell
flask db init
```

### 生成迁移脚本

```shell
flask db migrate -m "迁移描述"
```

### 应用迁移脚本

```shell
flask db upgrade
```
