import xlwt

workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('My Sheet')
worksheet.write(0, 0, 'My Cell Contents')

# 设置单元格宽度
worksheet.col(2).width = 33333

workbook.save('cell_width.xls')
