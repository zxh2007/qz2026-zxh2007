# ProgrammeHomework

程序部 2026 国庆考核作业。

## 仓库结构

```text
.
├── written.md      # 选择题与简答题
├── q1              # 编程题1：JSON日志管道
├── q2              # 编程题2：用户管理器
└── project-a       # 工程题A：文章管理系统
```

## 已完成内容

### written.md

完成全部选择题和简答题。

### q1

JSON 日志分析器。

实现功能：

- 读取 `.jsonl` 文件
- 统计日志总数
- 按 level 分类统计
- 按 user 分类统计
- 获取最后一条 ERROR 日志
- 文件不存在时返回空结果
- 跳过格式错误的 JSON 行

### q2

用户管理器。

实现功能：

- 添加用户
- 查询用户
- 修改年龄
- 删除用户
- 列出所有用户
- 保存到 JSON 文件
- 从 JSON 文件加载数据
- 自动维护用户 id

### project-a

基于 Django 的文章管理系统。

已实现：

- Article 模型
- Attachment 模型
- AuditLog 模型
- Django Admin 后台管理
- Django Signal 自动记录审计日志
- JSONField 存储审计信息
- F 表达式实现浏览量原子更新
- SQLite 数据库

## project-a 运行方式

进入项目目录：

```bash
cd project-a
```

安装依赖：

```bash
pip install -r requirements.txt
```

执行数据库迁移：

```bash
python manage.py migrate
```

创建管理员账号：

```bash
python manage.py createsuperuser
```

启动项目：

```bash
python manage.py runserver
```

访问后台：

```text
http://127.0.0.1:8000/admin
```

## 开发环境

- Python 3.10+
- Django 6.1.1
- SQLite3
