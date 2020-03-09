import smtplib
import imghdr
import email.message
import os


def mailclient1():
    print("\n")
    print("SMTP-Mailclient1")
    print("\n")
    eingabe = input("Mailadresse: ")
    mail_adresse = eingabe
    eingabe = input("Mailpasswort: ")
    mail_passwort = eingabe
    eingabe = input("Mailbetreff: ")
    mail_betreff = eingabe
    eingabe = input("Mailnachricht: ")
    mail_nachricht = eingabe
    eingabe = input("Mailempfänger: ")
    mail_empfaenger = eingabe
    EMAIL_ADRESSE = mail_adresse
    EMAIL_PASSWORT = mail_passwort
    EMAIL_EMPFÄNGER = mail_empfaenger
    EMAIL_BETREFF = mail_betreff
    EMAIL_NACHRICHT = mail_nachricht
    KONTAKTE = [EMAIL_EMPFÄNGER]
    Nachricht = email.message.EmailMessage()
    Nachricht['Subject'] = EMAIL_BETREFF
    Nachricht['From'] = EMAIL_ADRESSE
    Nachricht['To'] = EMAIL_EMPFÄNGER
    Nachricht.set_content(EMAIL_NACHRICHT)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADRESSE, EMAIL_PASSWORT)
        smtp.send_message(Nachricht)
