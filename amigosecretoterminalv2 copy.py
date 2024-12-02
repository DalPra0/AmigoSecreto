import random
import smtplib
from email.mime.text import MIMEText

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "SEU_EMAIL"
EMAIL_PASSWORD = "SUA_SENHA_DE_APLICATIVO" 

def solicitar_dados_participantes():
    participantes = []
    try:
        num_participantes = int(input("Digite o número de participantes: "))
        if num_participantes < 2:
            raise ValueError("O número mínimo de participantes é 2.")
    except ValueError as e:
        print(f"Erro: {e}")
        return solicitar_dados_participantes()

    for i in range(num_participantes):
        print(f"\nParticipante {i + 1}:")
        email = input("Digite o e-mail: ").strip()
        nome = input("Digite o nome: ").strip()
        participantes.append((email, nome))

    return participantes

def gerar_sorteio(participantes):
    nomes = [p[1] for p in participantes]
    sorteio = {}

    while len(sorteio) < len(nomes):
        restantes = [n for n in nomes if n not in sorteio.values()]
        random.shuffle(restantes)

        for nome in nomes:
            if nome in sorteio:
                continue
            candidato = restantes.pop()
            if nome != candidato and sorteio.get(candidato) != nome:
                sorteio[nome] = candidato
            else:
                return gerar_sorteio(participantes)
    
    return sorteio

def enviar_emails(sorteio, participantes):
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        for email, nome in participantes:
            amigo_secreto = sorteio[nome]
            mensagem = MIMEText(f"Olá, {nome}!\nSeu amigo secreto é: {amigo_secreto}.")
            mensagem["Subject"] = "Amigo Secreto"
            mensagem["From"] = EMAIL_ADDRESS
            mensagem["To"] = email

            try:
                server.sendmail(EMAIL_ADDRESS, email, mensagem.as_string())
                print(f"E-mail enviado com sucesso para {nome} ({email})!")
            except Exception as e:
                print(f"Erro ao enviar e-mail para {nome} ({email}): {e}")

def main():
    print("Bem-vindo ao sorteio de Amigo Secreto!\n")
    participantes = solicitar_dados_participantes()
    sorteio = gerar_sorteio(participantes)
    enviar_emails(sorteio, participantes)
    print("\nSorteio realizado e e-mails enviados com sucesso!")

if __name__ == "__main__":
    main()
