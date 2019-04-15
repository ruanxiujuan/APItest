import xlrd



# 打开excel
wb = xlrd.open_workbook(r"D:\Projects\test\15期\接口测试\day04\data\加油卡完整用例.xls")
# sh = wb.sheet_by_index(0)
sh = wb.sheet_by_name("添加加油卡")

print(sh.nrows)  # 行数
print(sh.ncols)  # 列数

print(sh.cell(0,0).value)   # 获取某个单元格的值

title = sh.row_values(0)  # 获取一行数据
case_data = sh.row_values(1)

data = dict(zip(title, case_data))
print(data)
url = data["接口地址(名称)URL"]
data2 = data["入参"]
print(url)
print(data2)


