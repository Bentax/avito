def convert_filename(filename):
    try:
        if filename.startswith("IMG_") and filename.endswith(".jpg"):
            # Обработка формата IMG_YYYYMMDD_HHMMSSNNN.jpg
            img_name = filename[len("IMG_"):-len(".jpg")]
            if len(img_name) != 17:
                return None

            year = img_name[0:4]
            month = img_name[4:6]
            day = img_name[6:8]

            months = {
                '01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr',
                '05': 'May', '06': 'Jun', '07': 'Jul', '08': 'Aug',
                '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'
            }
            if month not in months:
                return None
            
            month_text = months[month]

            return f"{year}_{month_text}_{day}_PYTHON_CONFERENCE.jpg"

        elif filename.startswith("DCIM-") and filename.endswith(".jpg"):
            # Обработка формата DCIM-YYYY-MM-DD-N.jpg
            parts = filename.split('-')
            if len(parts) != 5 or parts[0] != "DCIM" or parts[4][-4:] != ".jpg":
                return None

            year = parts[1]
            month = parts[2]
            day = parts[3]

            months = {
                '01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr',
                '05': 'May', '06': 'Jun', '07': 'Jul', '08': 'Aug',
                '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'
            }
            if month not in months:
                return None
            
            month_text = months[month]

            return f"{year}_{month_text}_{day}_PYTHON_CONFERENCE.jpg"

        elif len(filename) == 17 and filename[-5] == '-' and filename[-4:].isdigit():
            # Обработка формата YYYYMMDDHHMMSS-1.jpg
            year = filename[0:4]
            month = filename[4:6]
            day = filename[6:8]

            months = {
                '01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr',
                '05': 'May', '06': 'Jun', '07': 'Jul', '08': 'Aug',
                '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'
            }
            if month not in months:
                return None
            
            month_text = months[month]

            return f"{year}_{month_text}_{day}_PYTHON_CONFERENCE.jpg"

        else:
            return None

    except Exception as e:
        return None

def main():
    import sys
    input_lines = sys.stdin.read().strip().split('\n')

    events = []
    files = []

    # Чтение входных данных и разделение на события и файлы
    for line in input_lines:
        if line.startswith("IMG_") or line.startswith("DCIM-") or len(line) == 17:
            files.append(line)
        else:
            events.append(line)

    results = {}

    # Обработка каждого события
    for event in events:
        parts = event.split()
        if len(parts) != 4:
            continue

        event_name = parts[0]
        year = parts[1]
        month = parts[2]
        day = parts[3]

        formatted_event_name = f"{year}_{month}_{day}_{event_name}"

        results[formatted_event_name] = []

        # Обработка файлов для текущего события
        for filename in files:
            converted_filename = convert_filename(filename)
            if converted_filename is not None and converted_filename.startswith(f"{year}_{month}_{day}_"):
                results[formatted_event_name].append(converted_filename)

        # Сортировка файлов по имени для текущего события
        results[formatted_event_name].sort()

    # Вывод отсортированных файлов
    for event_name, filenames in results.items():
        for idx, filename in enumerate(filenames, start=1):
            print(filename)

if __name__ == "__main__":
    main()


'''
На вход подаётся список из трёх мероприятий с датами. По одному на строку. Разделитель внутри строки - пробел. 
Формат: 
EVENT_NAME yyyy mm dd
Список названий файлов
Файлы также из трёх источников и формат названия у них разный - такой же, как в прошлой задаче. 
Упорядоченность списка файлов на входе не гарантируется.

Пример тестовых данных(количество строк с файлами может отличаться):
VERNITE_MOI 2007 07 07
TEST 2000 01 01
POKEMON_GO 2023 04 30
IMG_20070707_001311111.jpg
IMG_20070707_001412000.jpg
IMG_20070707_001617235.jpg
IMG_20070707_002424603.jpg
DCIM-2000-01-01-1.jpg
DCIM-2000-01-01-2.jpg
202304300924-1.jpg
202304301001-2.jpg
202304301012-3.jpg

На выходе ожидается отсортированный текст, где каждая строка - название файла. Формат как в Примере 2.
2023_Apr_30_POKEMON_GO_1.jpg
2023_Apr_30_POKEMON_GO_2.jpg
2023_Apr_30_POKEMON_GO_3.jpg
2000_Jan_01_TEST_1.jpg
2000_Jan_01_TEST_2.jpg
2007_Jul_07_VERNITE_MOI_1.jpg
2007_Jul_07_VERNITE_MOI_2.jpg
2007_Jul_07_VERNITE_MOI_3.jpg
2007_Jul_07_VERNITE_MOI_4.jpg

Sample Input:
VACATION_GREECE 2021 11 27
CHESS_TOURNAMENT 2004 12 18
CONFERENCE 2002 08 02
200208020145-6.jpg
200208020053-10.jpg
DCIM-2021-11-27-0.jpg
DCIM-2002-08-02-6.jpg
DCIM-2004-12-18-3.jpg
202111271009-2.jpg
200412180835-8.jpg
DCIM-2002-08-02-10.jpg
202111270804-5.jpg

Sample Output:
2002_Aug_02_CONFERENCE_1.jpg
2002_Aug_02_CONFERENCE_2.jpg
2002_Aug_02_CONFERENCE_3.jpg
2002_Aug_02_CONFERENCE_4.jpg
2004_Dec_18_CHESS_TOURNAMENT_1.jpg
2004_Dec_18_CHESS_TOURNAMENT_2.jpg
2021_Nov_27_VACATION_GREECE_1.jpg
2021_Nov_27_VACATION_GREECE_2.jpg
2021_Nov_27_VACATION_GREECE_3.jpg

Напишите программу. Тестируется через stdin → stdout
'''
