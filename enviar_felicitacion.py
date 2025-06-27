import csv
import smtplib
import ssl
from email.mime.text import MIMEText
from datetime import datetime

def enviar_correo(destinatario, asunto, html):
    remitente = "mariodejesusmontesinos06@gmail.com"
    contraseña = "1234"  

    mensaje = MIMEText(html, "html")
    mensaje["Subject"] = asunto
    mensaje["From"] = remitente
    mensaje["To"] = destinatario

    contexto = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=contexto) as servidor:
        servidor.login(remitente, contraseña)
        servidor.sendmail(remitente, destinatario, mensaje.as_string())

def obtener_html(nombre):
    with open("tarjeta.html", "r", encoding="utf-8") as file:
        contenido = file.read()
    return contenido.replace("{{nombre}}", nombre)

def main():
    hoy = datetime.now().strftime("%m-%d")  # Solo mes y día
    with open("cumple.csv", newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            fecha = datetime.strptime(fila["fecha"], "%Y-%m-%d").strftime("%m-%d")
            if fecha == hoy:
                html = obtener_html(fila["nombre"])
                enviar_correo(fila["email"], "¡Feliz cumpleaños!", html)

if __name__ == "__main__":
    main()
