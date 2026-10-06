import json
import os


class UserManager:
    def __init__(self):
        self.users = []
        self.next_id = 1

    def add_user(self, name, age):  # 添加用户
        user = {
            "id": self.next_id,
            "name": name,
            "age": age
        }
        self.users.append(user)
        self.next_id += 1
        return user

    def get_user(self, user_id):  # 根据id查找用户
        for user in self.users:
            if user["id"] == user_id:
                return user
        return None

    def update_age(self, user_id, new_age):  # 修改年龄
        for user in self.users:
            if user["id"] == user_id:
                user["age"] = new_age
                return True
        return False

    def remove_user(self, user_id):  # 删除用户
        for user in self.users:
            if user["id"] == user_id:
                self.users.remove(user)
                return True
        return False

    def list_users(self):  # 返回所有用户
        return self.users

    def save_to_json(self, filename):  # 保存到JSON文件
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.users, f, ensure_ascii=False)

    def load_from_json(self, filename):  # 从JSON文件读取
        if not os.path.exists(filename):
            return
        with open(filename, "r", encoding="utf-8") as f:
            self.users = json.load(f)
        max_id = 0
        for user in self.users:
            if user["id"] > max_id:
                max_id = user["id"]
        self.next_id = max_id + 1


if __name__ == "__main__":
    um = UserManager()
    print(um.add_user("张三", 18))
    print(um.add_user("李四", 20))
    print(um.get_user(1))
    um.update_age(1, 19)
    print(um.list_users())
    um.save_to_json("users.json")
    um2 = UserManager()
    um2.load_from_json("users.json")
    print(um2.list_users())
