# 学生成绩管理系统
# 用字典存所有学生数据， 格式：{"姓名"：{"科目"：分数，"科目"：分数}}
# === 1. 导入模块 ===

import json
import os

# === 2. 定义 main 函数（现在在最前面） ===
def main():
    """主菜单程序"""
    load_data()

    while True:
        print("\n" + "=" * 30)
        print("学生成绩管理系统")
        print("1.添加学生")
        print("2.添加成绩")
        print("3.查看学生平均分")
        print("4.显示所有学生")
        print("5.退出")
        print("6.删除学生")
        print("7.按科目统计平均分")
        print("8.按分数筛选学生")
        print("9.修改学生成绩")
        print("10.按总分排名")
        print("11. 班级成绩统计")
        print("12. 查看学生详细成绩")
        print("13. 重置所有数据")
        print("14. 从文件导入成绩")
        print("15. 搜索学生")
        print("16. 各科目最高/最低分")
        print("17. 导出学生名单")
        print("18. 查看缺考学生")
        print("19. 按科目查询学生")
        print("20. 统计学生总数")
        print("21. 查看无成绩学生")
        print("22. 分数段统计")
        print("=" * 30)

        choice = input("请选择操作（1-22）：")

        if choice == "1":
            name = input("请输入学生姓名：")
            add_student(name)

        elif choice == "2":
            name = input("请输入学生姓名：")
            subject = input("请输入科目：")
            score = input("请输入分数：")
            add_score(name, subject, score)

        elif choice == "3":
            name = input("请输入学生姓名：")
            avg = get_avg(name)
            if avg is not None:
                print(f"{name}的平均分是：{avg:.1f}")

        elif choice == "4":
            show_all()

        elif choice == "5":
            save_data()  # 退出前保存数据
            print("感谢使用，再见！")
            break

        elif choice == "6":
            name = input("请输入要删除的学生姓名：")
            delete_student(name)

        elif choice == "7":
            subject_avg()

        elif choice == "8":
            filter_by_score()

        elif choice == "9":
            update_score()

        elif choice == "10":
            rank_students()

        elif choice == "11":
            class_stats()

        elif choice == "12":
            student_detail()

        elif choice == "13":
            reset_data()

        elif choice == "14":
            import_from_csv()

        elif choice == "15":
            search_student()

        elif choice == "16":
            best_worst_subject()

        elif choice == "17":
            export_names()

        elif choice == "18":
            missing_scores()

        elif choice == "19":
            search_by_subject()

        elif choice == "20":
            student_count()

        elif choice == "21":
            empty_check()

        elif choice == "22":
            score_segment()

        else:
            print("无效选择，请重新输入")

# === 3. 定义全局变量 ===
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

def subject_avg():
    """按科目统计所有学生的平均分"""
    if not students:
        print("还没有学生数据")
        return

    # 收集每个科目的所有分数
    subject_scores = {}
    for name, scores in students.items():
        for subject,score in scores.items():
            if subject not in subject_scores:
                subject_scores[subject] = []
            subject_scores[subject].append(score)

    # 计算并打印每个科目的平均分
    print("\n各科目平均分：")
    for subject, scores in subject_scores.items():
        avg = sum(scores) / len(scores)
        print(f"  {subject}: {avg:.1f}分")

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

def filter_by_score():
    """按分数筛选学生"""
    if not students:
        print("还没有学生数据")
        return

    try:
        min_score = float(input("请输入最低分："))
        max_score = float(input("请输入最高分："))
    except:
        print("请输入有效的数字")
        return

    if min_score > max_score:
        print("最低分不能高于最高分")
        return

    print(f"\n分数在 {min_score} - {max_score} 之间的学生：")
    found = False
    for name,scores in students.items():
        for subject, score in scores.items():
            if min_score <= score <= max_score:
                found = True

    if not found:
        print("  没有找到符合条件的学生")

def update_score():
    """修改学生成绩"""
    if not students:
        print("还没有学生数据")
        return

    name = input("请输入学生姓名：")
    if name not in students:
        print(f"学生 {name} 不存在")
        return

    if not students[name]:
        print(f"学生 {name} 还没有成绩")
        return

    # 显示该学生现有的成绩
    print(f"\n{name} 的现有成绩：")
    for subject, score in students[name].items():
        print(f"  {subject}: {score}分")

    subject = input("请输入要修改的科目：")
    if subject not in students[name]:
        print(f"科目{subject} 不存在")
        return

    try:
        new_score = float(input("请输入新分数："))
    except:
        print("分数必须是数字")
        return

    students[name][subject] = new_score
    print(f"{name} 的{subject} 成绩已修改为{new_score}分")

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

def save_data():
    """把学生数据保存到文件"""
    try:
        with open('grade_data.json', 'w', encoding = 'utf-8') as f:
            json.dump(students, f, indent=4, ensure_ascii=False)
            print("数据保存成功")
    except:
        print("数据保存失败")

def load_data():
    """从文件中加载学生数据"""
    global students
    if os.path.exists('grade_data.json'):
        try:
            with open('grade_data.json', 'r', encoding = 'utf-8') as f:
                students = json.load(f)
                print("数据加载成功")
        except:
            print("数据加载失败，使用空数据")
    else:
        print("没有找到保存的文件，使用空数据")

def rank_students():
    """按学生总分从高到低排名"""
    if not students:
        print("还没有学生数据")
        return

    # 计算每个学生的总分
    rank_list = []
    for name, scores in students.items():
        if scores: # 如果有成绩
            total = sum(scores.values())
            rank_list.append((name, total))

    if rank_list:
        print("还没有学生有成绩")
        return

    # 按总分从高到低排序
    rank_list.sort(key = lambda x: x[1], reverse = True)

    # 打印排名
    print("\n====学生总分排名====")
    for i, (name, total) in enumerate(rank_list, 1):
        print(f"{i}. {name} —— 总分：{total}")

def class_stats():
        """统计全班成绩"""
        if not students:
            print("还没有学生数据")
            return

        all_scores = []
        total_sum = 0
        count = 0

        for name, scores in students.items():
            for subject, score in scores.item():
                all_scores.append(score)
                total_sum += score
                count += 1

        if count == 0:
            print("还没有成绩数据")
            return

        avg = total_sum / count
        max_score = max(all_scores)
        min_score = min(all_scores)

        print("\n==== 班级成绩统计 ====")
        print(f"总分数：{total_sum}")
        print(f"平均分：{avg:.1f}")
        print(f"最高分：{max_score}")
        print(f"最低分：{min_score}")
        print(f"参与统计的成绩数：{count}")

def student_detail():
    """查看单个学生的所有成绩和统计"""
    name = input("请输入学生姓名：")
    if name not in students:
        print(f"学生{name} 不存在")
        return

    if not students[name]:
        print(f"学生{name} 还没有成绩")
        return

    print(f"\n==== {name} 的成绩单 ====")
    total = 0
    for subject, score in students[name].items():
        print(f" {subject}: {score}分")
        total += score

    avg = total / len(students[name])
    print(f"总分：{total}")
    print(f"平均分：{avg:1f}")

def reset_data():
    """清空所有学生数据"""
    global students
    confirm = input("确定要清空所有的数据吗？(y/n)")
    if confirm.lower() == "y":
        students = {}
        print("数据已清空")
        # 顺便删掉保存的文件
        if os.path.exists('grade_data.json'):
            os.remove('grade_data.json')
            print("存档文件已删除")
        else:
            print("操作取消")

def import_from_csv():
    """"从CSV文件导入成绩"""
    import csv

    filename = input("请输入要导入的文件名（如 grades.csv）:")

    try:
        with open(filename, 'r', encoding = 'utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            count = 0
            for row in reader:
                if len(row) >= 3:
                    name,subject,score = row[0],row[1],row[2]
                    if name not in students:
                        students[name] = {}
                    students[name][subject] = score
                    count += 1
            print(f"成功导入{count}条成绩")
    except FileNotFoundError:
        print(f"文件{filename} 不存在")
    except Exception as e:
        print(f"导入失败：{e}")

def search_student():
    """模糊搜索学生"""
    keyword = input("请输入学生姓名关键词：").strip()
    found = False
    for name in students.keys():
        if keyword in name:
            print(f"\n{name}:")
            if students[name]:
                for subject,score in students[name].items():
                    print(f"  {subject}: {score}")
            else:
                print("  暂无成绩")
            found = True
    if not found:
        print(f"未找到姓名包含 '{keyword}'的学生")

def best_worst_subject():
    """查看班级最高分和最低分科目"""
    if not students:
        print("还没有学生数据")
        return

    subject_stats = {}
    for name,scores in students.items():
        for subject, score in scores.items():
            if subject not in subject_stats:
                subject_stats[subject] = {'max': score, 'min': score,'total': score,'count': 1}
            else:
                subject_stats[subject]['max'] = max(subject_stats[subject]['max'], score)
                subject_stats[subject]['min'] = min(subject_stats[subject]['min'], score)
                subject_stats[subject]['total'] += score
                subject_stats[subject]['count'] += 1

    print("\n各科目统计：")
    for subject, stats in subject_stats.items():
        avg = stats['total'] / stats['count']
        print(f"\n{subject}:")
        print(f"  最高分： {stats['max']}")
        print(f"  最低分： {stats['min']}")
        print(f"  平均分： {avg:.1f}")

def export_names():
    """导出学生名单到文件"""
    if not students:
        print("还没有学生数据")
        return

    filename = input("请输入要保存的文件名（如 names.txt）:")
    try:
        with open(filename, 'w', encoding = 'utf-8') as f:
            for name in sorted(students.keys()):
                f.write(name + '\n')
        print(f"学生名单已导出到{filename}")
    except:
        print("导出失败")

def missing_scores():
    """查看还没有成绩的学生"""
    if not students:
        print("还没有学生成绩")
        return

    missing = []
    for name, scores in students.items():
        if not scores:
            missing.append(name)

    if missing:
        print("\n还没有成绩的学生：")
        for name in missing:
            print(f" {name}:")
        else:
            print("所有学生都有成绩")

def search_by_subject():
    """按科目查询有哪些学生"""
    subject = input("请输入科目名称：").strip()
    found = False
    for name,scores in students.items():
        if subject in scores:
            print(f"{name}: {scores[subject]}分")
            found = True
    if not found:
        print(f"没有学生选修 {subject}")

def student_count():
    """统计学生总数和男女比例（假设名字最后一位是性别标记）"""
    total = len(students)
    male = 0
    female = 0
    for name in students.key():
        if name.endswith('熊') or name.endwith('刚') or name.endwith('伟'):
            male += 1
        elif name.endwith('芳') or name.endwith('丽') or name.endwith('娜'):
            female += 1
    print(f"\n学生总数：{total}")
    if male + female > 0:
        print(f"男生：{male}, 女生：{female}")
    else:
        print("无法识别性别（可手动添加标记）")

def empty_check():
    """检查是否有空的学生记录（没有成绩）"""
    empty_list = []
    for name, scores in students.items():
        if not scores:
            empty_list.append(name)
            if empty_list:
                print(f"\n以下学生还没有成绩：")
                for name in empty_list:
                    print(f"  {name}")
            else:
                print("所有学生都有成绩")

def score_segment():
    """统计各分段人数"""
    seg = {'90-100':0, '88-89':0, '70-79':0, '60-69':0, '0-59':0}
    for name, score in students.items():
        if score >= 90:
            seg['90-100'] += 1
        elif score >= 80:
            seg['80-89'] += 1
        elif score >= 70:
            seg['70-79'] += 1
        elif score >= 60:
            seg['60-69'] += 1
        else:
            seg['0-59'] += 1
    print("\n各分段人数：")
    for k, v in seg.items():
        print(f"{k}: {v}人")

# 启动程序
if __name__ == "__main__":
    main()