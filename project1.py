# 用字典存所有学生数据
# 格式：{“姓名”：{“科目”：分数，“科目”：分数}}

students = {}

def add_student(name):
    # 添加一个新学生
    if name in students:
        print(f"学生{name}已存在")
    else:
        students[name] = {}
        print(f"学生 {name} 添加成功")
def add_score(name,subject,score):
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