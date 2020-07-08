
from qrcode import *
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class FileChooserWindow(Gtk.Window):

# 1º built a window with two buttons and one text box

    def __init__(self):
        Gtk.Window.__init__(self, title="GERADOR QR-CODE UNIVESP") # Built the window with name "Save the Image"

        grid = Gtk.Grid()
        self.add(grid)

        logo = Gtk.Image()
        logo.set_from_file('/home/mateus/PycharmProjects/Projeto Integrador/univesp_v1.jpeg')

        image_qrcode = Gtk.Image()

        label1 = Gtk.Label()
        label1.set_text(" \n PROJETO INTEGRADOR IV \n \n ENGENHARIA DA COMPUTAÇÃO \n \n POLO LIMIERA INTEGRANTES \n \n FELIPE ALLEONI TAMASI \n JOSE ASSIS DE OLIVEIRA \n MATEUS MODESTO \n PAULO CESAR DE SOUZA RODRIGUES \n SAMUEL RICARDO DOS SANTOS \n WELLINGTON FERNANDO SANTOS OLIVEIRA")
        label1.set_justify(Gtk.Justification.CENTER)

        button1 = Gtk.Button("LOGO") # This command built the button to choose the folder
        button1.connect("clicked", self.on_folder_clicked) # This command to built the procedure when the user clicked

        self.entry = Gtk.Entry() # This command built the text box
        self.entry.set_text("Insira a url ou texto aqui") # this command to set the box with a simple text
        # f_name = self.entry.get_text()

        # This commands are same the button 1
        button2 = Gtk.Button("SALVAR")
        button2.connect("clicked", self.save)

        # This commands are same the button 1
        button3 = Gtk.Button("GERAR")
        button3.connect("clicked", self.gerar)

        # This command include check button
        checkbutton = Gtk.CheckButton("QR-Code com logo")
        checkbutton.connect("toggled", self.toggled_cb)

        # This command organize layout
        grid.add(logo)
        grid.attach(logo, 0, 0, 1, 15)
        grid.attach(image_qrcode, 2, 2, 6, 6)
        grid.attach(label1, 0, 15, 1, 2)
        grid.attach(self.entry, 2, 9, 4, 1)
        grid.attach(checkbutton, 2, 12, 3, 1)
        grid.attach(button1, 2, 14, 1, 1)
        grid.attach(button2, 7, 14, 1, 1)
        grid.attach(button3, 7, 9, 1, 1)

    # callback function
    def toggled_cb(self, button):
        # if the togglebutton is active, set the title of the window
        # as "Checkbutton Example"
        if button.get_active():
            state = "on"
            # self.set_title("CheckButton Example")
        # else, set it as "" (empty string)
        else:
            # self.set_title("")
            state = "off"

    # This procedure to take a file name
    def save(self, *widget):
        file_name = 'UNIVESP_QR_Code'
        save_path = str(self.on_folder_clicked())
        url = self.entry.get_text()

        if self.checkbutton.Active:
            state = "on"
            logo_path = str(self.button1)
            size, img = qrcode.qrcode_logo(url, file_name, logo_path)
            qrcode.save(img, size, save_path, file_name)

        else:
            state = "off"
            size, img = qrcode.qrcode(url, file_name)
            qrcode.save(img, size, save_path, file_name)
        self.destroy()

    def gerar(self, checkbutton):

       file_name = 'UNIVESP_QR_Code'
       url = self.entry.get_text()

       if str(checkbutton.get_active()) == True:

          logo_path = str(self.button1)
          size, img = qrcode.qrcode_logo(url, file_name, logo_path)
          qrcode.show(img)

       else:

           size, img = qrcode.qrcode(url, file_name)
           qrcode.show(img)



    # This procedure to take a file name
    def confirm_the_file_name(self, *widget):
        self.file_name = self.entry.get_text()
        self.destroy()

    # This procedure to take a folder path

    def on_folder_clicked(self, *widget):
        dialog = Gtk.FileChooserDialog("Please choose a folder", self,
            Gtk.FileChooserAction.SELECT_FOLDER,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             "Select", Gtk.ResponseType.OK))
        dialog.set_default_size(800, 400)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Select clicked")
            print("Folder selected: " + dialog.get_filename())
            self.folder = dialog.get_filename()
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()

# Finish the procedure

win = FileChooserWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()




