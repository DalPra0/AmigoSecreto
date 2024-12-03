# Amigo Secreto

Este repositório contém dois programas para realizar sorteios de **Amigo Secreto**, com envio automático de e-mails para os participantes. Você pode escolher entre uma versão com interface gráfica utilizando a biblioteca `customtkinter` ou uma versão simples baseada no terminal.

---

## 🛠️ Pré-requisitos
```markdown
1. **Python 3.x** instalado no sistema.
2. Instale as bibliotecas necessárias:
   ```bash
   pip install customtkinter
   ```
3. Configure o acesso ao seu e-mail:
   - Utilize um e-mail do Gmail.
   - Habilite **Senhas de Aplicativo** no Gmail e utilize-a como `EMAIL_PASSWORD`.

---

## 🔍 Explicação dos Códigos

### `amigoSecretoComTelaV2.py`

Este programa utiliza uma **interface gráfica** para gerenciar o sorteio de Amigo Secreto. Os participantes informam seus nomes e e-mails, e o programa realiza o sorteio, enviando automaticamente um e-mail para cada participante com o nome de seu amigo secreto.

**Funcionalidades principais**:
- Entrada gráfica para participantes.
- Sorteio automático de pares garantindo que ninguém tire a si mesmo.
- Envio de e-mails com os resultados do sorteio.

---

### `amigosecretoterminalv2 copy.py`

Este é um programa mais simples baseado no **terminal**. Ele solicita que os usuários insiram manualmente o número de participantes, seus nomes e e-mails. Após o sorteio, os e-mails são enviados para os participantes.

**Funcionalidades principais**:
- Interface por linha de comando (CLI).
- Sorteio automático.
- Envio de e-mails para os participantes.

---

## 📄 Como Usar

### Versão com Interface Gráfica (`amigoSecretoComTelaV2.py`)

1. Execute o arquivo:
   ```bash
   python amigoSecretoComTelaV2.py
   ```
2. Insira o número de participantes e clique em **Avançar**.
3. Preencha os campos de **nome** e **e-mail** para cada participante.
4. Clique em **Sortear e Enviar**:
   - O sorteio será realizado.
   - Os e-mails serão enviados automaticamente.
5. Pronto! Os participantes receberão suas respectivas notificações.

---

### Versão Terminal (`amigosecretoterminalv2 copy.py`)

1. Execute o arquivo:
   ```bash
   python amigosecretoterminalv2\ copy.py
   ```
2. Siga as instruções no terminal:
   - Insira o número de participantes.
   - Insira o nome e e-mail de cada participante.
3. Após preencher os dados, o sorteio será realizado.
4. Os e-mails serão enviados automaticamente.
5. Verifique no terminal os logs de envio.

---

## 💡 Observações Importantes

1. Certifique-se de configurar as credenciais de e-mail no início de ambos os arquivos:
   ```python
   EMAIL_ADDRESS = "seuemail@gmail.com"
   EMAIL_PASSWORD = "suasenhadeaplicativo"
   ```
2. O Gmail pode exigir configurações adicionais para aceitar conexões externas. Habilite **Senhas de Aplicativo** em [Configurações do Gmail](https://support.google.com/accounts/answer/185833?hl=pt-BR).

3. Para ambientes que não aceitam `customtkinter` (ex.: algumas distribuições Linux), use a versão do terminal.

---

## 🔗 Recursos Utilizados

- **Python**: Linguagem principal.
- **CustomTkinter**: Biblioteca para interface gráfica.
- **Smtplib**: Envio de e-mails via SMTP.
- **MimeText**: Formatação de e-mails.

---

## 🧪 Testando o Programa

Certifique-se de testar o programa em um ambiente controlado antes de utilizá-lo com e-mails reais. O envio de e-mails incorretos pode causar problemas com o servidor SMTP.

```
