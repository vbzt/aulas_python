def calc_media(gs: bool):
    cps = []
    while(len(cps)) < 3:
        cp = float(input(f"Nota checkpoint {len(cps)+1}: "))
        if 0 <= cp <= 10:
            cps.append(cp)
        else:
            print('Nota inválida, digite um número entre 0 e 10')


    sorted_cps = sum(sorted(cps)[-2:])


    sp1 = float(input('Nota sprint 1: '))
    sp2 = float(input('Nota sprint 2: '))


    if gs:
        gs = float(input("Nota Global solution: "))
        mf = sorted_cps * 0.1  + (sp1 + sp2) * 0.1 + gs * 0.6
        return mf

    mf = sorted_cps * 0.1  + (sp1 + sp2) * 0.1
    return mf

sem1 = calc_media(True)
sem2 = calc_media(False)

nota_gs2 = 6 - (sem1 * 0.4) - (sem2 * 0.6)

if nota_gs2 > 0:
    print(f'Nota necessária para Global solution do segundo semestre: {nota_gs2}')
else:
    print("Já passou de ano. ")







