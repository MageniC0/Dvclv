import json
import os

def load_json(filename):
    json_path_local = os.path.join('res', filename + '.json')
    if os.path.exists(json_path_local):
        with open(json_path_local, 'r') as file:
            return json.load(file)
    else:
        return []

def save_json(filename, data):
    json_path_local = os.path.join('res', filename + '.json')
    dir_path = os.path.dirname(json_path_local)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    with open(json_path_local, 'w') as file:
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

def get_c():
    a = input("[flu]define A:")
    b = input("[flu]define B:")
    ac = tuple(int(a[i:i+2], 16) for i in (0, 2, 4))
    bc = tuple(int(b[i:i+2], 16) for i in (0, 2, 4))
    return (ac,bc)

def manage_json(filename):
    json_path = os.path.join('res', filename + '.json')
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
                action = input("要修改(m)、删除(d)? ").lower()
                if action == 'm':
                    new_name = input("输入新的name: ")
                    new_c = get_c()
                    if update_item(data, n, new_name, new_c):
                        print("[flu]update.")
                elif action == 'd':
                    if delete_item_by_n(data, n):
                        print("[flu]delete.")
                else:
                    print("[flu]?")
            else:
                create = input("未找到该项，是否要创建(y/n)? ").lower()
                if create == 'y':
                    name = input("[flu]name: ")
                    c = get_c()
                    data = add_item(data, n, name, c)
                    print(f"[flu]saved as {filename}.")
        except ValueError:
            print("[flu]?")
