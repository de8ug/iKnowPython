

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
            format_line['mean'] = f'注释内容：{line}'
        elif line.startswith('import'):
            format_line['type'] = 'import'
            format_line['mean'] = f'导入: {line.split()[1]}'
        elif line.find('=') > 0:
            format_line['type'] = 'var'
            format_line['mean'] = f'变量: {line.split("=")[0]}'

        elif line.startswith('def'):
            format_line['type'] = 'function'
            format_line['mean'] = f'函数: {line.split("(")[0].lstrip("def")}'


        # 空行，函数内部代码，变量内部代码，不加入结果
        if line.startswith(' ') or line.startswith('}\n'):
            # print(results[-1])
            if results[-1]['type'] == 'function' or results[-1]['type'] == 'var':
                results[-1]['inner_code'].append(line)
                # 根据不同情况，分析每一行代码含义，并累加字符串
                """分析我们的示例代码，发现主要分类如下：
                with open(filename) as f:   打开文件
                return data                 返回值为xx
                if rule_k == ljt['name']:   if 判断相等，
                    if laji in v:           判断包含关系
                for k, v in rule.items():   for循环
                print(k, v)                 直接调用
                ljt['data'].append(laji)    a调用b
                data = json.load(f)         调用某个函数，赋值给一个变量
                """
                # 去掉line的空格，回车，只判断具体语句
                line = line.strip()
                if line.startswith('#'):  # 先判断注释
                    results[-1]['mean'] += '\n' + f"注释内容：{line}" 
                elif line.startswith('with open'):
                    params = line[ line.find('(')+1:line.find(')') ]
                    if params.find(',') > 0:  # 判断是否有第二个参数
                        left, right = params.split(',')
                        results[-1]['mean'] += '\n' + f"用{right}的方式，打开文件{left}"  # 注意括号嵌套
                    else:
                        results[-1]['mean'] += '\n' + f"打开文件{params}"  # 注意括号嵌套
                elif line.startswith('return'):
                    results[-1]['mean'] += '\n' + f'返回{line.split()[1]}'
                elif line.startswith('if '):  # 注意空格
                    if line.find('==') > 0:
                        if_left = line.split('==')[0].lstrip('if')                   
                        if_right = line.split('==')[1].rstrip(':')                   
                        results[-1]['mean'] += '\n' + f'判断{if_left}与{if_right}是否相等'
                    elif line.find(' in ') > 0:  # 注意带上两边的空格
                        if_left = line.split(' in ')[0].lstrip('if')                   
                        if_right = line.split(' in ')[1].rstrip(':')                   
                        results[-1]['mean'] += '\n' + f'判断{if_left}是否属于{if_right}'
                elif line.startswith('for '):
                    if line.find(' in ') > 0:  # 注意带上两边的空格
                        for_left = line.split(' in ')[0].lstrip('for')                   
                        for_right = line.split(' in ')[1].rstrip(':')                   
                        results[-1]['mean'] += '\n' + f'循环{for_right}中的{for_left}'
                elif line.find('=') > 0 and line.find('(') > 0:  # 判断函数调用关系，过滤变量定义
                    if line.find('.') > 0 and line.find('.json') < 0:  # 找到调用函数的代码, 过滤文件后缀
                        left = line.split('=')[0]                   
                        right_a, right_b = line.split('=')[1].split('.')                   
                        results[-1]['mean'] += '\n' + f'{right_a}调用{right_b}，并赋值给{left}'
                    else:
                        left, right = line.split('=')                   
                        results[-1]['mean'] += '\n' + f'调用{right}，并赋值给{left}'
                elif line.find('(') > 0: # 最后判断直接调用的语句
                    results[-1]['mean'] += '\n' + f'直接调用{line}'
                else:
                    results[-1]['mean'] += '\n' + f'{line}'

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
        print(f'-'*50)
        print(f'line:{f["line"]}', f['str'].strip())
        print(f['mean'])