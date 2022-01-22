import PySimpleGUI as sg
from os import remove
from os.path import splitext
import re 

#Параметры окна
layout_menu = [[sg.Text('Введите необходимые данные:')],
        [sg.Text('Email', size=(18, 1)), sg.Input(key="email")],
        [sg.Text('Имя', size=(18, 1)), sg.Input(key="name")],
        [sg.Text('Фамилия', size=(18, 1)), sg.Input(key="surname")],
        [sg.Text('Пароль', size=(18, 1)), sg.Input(key="password",password_char="*")],
        [sg.Text('Повтор пароля', size=(18, 1)), sg.Input(key="password_repit",password_char="*")],
        [sg.Text( size=(70, 2),key='OUTPUT')],
        [sg.Checkbox('Лицензионное соглашение',default=False,key='license')],
        [sg.Button('Зарегистрироваться') ],
        [sg.Button('Выйти')]]

#Создание окна
window = sg.Window('Форма регистрации', layout_menu)

#Проверка на спец. символы  в имени и фамилии         
def check_simvoli(value):
    if(re.search(r'\W',value)==None):        
        return(True)        
    else:
        
        return(False)

#Проверка наличия хотя бы одного спец.символа в пароле
def check_simvoli_pass(value):
    if(re.search(r'\W',value)!= None):        
        
        return(True)        
    else:
            
        return(False)

#Провекра на введеную почту, 2-х уровней домена и @
def check_email(value):
    if(re.search(r'\w@\w+.\w+', value) != None):
        return(True)
            
    else:
        print(value+'gjiuui')
        #global status
        #status = "Почта не соответствует необходимым параметрам" 
        return(False)

#Проверка максимальной длины
def check_lenght(value):
    if(len(value) < 128 ):
        return(True)
        print(value)
    elif(check_lenght(value)==None):
        return(True)
        print(value)
    else:
        return(False)
        #global status
        #status = "Количество символов не должно превышать больше 128"

#Проверка паролей на длину и соответствие
def check_pass(value):
    print(len(value))    
    if(len(value) > 8 ):
        
        if(check_simvoli_pass(value)==True):               
            return(True)
        else:
            return(False)   
    else:        
        return(False)   

#Цикл запущенного окна
while True:  
    event, values = window.read()    
 
    bufferSize = 64*1024
    email = values["email"]
    name = values["name"]
    surname = values["surname"]
    password = values["password"]
    password_repit = values["password_repit"]     
    license_check = values['license']  
    
    #Вызов необходимых функций для проверки нескольких условий для одной строки
    result_email = check_email(email) and check_lenght(email)
    #print("email"+ str(result_email))
    result_name =  check_simvoli(name) and check_lenght(name) 
    #print("name"+ str(result_name))
    result_surname =  check_simvoli(surname) and check_lenght(surname) 
    #print("surname"+ str(result_surname))        
    result_pass = check_pass(password) and check_simvoli_pass(password) 
    #print("password"+ str(result_pass))
    result_pass_repit = check_pass(password_repit) 
    #print("repit"+ str(result_pass_repit))
    

    if event in  (None, 'Выйти'):
        break

#Поочередная проверка всех необходимых условий,но не в реал тайме
    elif event == 'Зарегистрироваться':

        if(result_email==True):
            print(window['license'])        
            if(result_name==True):
                if(result_surname==True):
                    if(result_pass==True):                       
                        if((result_pass == result_pass_repit) !=False):
                            if(license_check==True):
                                
                                window['OUTPUT'].update("Все супер")
                            else:
                                window['OUTPUT'].update("Необходимо подтвердить лиценизонное соглашение")
                        else:                                                           
                            window['OUTPUT'].update("Пароли не совпадают")
                    else:
                        window['OUTPUT'].update("Количество символов в пароли должно быть больше 8 и должны присутствовать специальные символы")      
                else:
                    window['OUTPUT'].update("В Фамилии присутствуют недопустимые символы,a длина должна быть меньше 128 символов") 
            else:
               window['OUTPUT'].update("В Имени присутствуют недопустимые символы,a длина должна быть меньше 128 символов") 
        else:
            window['OUTPUT'].update("Почта не соответствует необходимому шаблону типа: \nxxx@xxx.xxx" )

#Закрытие окна
window.close()