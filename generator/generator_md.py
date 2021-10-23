def read_data(file_name):
    file = open(file_name, 'r')
    data = file.readlines()
    file.close()
    return data


def write_data(file_name, data):
    file = open(file_name, 'w')
    file.write(data)
    file.close()


def get_md_data(solution, tests):
    data = ''
    data += '# ' + solution[0] + '\n'  # заголовок
    data += get_md_link(solution[1]) + '\n'  # ссылка на подзаголовок
    data += '## ' + solution[1] + '\n'  # подзаголовок
    data += solution[2] + '\n'  # ссылка на leetcode
    data += get_md_code_block(''.join(solution[3::])) + '\n'
    data += get_formatted_test_block(''.join(tests)) + '\n'
    return data


def get_md_link(task_title):
    return '+ [{}](#{})'.format(task_title, '-'.join(map(lambda x: x.lower(), task_title.split(' '))))


def get_md_code_block(data):
    return '\n```python\n{}```\n'.format(data)


def get_formatted_test_block(tests):
    test_block = ''
    test_block += '<details><summary>Test cases</summary><blockquote>\n'  # ссылка на тесты
    test_block += get_md_code_block(tests) + '\n'
    test_block += '</blockquote></details>\n'  # "закрыть" ссылку на тесты
    return test_block


def main():
    solution = read_data('solution.txt')
    tests = read_data('tests.py')
    write_data('new_file.md', get_md_data(solution, tests))
    print('Hello')


if __name__ == '__main__':
    main()
