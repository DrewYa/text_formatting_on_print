import sys


def filling(list_words, last_str=False, need_len_str=80):
	''':list_words: - список слов, которые должны быть в одной строке
	разделены пробелами, чтобы в результате получилась строка длиной
	80 символов
	:last_str: - если True, то строка последняя => выравниваение слов
	по левому краю окна.
	:need_len_str: - нужная длина результирующей строки
	'''
	if last_str:
		print(' '.join(list_words).strip(), end='\n\n')
		return None
	length = len(list_words)
	need_spaces = need_len_str - len(''.join(list_words))
	# т.к. для конечного слова пробел не нужен, то количество мест,
	# в которые будем вставлять пробелы = length - 1
	count_places = length - 1

	_spaces = [0 for i in range(count_places)]
	i = 0
	while need_spaces != 0:
		_spaces[i] += 1
		need_spaces -= 1
		i += 1
		if i == count_places:
			i = 0

	spaces = [i * ' ' for i in _spaces]

	_str = '{}'.join(list_words)
	result_str = _str.format(*spaces)
	print(result_str)
	return None


def division(s):
	list_words = s.split(' ')
	sum_len = 0
	single_list_words = []
	container = [] # для списков слов

	len_list_words = len(list_words)
	for i in range(len_list_words):
		word = list_words[i]
		length = len(word) + 1
		if length == 1:
			continue
		elif sum_len + length >= 81:
			container.append(single_list_words)
			single_list_words = []
			sum_len = 0
			single_list_words.append(word)
			sum_len += length
		else:
			single_list_words.append(word)
			sum_len += length
		# если слово последнее и есть слова в single_list_words
		if i == len_list_words-1 and sum_len != 0:
			container.append(single_list_words)

	len_container = len(container)
	for i in range(len_container):
		if i == len_container - 1:
			filling(container[i], last_str=True) # последняя строка
		else:
			filling(container[i])


def main():
	if len(sys.argv) < 2:
		print('Не был указан файл с текстом')
		exit(1)

	file_path = sys.argv[1]

	try:
		with open(file_path, 'r') as file:
			content = file.read()
	except FileNotFoundError:
		print('Файл не был найден')
		exit(1)

	primary_str_list = content.split('\n')
	for s in primary_str_list:
		division(s)


if __name__ == '__main__':
	main()
