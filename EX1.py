temperaturas = [
    [28, 31, 34, 33],
    [25, 27, 29, 28],
    [32, 35, 36, 34],
    [24, 26, 25, 27]
]

num_sala = 1
maior = 0
sala_maior_risco = 0

for sala in temperaturas:
    print("SALA", num_sala)
    print("Media:", sum(sala) / len(sala))

    registros_criticos = 0

    for temp in sala:
        if temp >= 33:
            registros_criticos += 1

    print("Registros criticos:", registros_criticos)
    print()

    if registros_criticos > maior:
        maior = registros_criticos
        sala_maior_risco = num_sala

    num_sala += 1

print("Sala com maior risco: Sala", sala_maior_risco)