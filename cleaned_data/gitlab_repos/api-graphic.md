# Repository Information
Name: api-graphic

# Files

File: config
================================================
[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
	symlinks = false
	ignorecase = true
[remote "origin"]
	url = https://gitlab.com/edopore1/api-graphic.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: api.py
================================================
import routeros_api
import getpass
import pandas as pd
def connect(host, username, password):
    connection = routeros_api.RouterOsApiPool(host, username=username, password=password, port=8740, plaintext_login=True)
    api = connection.get_api()
    print('Conexión Establecida')
    return api, connection
def disconnect(connection):
    print("Desconexión Exitosa")
    return connection.disconnect()
def obtenerqueue(api):
    list_queues = api.get_resource('/queue/simple')
    lista = list_queues.get()
    queue = []
    for i in lista:
        queue.append(i)
    return lista
def obtenerarp(api, interface=''):
    list_queues = api.get_resource('/ip/arp')
    if interface == '':
        lista = list_queues.get()
    else:
        lista = list_queues.get(interface=interface)
    arp = []
    for i in lista:
        arp.append(i)
    return arp
def desactivarfile(file, app):
    file = pd.read_excel(file)
    ip = ip2str(file['DIRECCION IP'])
    print(len(ip))
    list_address = app.get_resource('/ip/arp')  # Obtiene Datos de la tabla ARP
    for dire in ip:
        _id = list_address.get(address=dire)[0]['id']
        print('ip address: ', list_address.get(address=dire)[0]['address'], 'id: ', _id)
        list_address.set(id=_id, address=dire, disabled='true')
    return
def activarfile(file, app):
    file = pd.read_excel(file)
    ip = ip2str(file['DIRECCION IP'])
    print(len(ip))
    list_address = app.get_resource('/ip/arp')  # Obtiene Datos de la tabla ARP
    for dire in ip:
        _id = list_address.get(address=dire)[0]['id']
        print('ip address:', dire, ' id:', _id)
        list_address.set(id=_id, address=dire, disabled='false')
    return
def activar(app):
    list_address = app.get_resource('/ip/arp')  # Obtiene Datos de la tabla ARP
    while True:
        address = input("Dirección IP Usuario: ")
        if address:
            _id = list_address.get(address=address)[0]['id']
            print(list_address.get(address=address))
            # list_address.set(id=_id, address=address, disabled='true')
        else:
            break
    return
def desactivar(app):
    list_address = app.get_resource('/ip/arp')  # Obtiene Datos de la tabla ARP
    while True:
        address = input("Dirección IP Usuario: ")
        if address:
            _id = list_address.get(address=address)[0]['id']
            print(list_address.get(address=address))
            # list_address.set(id=_id, address=address, disabled='true')
        else:
            break
    return
def ip2str(x_val):
    ipstr = []
    for i in x_val:
        aux = str(i)
        ipstr.append(aux)
    return ipstr
================================================

File: funciones.py
================================================
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
from api import *
def inicio():
    raiz = Tk()
    raiz.title("API MikroTik")
    raiz.iconbitmap("media/MikroTik.ico")
    raiz.resizable(False, False)
    frameimagen = Frame(raiz)
    frameimagen.grid(row=0)
    host = StringVar()
    username = StringVar()
    password = StringVar()
    imagen = PhotoImage(file="media/logoIsanet.gif")
    Label(frameimagen, image=imagen).pack()
    miframe = Frame(raiz, width=650, height=350)
    miframe.grid(row=1, pady=5)
    Label(miframe, text="Host: ").grid(column=0, row=1, padx=5, pady=5, sticky='e')
    host = Entry(miframe, textvariable=host)
    host.grid(column=1, row=1, padx=5, pady=5)
    lusername = Label(miframe, text="Username: ")
    lusername.grid(column=0, row=2, padx=5, pady=5, sticky='e')
    username = Entry(miframe, textvariable=username)
    username.grid(column=1, row=2, padx=5, pady=5)
    lpassword = Label(miframe, text="Password: ")
    lpassword.grid(column=0, row=3, padx=5, pady=5, sticky='e')
    password = Entry(miframe, textvariable=password, show='x')
    password.grid(column=1, row=3, padx=5, pady=5)
    botonconectar = Button(miframe, text="Conectar", command=lambda: getdata(host, username, password, raiz))
    botonconectar.grid(column=0, row=4, padx=5, pady=5)
    botonsalir = Button(miframe, text="Salir", command=lambda: salir(raiz))
    botonsalir.grid(column=1, row=4, padx=5, pady=5)
    raiz.mainloop()
def archivo():
    ventana = Tk()
    ventana.withdraw()
    ventana.filename = filedialog.askopenfilename(initialdir="/Documents", title="Select file", filetypes=(("excel files", "*.xlsx"), ("all files", "*.*")))
    print(ventana.filename)
    return ventana.filename
def disconect(conect,window):
    disconnect(conect)
    window.destroy()
    inicio()
def salir(window):
    cerrar = messagebox.askyesno(title="Salir", message="¿Está seguro que desea salir?")
    if cerrar:
        window.destroy()
def getdata(host, username, password, window):
    host = host.get()
    username = username.get()
    password = password.get()
    if not (host and username and password):
        messagebox.showerror(title="Error", message='¡¡Ingrese los datos!!')
    else:
        app, conect = connect(host, username, password)
        window.destroy()
        MainWindow(app, conect)
def MainWindow(app, conect):
    MainMenu = Tk()
    MainMenu.geometry("500x500")
    blogout = Button(MainMenu,text="Cerrar Sesión",command=lambda: disconect(conect, MainMenu))
    blogout.grid()
================================================

File: prueba.py
================================================
from funciones import *
inicio()
================================================

File: README.md
================================================
# apigraphic