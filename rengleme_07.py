# author: DE8UG
# 创建垃圾桶和垃圾
# 规则：k:v,一个k对应一个v，代码表示用冒号分割
# 输入
# 判断
# 保存
# 函数
# 综合


import json


rule = {
    "湿垃圾": ["菜叶", "橙皮", "葱", "饼干"],
    "干垃圾": ["旧浴缸", "盆子", "海绵", "卫生纸"]
}


# print('加载文件：', ljt_gan)
def load_data(filename):
    with open(filename) as f:
        data = json.load(f)
        return data


def reng_laji(rule_k, laji, ljt):
    if rule_k == ljt['name']:
        ljt['data'].append(laji)


def fenlei(laji, rule, ljt):
    for k, v in rule.items():
        print(k, v)
        if laji in v:
            print('找到了垃圾：', laji, k)
            reng_laji(k, laji, ljt)
            # reng_laji(k, laji, ljt_shi)
        

# 用函数封装写文件的代码
def save_to_file(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f)


def main():

    # 定义垃圾桶
    ljt_shi = {
        'name': "湿垃圾",
        'data': []
    }

    ljt_gan = {
        'name': "干垃圾",
        'data': []
    }

    # 加载已有的垃圾
    ljt_gan = load_data('gan.json')
    ljt_shi = load_data('shi.json')

    print('加载文件：', ljt_gan, ljt_shi)

    # 扔垃圾
    laji = input("输入要扔的垃圾：")
    print("垃圾：", laji)

    # 分类
    fenlei(laji, rule, ljt_gan)
    fenlei(laji, rule, ljt_shi)

    print('-'*20)
    print(ljt_shi)
    print(ljt_gan)

    # 调用函数，保存到具体的垃圾桶文件
    save_to_file('gan.json', ljt_gan)
    save_to_file('shi.json', ljt_shi)


if __name__ == "__main__":
    main()



