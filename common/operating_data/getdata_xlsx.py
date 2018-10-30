# -*- coding: utf-8 -*-
# @Time    : 2018/5/24 10:57
# @Author  : sssssjd
# @Email   : sssssjd@163.com
# @File    : getdata_xlsx.py
# @Software: PyCharm
import xlrd


def get_xlsxdata(filepath, sheetname):
    try:
        data = xlrd.open_workbook(filepath)
        table = data.sheet_by_name(sheetname)
        nrow = table.nrows
        ncol = table.ncols
        list_top = table.row_values(0)
        list_all = []
        for m in range(1, nrow):
            list_sub = table.row_values(m)
            dict_sub = {}
            for i in range(ncol):
                dict_sub[list_top[i]] = list_sub[i]
            list_all.append(dict_sub)
        return list_all
    except Exception as e:
        print('获取数据失败:' + str(e))
