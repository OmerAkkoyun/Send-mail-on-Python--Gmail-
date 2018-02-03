import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

"""
SMTP Modülü ile mail gönderme

Ýlk olarak daha az güvenli uygulamalar için öncelikle aþaðýdaki linke gidiyoruz ve güvenliði
kaldýrýyoruz.

https://myaccount.google.com/lesssecureapps

"""

mesaj = MIMEMultipart()  # Mail yapýmýzý oluþturuyoruz.

mesaj["From"] = "mail gir "  # Kimden Göndereceðimiz

mesaj["To"] = "mail gir "  # Kime Göndereceðimiz

mesaj["Subject"] = "Smtp Mail Gönderme"  # Mailimizin Konusu

# Mailimizin Ýçeriði
yazi = """

Merhaba, Python ile mail gönderiyorum.    

Ömer Akkoyun


"""

mesaj_govdesi = MIMEText(yazi, "plain")  # Mailimizin gövdesini bu sýnýftan oluþturuyoruz.

mesaj.attach(mesaj_govdesi)  # Mailimizin gövdesini mail yapýmýza ekliyoruz.

try:
    mail = smtplib.SMTP("smtp.gmail.com", 587)  # SMTP objemizi oluþturuyoruz ve gmail smtp server'ýna baðlanýyoruz.

    mail.ehlo()  # SMTP serverýna kendimizi tanýtýyoruz.

    mail.starttls()  # Adresimizin ve Parolamýzýn þifrelenmesi için gerekli

    mail.login("mail gir @gmail.com",
               "*þifregirilcek")  # SMTP server'ýna giriþ yapýyoruz. Kendi mail adresimizi ve parolamýzý yapýyoruz.

    mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())  # Mailimizi gönderiyoruz.
    print("Mail baþarýyla gönderildi....")
    mail.close()  # Smtp serverýmýzýn baðlantýsýný koparýyoz.

except:
    sys.stderr.write(
        "Mail göndermesi baþarýsýz oldu...")  # Herhangi bir baðlanma sorunu veya mail gönderme sorunu olursa
    sys.stderr.flush()