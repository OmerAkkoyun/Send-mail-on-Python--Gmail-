import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

"""
SMTP Mod�l� ile mail g�nderme

�lk olarak daha az g�venli uygulamalar i�in �ncelikle a�a��daki linke gidiyoruz ve g�venli�i
kald�r�yoruz.

https://myaccount.google.com/lesssecureapps

"""

mesaj = MIMEMultipart()  # Mail yap�m�z� olu�turuyoruz.

mesaj["From"] = "mail gir "  # Kimden G�nderece�imiz

mesaj["To"] = "mail gir "  # Kime G�nderece�imiz

mesaj["Subject"] = "Smtp Mail G�nderme"  # Mailimizin Konusu

# Mailimizin ��eri�i
yazi = """

Merhaba, Python ile mail g�nderiyorum.    

�mer Akkoyun


"""

mesaj_govdesi = MIMEText(yazi, "plain")  # Mailimizin g�vdesini bu s�n�ftan olu�turuyoruz.

mesaj.attach(mesaj_govdesi)  # Mailimizin g�vdesini mail yap�m�za ekliyoruz.

try:
    mail = smtplib.SMTP("smtp.gmail.com", 587)  # SMTP objemizi olu�turuyoruz ve gmail smtp server'�na ba�lan�yoruz.

    mail.ehlo()  # SMTP server�na kendimizi tan�t�yoruz.

    mail.starttls()  # Adresimizin ve Parolam�z�n �ifrelenmesi i�in gerekli

    mail.login("mail gir @gmail.com",
               "*�ifregirilcek")  # SMTP server'�na giri� yap�yoruz. Kendi mail adresimizi ve parolam�z� yap�yoruz.

    mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())  # Mailimizi g�nderiyoruz.
    print("Mail ba�ar�yla g�nderildi....")
    mail.close()  # Smtp server�m�z�n ba�lant�s�n� kopar�yoz.

except:
    sys.stderr.write(
        "Mail g�ndermesi ba�ar�s�z oldu...")  # Herhangi bir ba�lanma sorunu veya mail g�nderme sorunu olursa
    sys.stderr.flush()