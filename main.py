#!/usr/bin/python3
#-*- coding: utf8 -*-

from io import open


class Data():
    def __init__(self):
        self.data = None
        self.my_list = []
        self.record = 5

    def get_data(self):
        while True:
            self.data = (input("Ingresa datos: "))
            my_list = self.my_list
            my_list.append(self.data)
            self.record -= 1
            if (self.record == 0):
                print("Hemos almacenado 5 datos")
                break
        
    def save_data(self):
        self.save = open("datos_guardados.txt", "a")
        self.save.write(str(self.my_list))
        self.save.close()


    def loop_view(self):
        self.view = open("datos_guardados.txt", "r")
        run = self.view.readlines()
        self.view.close()
        for i in run:
            print(i)



data = Data()
data.get_data()
data.save_data()
data.loop_view()

#End of the program.
