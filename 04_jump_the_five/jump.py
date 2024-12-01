#!/usr/bin/env python3
"""
Author : maxiaofei <maxiaofei@localhost>
Date   : 2024-12-01
Purpose: Jump the Five
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    # 为查询表创建一个字典
    jumper = {
        '1': '9',
        '2': '8',
        '3': '7',
        '4': '6',
        '5': '0',
        '6': '4',
        '7': '3',
        '8': '2',
        '9': '1',
        '0': '5'
    }

    # 处理输入文本中的每一个字符
    for char in args.text:
        # 打印该字符在字典中的对应值，或打印该字符本身。改变print()中的"end"值，以避免添加一个新行
        print(jumper.get(char, char), end='')
    print()

# --------------------------------------------------
if __name__ == '__main__':
    main()
