#Day 1:变量、类型、input/print、string

# 1. 变量与类型
name = "杨育凡"        # str  字符串
age = 23               # int  整数
height = 1.75          # float 小数
is_student = True      # bool 布尔值（首字母大写！）
print(name,age,height,is_student)
print(type(name),type(age),type(height),type(is_student))

# 2. 输入与类型转换
birth_year=input("请输入你的出生年份：")
print("你输入的是：",birth_year,"类型：",type(birth_year))
real_age=2026-int (birth_year)
print("你的年龄大约是：",real_age)

# 3. f-string 格式化（字符串前加 f，变量用 {} 包起来）
print(f"你好，我是{name}，今年{real_age}岁，身高{height}米。")
print(f"两年后我{real_age+2}岁")

# 4. 小练习：打印一张个人信息卡片

print("="*30)
print(f"姓名:{name}")
print(f"年龄：{real_age}岁")
print(f"身高：{height:.2f}米")
print("="*30)


