#!/usr/bin/env python3
"""
Author : maxiaofei <maxiaofei@localhost>
Date   : 2024-11-27
Purpose: Crow's Nest
"""

import argparse


# --------------------------------------------------
# 定义函数get_args()，以处理命令行实参。
def get_args():
    """Get command-line arguments"""

    # 解析器将解析这些实参
    parser = argparse.ArgumentParser(
        description="Crow's Nest -- choose the correct article",
        # description将出现在使用说明中，描述该程序做什么
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        #在使用说明中显示针对每个参数的默认值

    parser.add_argument('word', metavar='word', help='A word')
    # 定义一个名为word的位置实参

    return parser.parse_args()
    # 这些实参的解析结果将返回到main()


# --------------------------------------------------
# 定义main函数，该程序将在这里开始
def main():
    """Make a jazz noise here"""

    args = get_args()
    # args含有get_args()函数的返回值
    word = args.word
    # 把来自实参的args.word值放入该word变量
    article = 'an' if word[0].lower() in 'aeiou' else 'a'
    # 选择正确的冠词，使用if表达式以查看word的第一个小写字符是否在元音集中
    print(f'Ahoy, Captain, {article} {word} off the larboard bow!')
    # 使用f-string打印该输出字符串，以把article和word变量插入到字符串内


# --------------------------------------------------
if __name__ == '__main__':
    main()
