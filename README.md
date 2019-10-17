# MyOceanPrograming
https://blog.csdn.net/Goldxwang/article/details/93893862 #to read file data
# coding = utf-8
# /usr/yangshugang/Anaconda3 python3.7

Author:Yang Shugang
Email :yangshugang12@stu.ouc.edu.cn or yangshugang@theidi.com
Number:18205422083
date  :2019-10-16 09:45
introduction:uesd 

from numpy import *

def loadDataSet(fileName):
    '''导入数据'''
    numFeat = len(open(fileName).readline().split('\t')) - 1
    dataMat = []
    labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = []
        curLine = line.strip().split('\t')
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))
    return dataMat, labelMat

if __name__ == "__main__":
    '''线性回归'''
    datafile = u'D:/2019工作项目/201909温州洞头大小门岛/sontek/GPS_MODEL_SpringTide083113-083121/08311930/WENZH1908311930.spd'
    #datafile = 'ex0.txt'
    xArr, yArr = loadDataSet(datafile)
    #xArr, yArr = loadDataSet('ex0.txt')
    print('xArr= \n', yArr)
    print('yArr= \n',  yArr)

    '''
     
    import csv
    import sys
    filename = 'ex5.csv'
    data = []
    try:
        with open(filename) as f:
            reader = csv.reader(f)
            header = reader.next()
            data = [row for row in reader]
    except csv.Error as e:
        print "Error reading CSV file at line %s : %s" % (reader.line_num, e)
        sys.exit(-1)
    if header:
        print header
        print "=========="
    for datarow in data:
        print datarow
     
     
    # 从Excel文件中导入数据
    '''
    步骤：
    1. 打开文件的工作簿。
    2. 根据名称找到工作表。根据行数（nrows）和列数（ncols）读取单元格的内容。
    3. 打印出数据集合。
    '''
    import xlrd
    file = 'output.xls'
    wb = xlrd.open_workbook(file)
    ws = wb.sheet_by_name("sheet1")
    dataset = []
    for r in xrange(ws.nrows):
        col = []
        for c in range(ws.ncols):
            col.append(ws.cell(r, c).value)
        dataset.append(col)
    # 美化打印
    from pprint import pprint
    pprint(dataset)
     
    # 从定宽数据文件导入数据
    '''
    步骤：
    1.指定要读取的数据文件。
    2.定义数据读取的方式。
    3.逐行读取文件并根据格式把每一行解析成单独的数据字段。
    4.按单独数据字段的形式打印每一行。
    '''
    import struct
    datafile = 'fix-width.data'
    # 掩码定义为5s10s5s，表示为9个字符的字符串，跟一个10个字符的字符串，再跟一个5个字符的字符串（包括空格）。
    mask = '5s10s5s'
    results = []
    with open(datafile, 'r') as f:
        for line in f:
            # 用格式解析的unpack_from方法。
            fields = struct.Struct(mask).unpack_from(line)
            results.append([field.strip() for field in fields])
    from pprint import pprint
    pprint(results)
     
     
    # 从制表符分隔的文件中读取数据
    '''
    制表符分隔的文件大部分是可以用CSV文件导入的方法，除了一些不正常的文件。这时就需要在切分前对特殊行的数据进行单独清理。
    '''
     
    from pandas import DataFrame
    lines = []
    datafile = 'data_dirty.tab'
    with open(datafile, "r") as f:
        for line in f:
            line = line.strip().split("\t")
            lines.append(line)
            results = DataFrame(lines[1:], columns=[lines[0]])
    print results
     
     
    # 从JSON数据源导入数据
    '''
    步骤：
    1.指定URL读取JSON格式数据
    2.使用requests模块访问指定的URL，并获取内容
    3.读取内容并将转化为JSON格式的对象
    4.迭代访问JSON对象，读取每一个代码库的URL值
    '''
    import requests
    url = 'https://github.com/timeline.json'
    r = requests.get(url)
    json_obj = r.json()
    repos = set()
    for entry in json_obj:
        print entry
     
        try:
            repos.add(entry['repository']['url'])
        except KeyError as e:
            print "No key %s Skipping..." % (e)
    from pprint import pprint
    pprint(repos)
     
    # 从HTML中导入数据
    from lxml.html import parse
    from urllib2 import urlopen
    parsed = parse(urlopen("https://finance.yahoo.com/q/op?s=AAPL+Options"))
    # 找到文档中的表格，并将其导入。
    doc = parsed.getroot()
    table = doc.findall(".//table")
    # 然后选择一个表格做测试。
    put = table[1]
    # 对于一个表格来说，有一个标题和数据。在HTML中th单元格就表示标题行，td则表示数据行。
    def _unpack(row, kind="td"):
        elts = row.findall(".//%s" % kind)
        return [val.text_content() for val in elts]
    # 同时，在导入数据表格时，应该考虑到文本类型。我们使用pandas中的TextParser类自动类型转换。
    from pandas.io.parsers import TextParser
    def parse_options_data(table):
        rows = table.findall(".//tr")
        header = _unpack(rows[0], kind="th")
        data = [_unpack(r) for r in rows[1:]]
        return TextParser(data, names=header).get_chunk()
    # 最后对这个表格调用该解析函数
    put_data = parse_options_data(put)
    print put_data[:10]
    # 同时，我们也可以获取文档的全部URL
    # 链接的标签是a。
    links = doc.findall(".//a")
    # print links[15:20]
    # 得到一个链接的URL和文本内容分别使用，get()和text_content()方法
    urls = [lnk.get("href") for lnk in links]
    text = [lnk.text_content() for lnk in links]
    from pprint import pprint
    pprint(urls[:10])
    print “============”

