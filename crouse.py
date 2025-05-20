import requests
from bs4 import BeautifulSoup

# 选课系统的URL
courses_url = "https://jwglxt.xcu.edu.cn/"
login_url = "https://jwglxt.xcu.edu.cn/"

# 登录信息（视情况而定）
login_data = {
    "username": "5001230407",
    "password": "ab030516.."
}

# 模拟浏览器的headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
}

# 使用session保持会话
session = requests.Session()

# 先登录（如果需要）
response = session.post(login_url, data=login_data, headers=headers)

# 获取可选课程页面
response = session.get(courses_url, headers=headers)

# 解析HTML内容
soup = BeautifulSoup(response.text, 'html.parser')

# 假设课程信息在一个表格中，可以根据实际情况调整选择器
courses_table = soup.find('table', {'id': 'courses_table'})  # 根据实际ID或Class调整
rows = courses_table.find_all('tr')[1:]  # 跳过表头行

# 遍历每一行，提取课程信息
for row in rows:
    columns = row.find_all('td')
    course_name = columns[0].text.strip()  # 课程名称
    course_id = columns[1].text.strip()  # 课程ID
    instructor = columns[2].text.strip()  # 教师
    available_slots = columns[3].text.strip()  # 剩余名额

    print(f"课程名: {course_name}, 课程ID: {course_id}, 教师: {instructor}, 剩余名额: {available_slots}")
