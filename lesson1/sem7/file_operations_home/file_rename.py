from pathlib import Path


# Напишите функцию группового переименования файлов. Она должна:
# - принимать параметр желаемое конечное имя файлов. При переименовании в конце
# имени добавляется порядковый номер.
# - принимать параметр количество цифр в порядковом номере.
# - принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# - принимать параметр расширение конечного файла.
# - принимать диапазон сохраняемого оригинального имени. Например для диапазона
# [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
# желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
def bulk_rename(
        file_new_name: str,
        digits_count: int,
        source_ext: str,
        target_ext: str,
        path: str,
        origin_name_range: range = (3, 6)) -> int:
    work_path = Path.cwd() if path is None else Path(path)
    print(work_path)
    file_number = 0
    print(origin_name_range)
    target_ext = source_ext if target_ext is None else target_ext
    for f in work_path.iterdir():
        if f.is_file():
            file_number += 1
            file_name = f.stem[origin_name_range[0]:origin_name_range[1]]
            numeration = str(file_number).zfill(digits_count)
            name = file_name + file_new_name + numeration + (
                target_ext if "." in target_ext else f'.{target_ext}')
            f.rename(Path(f.parent, name))
