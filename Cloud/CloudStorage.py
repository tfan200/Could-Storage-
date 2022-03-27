import dropbox

class TransferData: 
    def __init___(self, access_token): 
        self.access_token = access_token
    def UploadFiles(self,filefrom,fileto):
        dbx = dropbox.Dropbox(self.access_token)
        fk = open(filefrom, 'rb')
        dbx.files_upload(fk.read(),fileto)

def main():
    access_token = "sl.BEHBVLE5P18Hq49Pxd1pdDWeR2p7YSCsWio4hYUDkir2as4ljMjc2sx3ctAeQyV3L1QGcEFtnzQAyA4bjR5sYd_-wgPEEy7JrgMlBa_1OPoiL8VUMJ6bU9eK5d95dUkzCUiRDAA"
    transferData = TransferData(access_token)

    filefrom = input("Enter the file path you.... leave it. Just enter the file path")
    fileto = input("enter the full path you noob")
    transferData.UploadFiles(filefrom,fileto)

    print("Ey fuckwit.. File has been moved")
main() 
