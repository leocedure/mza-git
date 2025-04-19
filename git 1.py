import json
import os

# 数据存储文件
DATA_FILE = "scores.json"


# 初始化数据存储
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

#这个注释是我随便添加一下注释qwq
#在代码文件中添加注释保存修改
def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)


# 核心功能函数
def record_score(data):
    print("\n【记录学生成绩】")
    print("—— 记录学生成绩 ——")

    while True:
        try:
            name = input("请输入学生姓名：").strip()
            stu_id = input("请输入学生学号：").strip()

            # 检查学号是否重复
            if any(record['学号'] == stu_id for record in data):
                print("错误：该学号已存在！")
                continue

            course = input("请输入课程名称：").strip()
            score = float(input("请输入成绩（0-100）："))

            if not 0 <= score <= 100:
                print("错误：成绩必须在0-100之间！")
                continue

            data.append({
                "姓名": name,
                "学号": stu_id,
                "课程": course,
                "成绩": score
            })
            save_data(data)
            print("成绩已成功记录！")
            return

        except ValueError:
            print("错误：请输入有效的数字成绩！")


def query_score(data):
    print("\n【查询学生成绩】")
    print("—— 查询学生成绩 ——")
    print("请选择查询方式：")
    print("1. 按学生姓名查询")
    print("2. 按学生学号查询")
    print("3. 按课程名称查询")

    choice = input("请输入选项序号：").strip()
    keyword = input("请输入查询关键词：").strip().lower()

    results = []
    for record in data:
        if choice == '1' and record['姓名'].lower() == keyword:
            results.append(record)
        elif choice == '2' and record['学号'] == keyword:
            results.append(record)
        elif choice == '3' and record['课程'].lower() == keyword:
            results.append(record)

    if not results:
        print("未找到相关记录")
    else:
        for record in results:
            print(f"姓名：{record['姓名']}，学号：{record['学号']}，课程：{record['课程']}，成绩：{record['成绩']}")


def show_menu():
    print("\n欢迎使用学生成绩管理系统")
    print("请选择操作：")
    print("1. 记录学生成绩")
    print("2. 查询学生成绩")
    print("3. 统计课程成绩")
    print("4. 退出系统")


def main():
    data = load_data()

    while True:
        show_menu()
        choice = input("请输入选项序号：").strip()

        if choice == '1':
            record_score(data)
        elif choice == '2':
            query_score(data)
        elif choice == '3':
            # 统计功能留待后续开发
            print("统计功能正在开发中...")
        elif choice == '4':
            print("\n感谢使用学生成绩管理系统，再见！")
            break
        else:
            print("错误：请输入有效的选项序号（1-4）！")


if __name__ == "__main__":
    main()