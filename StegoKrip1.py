# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 17:09:00 2019

@author: Abdullah Hamzah
"""

from bit_manipulation import lsb_interleave_list, lsb_deinterleave_list
from bit_manipulation import roundup
import base64
import hashlib
import os
from PIL import Image
import sys
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
from Cryptodome import Random
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from StegoKrip import Ui_StegoKrip
from AboutGuide import Ui_AboutGuide

class CryptoAES(object):
    
    def __init__(self,key):
        self.block_size = 32
        
        self.key = hashlib.sha256(key.encode()).digest()
    
    def enkrip (self, output_filename,data):
        
        iv = Random.new().read(AES.block_size)
        encryption_suite = AES.new(self.key, AES.MODE_CBC, iv)
        
        if isinstance (data,str):
            data = data.encode()
            
        secret = encryption_suite.encrypt(iv + pad(data, self.block_size))

        secret = base64.b64encode(secret).decode()
        
        with open(output_filename, "w") as text_file:
        
            text_file.write(secret)
            
    def dekrip (self, cypher_data):
        if not cypher_data:
            return None
        if isinstance(cypher_data, str):
            cypher_data = cypher_data.encode()
        cypher_data = base64.b64decode(cypher_data)
        
        iv = cypher_data[:AES.block_size]
        
        cypher_data = cypher_data[AES.block_size:]
        
        try:
            decryption_suite = AES.new(self.key, AES.MODE_CBC, iv)
            decrypted_data = unpad(decryption_suite.decrypt(cypher_data), self.block_size)
            try:
                return decrypted_data.decode('utf-8')
            except UnicodeDecodeError:
                return decrypted_data
        except ValueError:
            return None

def prepare_hide(input_image_path, input_file_path):
    image = Image.open(input_image_path)
    input_file = open(input_file_path,"rb")
    return image, input_file
"""Use Library Image from PIL"""

def prepare_recover(steg_image_path, output_file_path):
    steg_image = Image.open(steg_image_path)
    output_file = open(output_file_path, "wb+")
    return steg_image, output_file
"""Use Library Image from PIL"""

def get_filesize (path):
    return os.stat(path).st_size 
"""Use Library os"""

def max_bits_to_hide(image, num_lsb):
    return int(3 * image.size [0] * image.size [1] * num_lsb)
"""Menghitung bit yang akan disembunyikan ke file image"""

def bytes_in_max_file_size(image, num_lsb):
    return roundup(max_bits_to_hide(image, num_lsb).bit_length() / 8)
"""Use fungsi roundup di file bit_manipulation"""

def hide_data(input_image_path, input_file_path, steg_image_path, num_lsb, compression_level,output_hash):

    image, input_file = prepare_hide(input_image_path, input_file_path)
    num_channels = len(image.getdata()[0])
    flattened_color_data = [v for t in image.getdata() for v in t]
    
    file_size = get_filesize (input_file_path)
    file_size_tag = file_size.to_bytes(bytes_in_max_file_size(image, num_lsb),byteorder=sys.byteorder)
    """Use Library sys"""
    
    data = file_size_tag + input_file.read()
          
    flattened_color_data = lsb_interleave_list(flattened_color_data, data, num_lsb)
    """Use function lsb_interleave_list from file bit_manipulation"""
    
    image.putdata(list(zip(*[iter(flattened_color_data)]*num_channels)))
    image.save(steg_image_path, compress_level=compression_level)
    """Use Library Image"""
    sha256(steg_image_path,output_hash)
    
def recover_data(steg_image_path, output_file_path, num_lsb):

    steg_image, output_file = prepare_recover(steg_image_path, output_file_path)
    color_data = [v for t in steg_image.getdata() for v in t]
    
    file_size_tag_size = bytes_in_max_file_size(steg_image, num_lsb)
    tag_bit_height = roundup(8 * file_size_tag_size / num_lsb)
    
    bytes_to_recover = int.from_bytes(lsb_deinterleave_list(color_data[:tag_bit_height], 8* file_size_tag_size, 
                                                            num_lsb),byteorder=sys.byteorder)

    data = lsb_deinterleave_list(color_data[tag_bit_height:], 8 * bytes_to_recover, num_lsb)

    output_file.write(data)
    output_file.close()
    
    
def sha256(filename, output_path):
    sha256_hash = hashlib.sha256()
    with open(filename,"rb") as f:

        for byte_block in iter(lambda: f.read(4096),b""):
            sha256_hash.update(byte_block)
        hash_output = sha256_hash.hexdigest()
        with open(output_path, "w") as text_file:
            text_file.write(hash_output)

def sha256cek(filename):
    sha256_hash = hashlib.sha256()
    with open(filename,"rb") as f:

        for byte_block in iter(lambda: f.read(4096),b""):
            sha256_hash.update(byte_block)
        hash_output = sha256_hash.hexdigest()
        return hash_output
    
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        
        super (mywindow,self).__init__()
        self.ui = Ui_StegoKrip()
        self.ui.setupUi(self) 
        
        #TextBox
        #hide
        self.ui.TxtBrowseHide.setText("")
        self.ui.TxtBrowseImage.setText("")
        self.ui.BtnBrowseHide.clicked.connect(self.openFileNameDialogHide)
        self.ui.BtnBrowseCI.clicked.connect(self.openFileNameDialogCover)
        
        #recover
        self.ui.TxtBrowseRecover.setText("")
        self.ui.TxtCodeHash.setText("")
        self.ui.BtnBrowseRecover.clicked.connect(self.openFileNameDialogRecover)
        
        #enkrip
        self.ui.TxtBrowseEn.setText("")
        self.ui.TxtPassEn.setText("")
        self.ui.BtnBrowseEn.clicked.connect(self.openFileNameDialogEn)
        
        #dekrip
        self.ui.TxtBrowseDe.setText("")
        self.ui.TxtPassDe.setText("")
        self.ui.BtnBrowseDe.clicked.connect(self.openFileNameDialogDe)
        
        
        #Button Action
        self.ui.BtnHide.clicked.connect(self.onclickhide)
        self.ui.BtnEnkrip.clicked.connect(self.onclickenkrip)
        self.ui.BtnDekrip.clicked.connect(self.onclickdekrip)
        self.ui.BtnRecover.clicked.connect(self.onclickrecover)
        
        #Menu
        self.ui.actionAbout_Guide.triggered.connect(self.AboutGuide)
        self.ui.actionQuit.triggered.connect(app.quit)
               
    def openFileNameDialogEn(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Open File can be Encrypt", "","Text Files (*.txt);;All Files (*)", options=options)
        input_br = fileName
        self.ui.TxtBrowseEn.setText(input_br)
        
    def openFileNameDialogDe(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Open File can be Decrypt", "","Text Files (*.txt);;All Files (*)", options=options)
        input_br = fileName
        self.ui.TxtBrowseDe.setText(input_br)
        
    def openFileNameDialogHide(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Open File can be Hide", "","Text Files (*.txt);;All Files (*)", options=options)
        input_br = fileName
        self.ui.TxtBrowseHide.setText(input_br)
        
    def openFileNameDialogCover(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Open File Cover Image", "","PNG (*.png);;BMP (*.bmp);;JPG (*.jpg);;JPEG (*.jpeg);;All Files (*)", options=options)
        input_br = fileName
        self.ui.TxtBrowseImage.setText(input_br)
        
    def openFileNameDialogRecover(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Open File can be Recover", "","PNG (*.png);;All Files (*)", options=options)
        input_br = fileName
        self.ui.TxtBrowseRecover.setText(input_br)
    
    def saveFileDialogEn(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"Save File Encryption","","Text Files (*.txt);;All Files (*)", options=options)
        save_en = fileName
        return save_en
    
    def saveFileDialogDe(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"Save File Decryption","","Text Files (*.txt);;All Files (*)", options=options)
        save_en = fileName
        return save_en
    
    def saveFileDialogHide(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"Save File Stego Image","","PNG (*.png);;All Files (*)", options=options)
        save_en = fileName
        return save_en
    
    def saveFileDialogHash(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"Save File Hash Code","","Text Files (*.txt);;All Files (*)", options=options)
        save_hash = fileName
        return save_hash
    
    def saveFileDialogRecover(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"Save File Recover","","Text Files (*.txt);;All Files (*)", options=options)
        save_en = fileName
        return save_en
    
           
    def AboutGuide(self):
        self.window = QtWidgets.QMainWindow()
        self.ai = Ui_AboutGuide()
        self.ai.setupUi(self.window)
        self.window.show()
        self.ai.actionQuit.triggered.connect(app.quit)
        self.ai.actionMain_Menu.triggered.connect(self.rollbackMain)
    
    
    def rollbackMain(self):
        self.window.hide()
        
        
    def onclickhide(self):
        image_hp = self.ui.TxtBrowseImage.text()
        input_hp = self.ui.TxtBrowseHide.text()
        output_hp = self.saveFileDialogHide()
        output_hash = self.saveFileDialogHash()
        num_bits_hp = 4
        compression = 1
        
        if input_hp == '':
            QMessageBox.critical(self, "Failed Hide",'Input File can\'t be empty' )
        elif image_hp == '':
            QMessageBox.critical(self, "Failed Hide",'Cover Image can\'t be empty' )
        elif output_hp == '':
            QMessageBox.critical(self, "Failed Hide",'Output File Stego can\'t be empty' )
        elif output_hash == '':
            QMessageBox.critical(self, "Failed Hide",'Output File Hash can\'t be empty' )
        else:
            image, input_file = prepare_hide(image_hp, input_hp)
            
            file_size = get_filesize (input_hp)
            file_size_tag = file_size.to_bytes(bytes_in_max_file_size(image, num_bits_hp),byteorder=sys.byteorder)
            
            data = file_size_tag + input_file.read()
                
            output_hp = output_hp
            if not output_hp:
                output_hp = 'OutputHide.png'
            else:
                if output_hp[-4:].lower() != '.png':
                    output_hp += '.png'
                        
            output_hash = output_hash
            if not output_hash:
                output_hash = 'OutputHash.txt'
            else:
                if output_hash[-4:].lower() != '.txt':
                    output_hash += '.txt'
                        
            if 8 * len(data) > max_bits_to_hide(image, num_bits_hp):
                QMessageBox.critical(self,"Failed Hide",'PROCESS FAIL! Lower Image Capacity')
            else:
                hide_data(image_hp, input_hp, output_hp, num_bits_hp, compression, output_hash)
                QMessageBox.about(self, "Hidden Image Stego",'%s Saved File Success' % output_hp )
            
               
    def onclickrecover(self):
        image_rp = self.ui.TxtBrowseRecover.text()
        output_rp = self.saveFileDialogRecover()
        output_code = self.ui.TxtCodeHash.text()
        num_bits_rp = 4
        hashcode = sha256cek(image_rp)
        
        if image_rp == '':
            QMessageBox.critical(self, "Failed Recovery",'Image Stego can\'t be empty' )
        elif output_rp == '':
            QMessageBox.critical(self, "Failed Recovery",'Output File Name can\'t be empty' )
        elif output_code == '':
            QMessageBox.critical(self, "Failed Recovery",'Code Hash can\'t be empty' )
        else:
            if output_code != hashcode:
                QMessageBox.warning(self, "Failed Recovery",'Hash code does not match, file has been changed' )
            else:
                output_rp = output_rp
                if not output_rp:
                    output_rp = 'OutputRecover.txt'
                else:
                    if output_rp[-4:].lower() != '.txt':
                        output_rp += '.txt'
                        
                recover_data(image_rp, output_rp, num_bits_rp)
                QMessageBox.about(self, "Recovery Image Stego",'%s Saved File Success' % output_rp )
        
        
    def onclickenkrip(self):
        message_file = self.ui.TxtBrowseEn.text()
        password_en = self.ui.TxtPassEn.text()
        output_file = self.saveFileDialogEn() 
        
        if message_file == '':
            QMessageBox.critical(self, "Failed Encryption",'File can\'t be empty' )
        elif password_en == '':
            QMessageBox.critical(self, "Failed Encryption",'Password can\'t be empty' )
        elif output_file == '':
            QMessageBox.critical(self, "Failed Encryption",'Output File Name can\'t be empty' )
        else:
            if message_file:
                try:
                    with open(message_file, "r", encoding='utf-8') as f:
                        message = f.read()
                except Exception :
                    try:
                        with open(message_file, "rb") as f:
                            message = f.read()
                    except Exception :
                        QMessageBox.critical(self, "Failed Encryption",'Error while reading input')

            crypto = None

            crypto = CryptoAES(password_en)
            
            output_file = output_file
            if not output_file:
                output_file = 'OutputCipher.txt'
            else:
                if output_file[-4:].lower() != '.txt':
                    output_file += '.txt'
                    
            crypto.enkrip(output_file, message)
            QMessageBox.about(self, "Enkripsi",'%s Saved File Success' % output_file )
        
        
    def onclickdekrip(self):
        
        input_file = self.ui.TxtBrowseDe.text()
        output_file = self.saveFileDialogDe()
        password_de = self.ui.TxtPassDe.text()
        
        if input_file == '':
            QMessageBox.critical(self, "Failed Decryption",'File can\'t be empty' )
        elif password_de == '':
            QMessageBox.critical(self, "Failed Decryption",'Password can\'t be empty' )
        elif output_file == '':
            QMessageBox.critical(self, "Failed Decryption",'Output File Name can\'t be empty' )
        else:
            crypto = CryptoAES(password_de)
            with open(input_file, 'r') as infile:
                cypher_data = infile.read()
            secret = crypto.dekrip(cypher_data)
        
            output_file = output_file
            if not output_file:
                output_file = 'OutputPlainText.txt'
            else:
                if output_file[-4:].lower() != '.txt':
                    output_file += '.txt'
                    
            if output_file:
                try:
                    with open(output_file, 'wb')as f:
                        f.write(secret)
                except TypeError:
                    try:
                        with open(output_file, 'wb')as f:
                            f.write(secret.encode())
                    except Exception :
                        QMessageBox.critical(self,"Failed Decrypt",'Wrong Password!')
                        
                QMessageBox.about(self, "Dekripsi",'%s Saved File Success' % output_file )
        
if __name__ == "__main__":
    
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()
    sys.exit(app.exec())