### Задача

Написать скрипт, который запускается из командной строки, на вход принимает неформатированный текстовой файл, наполненный текстовыми строчками неограниченной длины.
Каждая строчка – это один абзац.
Задача скрипта - напечатать выравненный по ширине текст шириной 80 символов (за счёт добавления пробелов между словами), отделяя каждый абзац пустой строкой, используя только стандартную библиотеку Python (любые ее пакеты и модули, кроме textwrap).
При этом разбивать слова по слогам не требуется, а если получившаяся строка является окончанием абзаца, то её надо выравнивать по левому краю.

##### Реализовал, используя только `sys`
##### `python wrap.py path/to/file.txt`
