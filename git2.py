class StudentGradeManager:
    def __init__(self):
        self.students = []
        self.courses = set()
        self.student_ids = set()

    def add_grade(self):
        """记录学生成绩"""
        print("\n--- 记录学生成绩 ---")
        while True:
            try:
                name = input("请输入学生姓名：").strip()
                if not name:
                    raise ValueError("姓名不能为空")

                student_id = input("请输入学生学号：").strip()
                if not student_id.isdigit():
                    raise ValueError("学号必须为数字")
                if student_id in self.student_ids:
                    raise ValueError("学号已存在")

                course = input("请输入课程名称：").strip()
                if not course:
                    raise ValueError("课程名称不能为空")

                grade = float(input("请输入成绩（0-100）："))
                if not (0 <= grade <= 100):
                    raise ValueError("成绩必须在0-100之间")

                self.students.append({
                    "name": name,
                    "student_id": student_id,
                    "course": course,
                    "grade": grade
                })
                self.courses.add(course)
                self.student_ids.add(student_id)
                print("成绩已成功记录！")
                return
            except ValueError as e:
                print(f"输入错误：{e}，请重新输入！")

    def query_grades(self):
        """查询学生成绩"""
        print("\n--- 查询学生成绩 ---")
        while True:
            try:
                print("请选择查询方式：")
                print("1. 按学生姓名查询")
                print("2. 按学生学号查询")
                print("3. 按课程名称查询")
                choice = input("请输入选项序号：").strip()

                results = []
                if choice == "1":
                    name = input("请输入学生姓名：").strip()
                    results = [s for s in self.students if s["name"] == name]
                elif choice == "2":
                    student_id = input("请输入学生学号：").strip()
                    results = [s for s in self.students if s["student_id"] == student_id]
                elif choice == "3":
                    course = input("请输入课程名称：").strip()
                    results = [s for s in self.students if s["course"] == course]
                else:
                    raise ValueError("无效的选项")

                if not results:
                    print("未找到相关记录")
                else:
                    for record in results:
                        print(f"姓名：{record['name']}，学号：{record['student_id']}，"
                              f"课程：{record['course']}，成绩：{record['grade']:.1f}")
                return
            except ValueError as e:
                print(f"错误：{e}")

    def statistics(self):
        """统计课程成绩"""
        print("\n--- 统计课程成绩 ---")
        course = input("请输入课程名称：").strip()
        grades = [s["grade"] for s in self.students if s["course"] == course]

        if not grades:
            print("该课程暂无成绩记录")
            return

        avg = sum(grades) / len(grades)
        max_grade = max(grades)
        min_grade = min(grades)

        print(f"课程：{course}")
        print(f"平均分：{avg:.2f}")
        print(f"最高分：{max_grade:.1f}")
        print(f"最低分：{min_grade:.1f}")


def main():
    manager = StudentGradeManager()
    while True:
        print("\n欢迎使用学生成绩管理系统")
        print("请选择操作：")
        print("1. 记录学生成绩")
        print("2. 查询学生成绩")
        print("3. 统计课程成绩")
        print("4. 退出系统")

        choice = input("请输入选项序号：").strip()

        if choice == "1":
            manager.add_grade()
        elif choice == "2":
            manager.query_grades()
        elif choice == "3":
            manager.statistics()
        elif choice == "4":
            print("\n感谢使用学生成绩管理系统，再见！")
            break
        else:
            print("无效的选项，请重新输入！")


if __name__ == "__main__":
    main()