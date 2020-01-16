

filename = 'rengleme_07.py'


def get_lines(filename):
    with open(filename) as f:
        return f.readlines()



"""
['# author: DE8UG\n', '# 创建垃圾桶和垃圾\n', 
'# 规则：k:v,一个k对应一个v，代码表示用冒号分割\n', 
'# 输入\n', '# 判断\n', '# 保存\n', '# 函数\n', '# 综合\n', '\n', '\n', 

'import json\n', '\n', '\n', 
    'rule = {\n', '    "湿垃圾": ["菜叶", "橙皮", "葱", "饼干"],
        \n', '   
         "干垃圾": ["旧浴缸", "盆子", "海绵", "卫生纸"]\n', '}\n',
              '\n', '\n', 
                  "# print('加载文件：', ljt_gan)\n", 
'def load_data(filename):\n', 
    '    with open(filename) as f:\n', 
        '        data = json.load(f)\n', 
            '        return data\n', '\n', '\n', 'def reng_laji(rule_k, laji, ljt):\n', "    if rule_k == ljt['name']:\n", "        ljt['data'].append(laji)\n", '\n', '\n', 'def fenlei(laji, rule, ljt):\n', '    for k, v in rule.items():\n', '        print(k, v)\n', '        if laji in v:\n', "            print('找到了垃圾：', laji, k)\n", '            reng_laji(k, laji, ljt)\n', '            # reng_laji(k, laji, ljt_shi)\n', '        \n', '\n', '# 用函数封装写文件的代码\n', 'def save_to_file(filename, data):\n', "    with open(filename, 'w') as f:\n", '        json.dump(data, f)\n', '\n', '\n', 'def main():\n', '\n', '    # 定义垃圾桶\n', '    ljt_shi = {\n', '        \'name\': "湿垃圾",\n', "        'data': []\n", '    }\n', '\n', '    ljt_gan = {\n', '        \'name\': "干垃圾",\n', "        'data': []\n", '    }\n', '\n', '    # 加载已有的垃圾\n', "    ljt_gan = load_data('gan.json')\n", "    ljt_shi = load_data('shi.json')\n", '\n', "    print('加载文件：', ljt_gan, ljt_shi)\n", '\n', '    # 扔垃圾\n', '    laji = input("输入要扔的垃圾：")\n', '    print("垃圾：", laji)\n', '\n', '    # 分类\n', '    fenlei(laji, rule, ljt_gan)\n', '    fenlei(laji, rule, ljt_shi)\n', '\n', "    print('-'*20)\n", '    print(ljt_shi)\n', '    print(ljt_gan)\n', '\n', '    # 调用函数，保存到具体的垃圾桶文件\n', "    save_to_file('gan.json', ljt_gan)\n", "    save_to_file('shi.json', ljt_shi)\n", '\n', '\n', 'if __name__ == "__main__":\n', '    main()\n', '\n', '\n', '\n']
"""
[
{
    'line':1,
    'str':'def load_data(filename):\n',
    'type':'function',   # code, comment, import, var
    'mean':'函数load_data，包含参数：filename'
}
]

def analysis_code(lines):
    results = []
    count = 1
    for line in lines:
        format_line = {
            'line': count,
            'str': line,
            'type':'code',   # code, comment, import, var
            'inner_code': [],
            'mean':''
        }
        if line.startswith('#'):
            format_line['type'] = 'comment'
        elif line.startswith('import'):
            format_line['type'] = 'import'
        elif line.find('=') > 0:
            format_line['type'] = 'var'
        elif line.startswith('def'):
            format_line['type'] = 'function'

        # 空行，函数内部代码，变量内部代码，不加入结果
        if line.startswith(' ') or line.startswith('}\n'):
            # print(results[-1])
            if results[-1]['type'] == 'function' or results[-1]['type'] == 'var':
                results[-1]['inner_code'].append(line)
        elif line.startswith('\n'):
            pass  # 空行直接掠过
        else:
            results.append(format_line)

        # 循环下一行   
        count += 1

    return results


if __name__ == "__main__":
    print('*'*50)
    print('欢迎使用Python算个球，掐指一算，你的代码内容如下：')
    lines = get_lines(filename)
    # print(lines[:10])
    r = analysis_code(lines)
    # print(r)
    comment_list = []
    function_list = []
    for line in r:
        # print(line)
        if line['type']=='comment':
            comment_list.append(line)
        elif line['type']=='function':
            function_list.append(line)
    print(f'- 共{len(comment_list)}个注释')
    print(f'- 共{len(function_list)}个函数：')
    for f in function_list:
        print(f'line:{f["line"]}', f['str'].strip())