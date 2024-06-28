# json_manager.py
import json
import os

def load_json(filename):
    json_path = os.path.join('res', filename)
    if os.path.exists(json_path):
        with open(json_path, 'r') as file:
            return json.load(file)
    else:
        return []

def save_json(filename, data):
    json_path = os.path.join('res', filename)
    with open(json_path, 'w') as file:
        json.dump(data, file, indent=4)

def find_item_by_n(data, n):
    for item in data:
        if item['n'] == n:
            return item
    return None

def add_item(data, n, name, c):
    item = {'n': n, 'name': name, 'c': c}
    data.append(item)
    return data

def update_item(data, n, new_name, new_c):
    item = find_item_by_n(data, n)
    if item:
        item['name'] = new_name
        item['c'] = new_c
        return True
    return False

def delete_item_by_n(data, n):
    item_to_delete = find_item_by_n(data, n)
    if item_to_delete:
        data.remove(item_to_delete)
        return True
    return False

# 主程序入口（由main.py调用）
def manage_json(filename):
    data = load_json(filename)
    while True:
        n = input("请输入n的值(或输入'q'退出）: ")
        if n.lower() == 'q':
            save_json(filename, data)
            break
        try:
            n = int(n)
            item = find_item_by_n(data, n)
            if item:
                print(f"找到项: {item}")
                action = input("要修改(m)、删除(d)还是做其他操作(o)? ").lower()
                if action == 'm':
                    new_name = input("输入新的name: ")
                    new_c = input("输入新的c值(格式为'[a, b]'): ").strip('[]').split(',')
                    new_c = [int(c) for c in new_c]
                    if update_item(data, n, new_name, new_c):
                        print("更新成功！")
                elif action == 'd':
                    if delete_item_by_n(data, n):
                        print("删除成功！")
                elif action == 'o':
                    pass  # 其他操作可以在这里添加
                else:
                    print("无效操作！")
            else:
                create = input("未找到该项，是否要创建(y/n)? ").lower()
                if create == 'y':
                    name = input("输入name: ")
                    c = input("输入c值(格式为'[a, b]'): ").strip('[]').split(',')
                    c = [int(c) for c in c]
                    data = add_item(data, n, name, c)
                    print("创建成功！")
        except ValueError:
            print("请输入有效的n值!")

# main.py 中调用示例
# import json_manager
# json_manager.manage_json('my_data.json')
