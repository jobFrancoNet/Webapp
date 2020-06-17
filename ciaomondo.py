

i""Inserire in una lista dei dati immessi in input"""

attivita = input('inserisci la tipologia della tua attività: ')

categoria = ['supermercato', 'farmacia']

if str(attivita) == categoria:
    print("La tua attività è già presente")
else:
    categoria.append(attivita)

print(categoria)
