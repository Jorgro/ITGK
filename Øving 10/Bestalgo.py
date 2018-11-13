hukommelse = {}


def main(hukommelse):
    n = nummer()
    if n not in hukommelse:
        hukommelse[n] = {'venstre': False, 'hoyre': False}
    if er_utgang():
        gaa_ut()
        exit()
    if er_laas():
        laas_opp()
    if er_nokkel():
        plukk_opp()
        hukommelse = {}
        while n! = 0:
            gaa_tilbake()
            n = nummer()
        main(hukommelse)
    if er_stank():
        hukommelse[n]['venstre'] = True
        hukommelse[n]['hoyre'] = False

    if not hukommelse[n]['venstre']:
        gaa_venstre()
        hukommelse[n][venstre] = True
        main(hukommelse)

    if hukommelse[n]['venstre']:
        gaa_tilbake()
        if not hukommelse[n]['hoyre']:
            gaa_hoyre()
            hukommelse[n]['hoyre'] = True
            main(hukommelse)


main(hukommelse)




hukommelse = {}




def main(hukommelse):
    n = nummer()
    print(n)

    if er_nokkel():
        plukk_opp()
        hukommelse = {}
        while n != 0:
            gaa_tilbake()
            n = nummer()
        main(hukommelse)

    if er_laas():
        laas_opp()

    if n not in hukommelse:
        hukommelse[n] = {'venstre': False, 'hoyre': False}

    if er_stank():
        n = nummer()
        hukommelse[n]['venstre'] = True
        hukommelse[n]['hoyre'] = True
        exit()



    if not hukommelse[n]['venstre']:
        gaa_venstre()
        hukommelse[n]['venstre'] = True
        main(hukommelse)



    if not gaa_venstre() or hukommelse[n]['venstre']:
        gaa_tilbake()
        if not hukommelse[n]['hoyre']:
            gaa_hoyre()
            hukommelse[n]['hoyre'] = True
            main(hukommelse)


    if (hukommelse[n]['hoyre'] and hukommelse[n]['venstre']) or (not gaa_hoyre() and not gaa_venstre()):
        gaa_tilbake()
        main(hukommelse)

    main(hukommelse)

main(hukommelse)
