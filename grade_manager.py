# 学生成绩管理系统
# 用字典存所有学生数据， 格式：{"姓名"：{"科目"：分数，"科目"：分数}}

students = {}

def add_student(name):
    # 添加一个新学生
    if name in students:
        print(f"学生{name}已存在")
    else:
        students[name] = {}
        print(f"学生{name}添加成功")

def add_score(name, subject,score):
    # 给学生添加一门成绩
    if name not in students:
        print(f"学生{name}不存在，请先添加")
        return

    # 确保分数是数字
    try:
        score = float(score)
    except:
        print("分数必须是数字")
        return

    students[name][subject] = score
    print(f"已为{name}添加{subject}成绩：{score}")

def get_avg(name):
    """计算某个学生的平均分"""
    if name not in students:
        print(f"学生{name}不存在")
        return None

    scores = students[name].values()
    if not scores:
        print(f"学生{name}还没有成绩")
        return None

    avg = sum(scores) / len(scores)
    return avg

def show_all():
    """显示所有学生和成绩"""
    if not students:
        print("还没有学生数据")
        return

    for name, scores in students.items():
        print(f"\n{name}:")
        if scores:
            for subject, score in scores.items():
                print(f"  {subject}: {score}")
            avg = get_avg(name)
            print(f"  平均分：{avg:.1f}")
        else:
            print("  暂无成绩")

def delete_student(name):
    """删除一个学生"""
    if name in students:
        del students[name]
        print(f"学生{name} 已删除")
    else:
        print(f"学生{name} 不存在")


def main():
    """主菜单程序"""
    while True:
        print("\n" + "="*30)
        print("学生成绩管理系统")
        print("1.添加学生")
        print("2.添加成绩")
        print("3.查看学生平均分")
        print("4.显示所有学生")
        print("5.退出")
        print("6.删除学生")
        print("="*30)

        choice = input("请选择操作（1-5）：")

        if choice == "1":
            name = input("请输入学生姓名：")
            add_student(name)

        elif choice == "2":
            name = input("请输入学生姓名：")
            subject = input("请输入科目：")
            score = input("请输入分数")
            add_score(name,subject,score)

        elif choice == "3":
            name = input("请输入学生姓名：")
            avg = get_avg(name)
            if avg is not None:
                print(f"{name}的平均分是：{avg:.1f}")

        elif choice == "4":
            show_all()

        elif choice == "5":
            print("感谢使用，再见！")
            break

        elif choice == "6":
            name = input("请输入要删除的学生姓名：")
            delete_student(name)

        else:
            print("无效选择，请重新输入")

# 启动程序
if __name__ == "__main__":
    main()