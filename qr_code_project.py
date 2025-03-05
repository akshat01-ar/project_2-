import qrcode as qr
name = input("give  name of qr")
js = input("enter link Which QR has to be made")
img = qr.make(js)
img.save(f"QR_{name}.png")


    
