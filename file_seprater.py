import os
import shutil
print(f'your file path  {os.getcwd()}')
path=input('"Heloo sir!!" \n\ninput the path you want to saprate the files:   ')
print('\n Do you want to coninue?\n\n 1. yes \n 2. no')
a=int(input('>>  '))
if(a==1):
    try:
        os.mkdir(f'{path}\\text')
        os.mkdir(f'{path}\\photos')
        os.mkdir(f'{path}\\music')
        os.mkdir(f'{path}\\videos')
        os.mkdir(f'{path}\\pdf')
        os.mkdir(f'{path}\\pythonf')
        os.mkdir(f'{path}\\java')
    except:
        print('already created')
    finally:
        try:
            #print("already created")
            for i in os.listdir(path):
                if (i!='text' or i!='photos' or i!='videos' or i!='pdf' or i!='pythonf' or i!="project.py"):
                    if i.endswith('.txt'):
                          shutil.move(f'{path}\{i}',f'{path}\\text\{i}')
                       # print(i)
                    elif i.endswith(".jpg") or i.endswith(".png"):
                        shutil.move(f'{path}\{i}',f'{path}\\photos\{i}')
                    elif i.endswith(".mp4"):
                        shutil.move(f'{path}\{i}',f'{path}\\videos\{i}')
                    elif i.endswith(".pdf"):
                        shutil.move(f'{path}\{i}',f'{path}\\pdf\{i}')
                    elif i.endswith(".py"):
                        shutil.move(f'{path}\{i}',f'{path}\\pythonf\{i}')
                    elif i.endswith(".java"):
                        shutil.move(f'{path}\{i}',f'{path}\\java\{i}')
                    elif i.endswith("mp3"):
                        shutil.move(f'{path}\{i}',f'{path}\\music\{i}')
                    
                    else:
                        continue
            print('..................operation succesful...........................')
        except:
            print('opps......wrong input!!!')