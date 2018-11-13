# Definer denne en eller annen plass, f.eks på toppen av fila:
#     hukommelse = {}
# For hver ny node som ikke er i hukommelsen:
#     n = nummer ()
#     if n not in hukommelse :
#         hukommelse [n] = { " venstre ": False , " hoyre ": False }
# Oppdater nøklene venstre og høyre etter hvert som du besøker de retningene:
#     hukommelse [n][" venstre "] = True # f.eks
# For å nullstille hukommelsen:
#     hukommelse = {}
hukommelse = {}
import Skumleskogen
def main():
    if er_stank() or er_inngang():
        gaa_tilbake()
    if er_utgang():
        gaa_ut()
    if er_laas() or er_superlaas():
        laas_opp()

    n = nummer ()
    if n not in hukommelse :
        hukommelse [n] = {"venstre": False , "hoyre": False }

    if not hukommelse[n]['venstre']:
        gaa_venstre()
        hukommelse [n]["venstre"] = True
        if er_nokkel():
            plukk_opp()
            hukommelse = {}
    if not hukommelse[n]['hoyre']:
        gaa_hoyre()
        hukommelse [n]["hoyre"] = True
        if er_nokkel():
            plukk_opp()
            hukommelse = {}

    main()

main()
