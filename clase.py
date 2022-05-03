import numpy as np

class Ventana:
    __titulo=''
    __xsup=0
    __ysup=0
    __xinf=0
    __yinf=0
    def __init__(self,titulo,x_s=0,y_s=0,x_i=500,y_i=500):
        self.__titulo=titulo
        self.__xsup=x_s
        self.__ysup=y_s
        self.__xinf=x_i
        self.__yinf=y_i
    def mostrar(self):
        print(self.__titulo)
        print('(x,y) superior izquierdo:(',self.__xsup,',',self.__ysup,')')
        print('(x,y) inferior derecho:(',self.__xinf,',',self.__yinf,')')
    def getTitulo(self):
        return self.__titulo
    def alto(self):
        return (self.__yinf-self.__ysup)
    def ancho(self):
        return (self.__xinf-self.__xsup)
    def moverDerecha(self,n=1):
        if (self.__xinf+n < 500):
            self.__xsup=self.__xsup+n
            self.__xinf=self.__xinf+n
        else:
            self.__xinf=500
    def moverIzquierda(self,n=1):
        self.__xsup=self.__xsup-n
        self.__xinf=self.__xinf-n
    def subir(self,n=1):
        self.__yinf=self.__yinf+n
        self.__ysup=self.__ysup+n
    def bajar(self,n=1):
        self.__yinf=self.__yinf-n
        self.__ysup=self.__ysup-n
