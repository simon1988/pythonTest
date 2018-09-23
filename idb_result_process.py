import glob
from itertools import islice
import time
import os


def strip_quote(str):
    if len(str) < 2 or str[0] != '"' or str[-1] != '"':
        return str
    else:
        return str[1:-1]


def to_camel_case(snake_str):
    components = snake_str.split('_')
    # We capitalize the first letter of each component except the first one
    # with the 'title' method and join them together.
    return components[0] + ''.join(x.title() for x in components[1:])


def idb(is_strip_quote):
    files = glob.glob("/Users/simon/Downloads/执行结果-*.txt")
    files.sort(key=os.path.getmtime, reverse=True)
    print(files[0])
    with open(files[0], 'r') as f:
        res = None
        for line in f:
            if not res:
                res = line.split(",")
            else:
                cur = line.split(",")
                for index in range(len(res)):
                    if is_strip_quote:
                        res[index] = res[index] + "," + strip_quote(cur[index])
                    else:
                        res[index] = res[index] + "," + "'" + strip_quote(cur[index]) + "'"
        print("\n".join(res))


def output_reg_doc(file):
    with open('/Users/simon/Downloads/' + file, 'r') as f:
        res = ''
        for line in islice(f, 1, None):
            cur = line.split(",")
            iproleid = strip_quote(cur[5])
            alipayId = strip_quote(cur[6])
            amount = int(strip_quote(cur[7])) / 100
            res = res + "| {0} | {1} | {2} | {3}元 | 用户状态不可用 |\n".format(time.strftime("%Y-%m-%d"), iproleid, alipayId,
                                                                        amount)
        print(res)


def gen_sql_mapping(file):
    with open('/Users/simon/Downloads/' + file, 'r') as f:
        res = ''
        for line in f:
            line = line.strip()
            res = res + "<result column=\"{0}\" 			property=\"{1}\" 			jdbcType=\"VARCHAR\" />\n".format(
                line, to_camel_case(line))
        print(res)


def get_machine_list(file):
    with open('/Users/simon/tmp/' + file, 'r') as f:
        res = ''
        for line in f:
            line = line.strip()
            end = line.find("(内网)");
            if end >= 0:
                res = res+line[:end]+"\n"
        print(res)


# idb(True)
# idb(False)
# output_reg_doc('执行结果-11.txt')
# gen_sql_mapping('1.txt')
get_machine_list('machine.txt')
