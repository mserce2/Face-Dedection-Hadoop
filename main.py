# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 18:19:08 2020

@author: Mete
"""
import time
from df import DataSet
from df import DataAL
from df import DataTrain
from df import Mail

dst=DataSet("WELCOME ")
print(dst.bilgi)
dst1=DataAL()
dst2=DataTrain()
dst3=Mail()

main_menu=True
while True:
    if main_menu:
        print("""
           **********Yüz Tanıma Sistemi V:1.5********** 
           |        A.Data Oluşturma menüsü     |
           |        B.Data Eğitim menüsü        |
           |        C.Data Tanıma menüs         |
           |             Q.Çıkış                |
           --------------------------------------
        """)
        
        main_menu=False
        
        choice=input("Enter Choice :")
        
        if choice=="A"or choice=="a":
            
            print("""Data oluşturma menüsüne hoş geldiniz.
                     Devam etmek için '1' basınız
                     """)
            choice=input("Enter choice:")
            try:
                choice=int(choice)
            except ValueError:
                print("It is not integer")
                continue
            if choice==1:
                dst.dataTopla()
                main_menu=True  
            else:
                
                print("invalid input. Please enter a number between 1-6")
                main_menu=True  
                
        elif choice=="B"or choice=="b":
            print("""Data Eğitme menüsüne hoş geldiniz.
                     Devam etmek için '1' basınız
                     """)
            choice=input("Enter choice:")
            try:
                choice=int(choice)
            except ValueError:
                print("It is not integer")
                continue
            
            if choice==1:
                dst1.DataTrainSayisi()
                main_menu=True
            else:
                print("invalid input. Please enter a number between 1-6")
                main_menu=True

        elif choice=="C"or choice=="c":
            print("""Data Tanıma menüsüne hoş geldiniz.\nDevam etmek için '1' basınız
                     """)
            choice=input("Enter choice:")
            try:
                choice=int(choice)
            except ValueError:
                print("It is not integer")
                continue
            
            if choice==1:
                dst2.DataWork()
                dst3.mailAt()


                main_menu=True
            else:
                print("invalid input. Please enter a number between 1-6")
                main_menu=True


        elif choice=="Q" or choice=="q":
            break
        
        else:   
            print("ınvalid input.  Please Enter A-B-C-Q")




#dst.dataTopla()

#dst1.DataTrainSayisi()

#dst2.DataWork()

