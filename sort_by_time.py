#
import os, time, shutil
file_name='.\\icons' #переделать на input(), пока для теста оставить эту папку
class SortTime():
    def __init__(self,file_name):
        self.file_name=file_name #принимаем название файлика
for dirpath,dirnames,filenames in os.walk(name):
    print(f"{dirpath:-^30}")
    for file in filenames:
        full_file=os.path.join(dirpath,file)
        file_time_sec=os.path.getctime(full_file)
        full_time=time.gmtime(file_time_sec)
        year=full_time.tm_year
        month=full_time.tm_mon
        print(file,year,month)
        year_file=name+f"\\{year}"
        if(os.path.exists(year_file)):
            mon_file=year_file+f"\\{month}"
            if(os.path.exists(mon_file)):
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
                new_full=os.path.join(year_file,file)
                if(os.path.exists(new_full)):
                    mon_file_copy=os.path.join(mon_file,"copy")
                    os.makedirs(year_file)
                    shutil.copy2(full_file,mon_file_copy)
                else:
                    shutil.copy2(full_file, mon_file)
