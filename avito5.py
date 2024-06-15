def convert_filename(filename):
    try:
        # Проверяем, в каком формате представлено имя файла
        if filename.startswith("IMG"):
            # Формат "IMG_YYYYMMDD_HHMMSSNNN.jpg"
            parts = filename.split('_')
            if len(parts) != 3:
                return "Invalid input format"

            date_time = parts[1]
            if len(date_time) != 15:
                return "Invalid input format"
            
            year = date_time[:4]
            month = date_time[4:6]
            day = date_time[6:8]

        elif filename.startswith("DCIM"):
            # Формат "DCIM-YYYY-MM-DD-N.jpg"
            parts = filename.split('-')
            if len(parts) != 5:
                return "Invalid input format"

            year = parts[1]
            month = parts[2]
            day = parts[3]

            if len(year) != 4 or len(month) != 2 or len(day) != 2:
                return "Invalid input format"

        else:
            return "Invalid input format"

        # Преобразуем числовой месяц в текстовый формат
        months = {
            '01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr',
            '05': 'May', '06': 'Jun', '07': 'Jul', '08': 'Aug',
            '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'
        }
        if month not in months:
            return "Invalid input format"
        
        month_text = months[month]

        # Составляем новое имя файла в требуемом формате
        new_filename = f"{year}_{month_text}_{day}_PYTHON_CONFERENCE.jpg"

        return new_filename

    except Exception as e:
        return f"Error: {e}"

def main():
    import sys
    input_filename = sys.stdin.read().strip()

    new_filename = convert_filename(input_filename)
    print(new_filename)

if __name__ == "__main__":
    main()


'''
Привести все файлы к одному общему стилю именования.

Пример 1:
202304300924-1.jpg
DCIM-2023-04-30-1.jpg
IMG_20230430_092422111.jpg
где:
IMG - префикс производителя телефона или технический(Digital Camera IMages)
2023 - год
04 - месяц
30 - день
09 - час GMT+0
24 - минуты
22111 - микросекунды
1 - порядковый номер среди фото, сделанных в этот день
jpg - расширение файла

Пример 2
2023_Apr_30_PYTHON_CONFERENCE.jpg 
где:
PYTHON_CONFERENCE - название события
2023 - год
04 - месяц
30 - день
jpg - расширение файла
Напишите программу, которая сама определяет формат файла и конвертирует его в формат Пример 2

Условия:

На вход подаётся строка - название файла. Формат названия может быть одним из указанных в Примере 1.
На выходе ожидается строка - название файла. Формат как в Примере 2.
Проверка осуществляется на большом количестве тестовых "файлов" разного формата, предполагается, что все фотографии с одного мероприятия, поэтому постфикс "PYTHON_CONFERENCE" в финальном названии для всех них будет одинаковым.
Sample Input 1:
DCIM-2005-07-08-8.jpg

Sample Output 1:
2005_Jul_08_PYTHON_CONFERENCE.jpg          

Sample Input 2:
DCIM-2009-01-24-10.jpg

Sample Output 2:
2009_Jan_24_PYTHON_CONFERENCE.jpg

Напишите программу. Тестируется через stdin → stdout
'''
