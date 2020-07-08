# Gerador de código qrcode

import pyqrcode
from PIL import Image

class qrcode:

    def qrcode_logo(url, file_name, logo_path):

        # Generate the qr code and save as png
        qrobj = pyqrcode.create(str(url))
        with open(str(file_name), 'wb') as f:
            qrobj.png(f, scale=10)

        # Now open that png image to put the logo
        img = Image.open(str(file_name))
        img = img.convert("RGBA")
        width, height = img.size
        size = width, height

        # How big the logo we want to put in the qr code png
        logo_size = 100

        # Open the logo image
        logo = Image.open(logo_path)

        # Calculate xmin, ymin, xmax, ymax to put the logo
        xmin = ymin = int((width / 2) - (logo_size / 2))
        xmax = ymax = int((width / 2) + (logo_size / 2))

        # resize the logo as calculated
        logo = logo.resize((xmax - xmin, ymax - ymin))

        # put the logo in the qr code
        img.paste(logo, (xmin, ymin, xmax, ymax))

        return size, img

    def qrcode(url, file_name):

        # Generate the qr code and save as png
        qrobj = pyqrcode.create(str(url))
        with open(str(file_name), 'wb') as f:
            qrobj.png(f, scale=10)

        # Now open that png image to put the logo
        img = Image.open(str(file_name))
        img = img.convert("RGBA")
        width, height = img.size
        size = width, height

        return size, img

    # show image
    def show(self):
        self.show()

    # save the qr-code with logo
    def save(self, size, save_path, file_name):
        self.thumbnail(size)
        file = str(save_path + '/' + str(file_name))
        self.save(file, "png")
        # self.save(file + ".thumbnail", "png")



# teste

# url = 'https://sites.google.com/view/clubetodabella/home'
# file_name = 'teste_sem_logo'
# logo_path = '/home/mateus/PycharmProjects/Projeto Integrador/facebook.png'
# save_path = '/home/mateus/PycharmProjects/Projeto Integrador/Old'
#
# size, img = qrcode.qrcode(url, file_name)
#
# qrcode.show(img)
#
# qrcode.save(img, size, save_path, file_name)