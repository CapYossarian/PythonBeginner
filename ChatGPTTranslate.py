#python
import PyPDF2
from googletrans import Translator

def translate_pdf(input_path, output_path):
    # Открываем PDF файл для чтения
    with open(input_path, 'rb') as file:
        # Создаем объект для работы с PDF
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)

        # Создаем объект для записи переведенного текста
        pdf_writer = PyPDF2.PdfWriter()

        # Создаем объект для перевода текста
        translator = Translator()

        # Перебираем каждую страницу PDF
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]

            # Извлекаем текст из страницы
            text = page.extract_text()

            # Переводим текст с английского на русский
            translated_text = translator.translate(text, src='en', dest='ru').text
            translated_text = text

            # Создаем новую страницу с переведенным текстом
            #translated_page = PyPDF2.pdf.PageObject.create_blank_page(None, page.mediaBox.getWidth(), page.mediaBox.getHeight())
            translated_page = PyPDF2.PageObject.create_blank_page(None, page.mediabox.width, page.mediabox.height)
            translated_page.merge_page(page)
            translated_page.extract_text = lambda: translated_text

            # Добавляем переведенную страницу в объект для записи
            pdf_writer.add_page(translated_page)

        # Записываем переведенный PDF в файл
        with open(output_path, 'wb') as output_file:
            pdf_writer.write(output_file)

# Пример использования
input_path = "d:/Sergey/БиблиотекаПереводчика/TheEconomistUSA.pdf"
output_path = "d:/Sergey/БиблиотекаПереводчика/TheEconomistRU.pdf"
translate_pdf(input_path, output_path)
