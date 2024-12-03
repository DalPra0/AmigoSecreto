import customtkinter as ctk
import random
import smtplib
from email.mime.text import MIMEText

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "SEU_EMAIL"
EMAIL_PASSWORD = "SUA_SENHA_DE_APLICATIVO"

class AmigoSecretoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Amigo Secreto")
        self.participants = []

        self.frame_inicio = ctk.CTkFrame(root)
        self.frame_inicio.pack(pady=20, padx=20)

        self.label_num_participants = ctk.CTkLabel(self.frame_inicio, text="Número de Participantes:")
        self.label_num_participants.pack()

        self.entry_num_participants = ctk.CTkEntry(self.frame_inicio)
        self.entry_num_participants.pack(pady=10)

        self.button_avancar = ctk.CTkButton(self.frame_inicio, text="Avançar", command=self.criar_tela_participantes)
        self.button_avancar.pack()

    def criar_tela_participantes(self):
        try:
            self.num_participants = int(self.entry_num_participants.get())
            if self.num_participants < 2:
                raise ValueError("O número mínimo de participantes é 2.")
        except ValueError as e:
            ctk.CTkMessageBox.show_error(title="Erro", message=str(e))
            return

        self.frame_inicio.pack_forget()
        self.frame_participantes = ctk.CTkFrame(self.root)
        self.frame_participantes.pack(pady=20, padx=20)

        self.entries_email = []
        self.entries_nome = []

        for i in range(self.num_participants):
            label = ctk.CTkLabel(self.frame_participantes, text=f"Participante {i + 1}:")
            label.grid(row=i, column=0, padx=5, pady=5)

            entry_email = ctk.CTkEntry(self.frame_participantes, placeholder_text="E-mail")
            entry_email.grid(row=i, column=1, padx=5, pady=5)
            
            entry_nome = ctk.CTkEntry(self.frame_participantes, placeholder_text="Nome")
            entry_nome.grid(row=i, column=2, padx=5, pady=5)

            self.entries_email.append(entry_email)
            self.entries_nome.append(entry_nome)

        self.button_sortear = ctk.CTkButton(self.frame_participantes, text="Sortear e Enviar", command=self.sortear)
        self.button_sortear.grid(row=self.num_participants, columnspan=3, pady=10)

    def sortear(self):
        emails = [entry.get() for entry in self.entries_email]
        nomes = [entry.get() for entry in self.entries_nome]

        if "" in emails or "" in nomes:
            ctk.CTkMessageBox.show_error(title="Erro", message="Todos os campos devem estar preenchidos.")
            return

        participantes = list(zip(emails, nomes))

        try:
            sorteio = self.gerar_sorteio(participantes)
        except Exception as e:
            ctk.CTkMessageBox.show_error(title="Erro", message=f"Erro no sorteio: {e}")
            return

        try:
            self.enviar_emails(sorteio, participantes)
            ctk.CTkMessageBox.show_info(title="Sucesso", message="Sorteio realizado e e-mails enviados!")
        except Exception as e:
            ctk.CTkMessageBox.show_error(title="Erro", message=f"Erro ao enviar e-mails: {e}")

    def gerar_sorteio(self, participantes):
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
                    return self.gerar_sorteio(participantes)
        
        return sorteio

    def enviar_emails(self, sorteio, participantes):
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

            for email, nome in participantes:
                amigo_secreto = sorteio[nome]
                mensagem = MIMEText(f"Olá, {nome}!\nSeu amigo secreto é: {amigo_secreto}.")
                mensagem["Subject"] = "Amigo Secreto"
                mensagem["From"] = EMAIL_ADDRESS
                mensagem["To"] = email

                server.sendmail(EMAIL_ADDRESS, email, mensagem.as_string())

if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")
    root = ctk.CTk()
    app = AmigoSecretoApp(root)
    root.mainloop()
