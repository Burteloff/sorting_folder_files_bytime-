#
import os, time, shutil
file_name='.\\icons' #переделать на input(), пока для теста оставить эту папку
class SortTime():
    def __init__(self,file_name):
        self.file_name=file_name #принимаем название файлика
    def search(self):
        for dirpath, dirnames, filenames in os.walk(file_name): #пройдемся по файлику найдет пути, имена файлов и т.д
            for file in filenames: #Далее пойдем уже по самим файликам (там был список файликов)
                full_file=os.path.join(dirpath,file) #Преобразуем название файла в путь к файлу
                file_time_sec=os.path.getctime(full_file) #Здесь смотрит время, когда файлик был изменен
                full_time = time.gmtime(file_time_sec) #Там было время компьютерное, теперь в человечный массив
                year,month = full_time.tm_year,full_time.tm_mon #Возьмем из него только год и месяц
                year_file=file_name++f"\\{year}" #Это будущее название файла
                if (os.path.exists(year_file)):
                    mon_file = year_file + f"\\{month}"
                    if (os.path.exists(mon_file)):
                        new_full = os.path.join(year_file, file)
                        if (os.path.exists(new_full)):
                            mon_file_copy = os.path.join(mon_file, "copy")
                            os.makedirs(year_file)
                            shutil.copy2(full_file, mon_file_copy)
                        else:
                            shutil.copy2(full_file, mon_file)
                    else:
                        os.makedirs(mon_file)
                        new_full = os.path.join(year_file, file)
                        if (os.path.exists(new_full)):
                            mon_file_copy = os.path.join(mon_file, "copy")
                            os.makedirs(year_file)
                            shutil.copy2(full_file, mon_file_copy)
                        else:
                            shutil.copy2(full_file, mon_file)

                else:
                    os.makedirs(year_file)
                    mon_file = year_file + f"\\{month}"
                    if (os.path.exists(mon_file)):
                        new_full = os.path.join(year_file, file)
                        if (os.path.exists(new_full)):
                            mon_file_copy = os.path.join(mon_file, "copy")
                            os.makedirs(year_file)
                            shutil.copy2(full_file, mon_file_copy)
                        else:
                            shutil.copy2(full_file, mon_file)
                    else:
                        os.makedirs(mon_file)
                        new_full = os.path.join(year_file, file)
                        if (os.path.exists(new_full)):
                            mon_file_copy = os.path.join(mon_file, "copy")
                            os.makedirs(year_file)
                            shutil.copy2(full_file, mon_file_copy)
                        else:
                            shutil.copy2(full_file, mon_file)

