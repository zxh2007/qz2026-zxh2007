# Article Management System

## 项目简介

一个基于 Django 的文章管理系统数据层实现。

项目包含文章管理、附件管理、审计日志记录以及浏览量统计等功能。

## 功能列表

### Article

- 标题
- 正文
- 作者
- 状态管理
- 浏览量统计
- 创建时间
- 更新时间

### Attachment

- 文件上传
- 关联文章
- 上传时间记录

### AuditLog

- 创建日志
- 更新日志
- 删除日志
- JSON 格式变更信息记录

### 浏览量统计

使用 Django F 表达式：

```python
Article.objects.filter(id=article_id).update(
    views=F("views") + 1
)
```

避免高并发场景下出现丢失更新问题。

## 技术栈

- Python
- Django
- SQLite

## 安装依赖

```bash
pip install -r requirements.txt
```

## 数据库迁移

```bash
python manage.py makemigrations
python manage.py migrate
```

## 创建管理员

```bash
python manage.py createsuperuser
```

## 启动项目

```bash
python manage.py runserver
```

## 后台地址

```text
http://127.0.0.1:8000/admin
```