from getSimilarities import getSimilarities

messages = []
print("Bienvenido a su asistente personal Ajojo-amigo!!!\nPor favor, cuentame tu día")
while True:
    user_input = input("$ ")
    messages.append(user_input)
    print("Hay algo más que me quieras contar? [y/n]")
    user_input = input("$ ")
    if user_input != 'y' and user_input != 'Y':
        break

for i in messages:
    num_similitudes = getSimilarities(i)
    if(num_similitudes > 40):
        print("Emergencia: {0}".format(i))
