import pywhatkit

num_celular = input('Numero do contato')
msg = input('Digite aqui sua mensagem')
pywhatkit.sendwhatmsg(num_celular, msg, 12, 12, 30)
