from django.http import HttpResponse
import datetime
from django.template import Template, Context
#from django.template import loader, get_template#no tan simplificado como el de abajo
from django.template.loader import get_template #---> MAS DIRECTO EL PROCESO
from django.shortcuts import render

class taco_special(object):
    def __init__(self, pastor, queso):
        
        self.pastor = pastor
        self.queso = queso

def menu(request): #aqui esta el ejemplo de una vista, incluyendo(parametros de python en html a travez de un contexto"
    """ya hemos minimizado la importacion de un template con el ((get_template)) 
                -importando >>get_template<< a travez de la funcion: >>loader<<,
                -con esto no ahorramos: importar el archivo html, luego leerlo, 
                  luego cerrarlo, y luego "renderizarlo" === juntar todo y mostrarlo
                -finalmente mostramos la pagina con el return, y los mostramos
                   juntando el file con el render"""

    ts = taco_special("pastor", "queso")
    
    menu_gringas = ["suadero", "pastor", "campechana", "tripa", "longamuerdes"]
    hoy = datetime.datetime.now()

    #doc_externo = open("C:/Users/dancr/Desktop/pag/pag/templates/vista1.html") #metodo para abrir la pagina


    #doc_externo=get_template('vista1.html') #metodo simplificado para abrir(ya indicando donde estan las plantillas en settings.)

    #plt = Template(doc_externo.read()) #leer el template

    #doc_externo.close() #poder cerrar el template
    

    #ctx = Context({"menu_gringas":menu_gringas}) #sincronizar el diccionario con la palntilla

    #muestramenu = doc_externo.render({"gringas":menu_gringas, "fecha":hoy, "ingrediente_1":ts.pastor, "ingrediente_2":ts.queso}) #metodo ya simplificado usando get_template


    ####return HttpResponse(muestramenu)
    return render(request, "vista1.html", {"gringas":menu_gringas, "fecha":hoy, "ingrediente_1":ts.pastor, "ingrediente_2":ts.queso})
    #El modulo """shurtucts""" funciona para mostar la vista html sin necesidad 
    #..de estar guardando los objetos del proceso para que se vea la vista en mas variables.
