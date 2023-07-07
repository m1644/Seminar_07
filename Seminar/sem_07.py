import os
import shutil


''' Задание_7
✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
'''

def sort_files(directory):
    video_extensions = [".mp4", ".avi", ".mkv"]
    image_extensions = [".jpg", ".jpeg", ".png", ".gif"]
    text_extensions = [".txt", ".docx", ".pdf"]
    
    video_dir = os.path.join(directory, "Видео")
    image_dir = os.path.join(directory, "Изображения")
    text_dir = os.path.join(directory, "Тексты")
    other_dir = os.path.join(directory, "Прочие")
    
    if not os.path.exists(video_dir):
        os.makedirs(video_dir)
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)
    if not os.path.exists(text_dir):
        os.makedirs(text_dir)
    if not os.path.exists(other_dir):
        os.makedirs(other_dir)
    
    files = os.listdir(directory)
    
    for file in files:
        file_path = os.path.join(directory, file)
        
        if os.path.isfile(file_path):
            _, file_extension = os.path.splitext(file)
            
            if file_extension.lower() in video_extensions:
                shutil.move(file_path, video_dir)
            elif file_extension.lower() in image_extensions:
                shutil.move(file_path, image_dir)
            elif file_extension.lower() in text_extensions:
                shutil.move(file_path, text_dir)
            else:
                shutil.move(file_path, other_dir)

# Пример использования функции
directory = "files_1"
sort_files(directory)
