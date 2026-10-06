import json
import os


def analyze_log(filepath: str) -> dict:
    result = {
        "total": 0,
        "by_level": {},
        "by_user": {},
        "last_error": None
    }
    if not os.path.exists(filepath):
        return result
    # 文件不存在时返回空结果字典
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:  # 空文件时不会进入循环
            try:
                data = json.loads(line)
            except:
                continue
            # 某行 json.loads 失败时跳过该行，不得中断整个解析
            result["total"] += 1
            level = data["level"]
            user = data["user"]
            if level in result["by_level"]:
                result["by_level"][level] += 1
            else:
                result["by_level"][level] = 1
            if user in result["by_user"]:
                result["by_user"][user] += 1
            else:
                result["by_user"][user] = 1
            if level == "ERROR":
                result["last_error"] = data["message"]
    return result


if __name__ == "__main__":
    print(analyze_log("app.jsonl"))
