tupla_consumi_energetici = (
    ("Milano", [
        ("gennaio", ("elettrico", 300)),
        ("gennaio", ("gas", 150)),
        ("febbraio", ("elettrico", 280)),
        ("febbraio", ("gas", 120)),
        ("marzo", ("elettrico", 180)),
        ("marzo", ("gas", 20)),
    ]),
    ("Brescia", [
        ("gennaio", ("elettrico", 280)),
        ("gennaio", ("gas", 140)),
        ("febbraio", ("elettrico", 260)),
        ("febbraio", ("gas", 130)),
        ("marzo", ("elettrico", 80)),
        ("marzo", ("gas", 70)),
    ]),
    ("Catanzaro", [
        ("gennaio", ("elettrico", 80)),
        ("gennaio", ("gas", 10)),
        ("febbraio", ("elettrico", 26)),
        ("febbraio", ("gas", 130)),
        ("marzo", ("elettrico", 80)),
        ("marzo", ("gas", 170)),
    ]),
)

def analizza_consumi_energetici(tupla, cittaScelta, risorsa):
    mesiMaxRisorsa = []
    maxRisorsa = 0
    totaleRisorsa = 0
    contatoreRisorse = 0

    for citta, consumi in tupla:
        if(citta == cittaScelta):
            for mese, tipoDiRisorsa in consumi:
                if(maxRisorsa < tipoDiRisorsa[1] and tipoDiRisorsa[0] == risorsa):
                    maxRisorsa = tipoDiRisorsa[1]
                if(tipoDiRisorsa[0] == risorsa):
                    totaleRisorsa += tipoDiRisorsa[1]
                    contatoreRisorse += 1
                
    for citta, consumi in tupla:
        if(citta == cittaScelta):
            for mese, tipoDiRisorsa in consumi:
                if(tipoDiRisorsa[1] == maxRisorsa and tipoDiRisorsa[0] == risorsa):
                    mesiMaxRisorsa.append(mese)

    if(contatoreRisorse > 0):
        media = round(totaleRisorsa / contatoreRisorse)
        return (media, (maxRisorsa, mesiMaxRisorsa))
    else:
        return "Impossibile trovare la città oppure il tipo di risorsa."


citta = input("Inserisci la città da voler analizzare: ")
risorsa = input("Inserisci il tipo di risorsa da analizzare (elettrico o gas): ")
print(f"L'analisi è (media della risorsa, (massimo consumo, mese massimo consumo)): {analizza_consumi_energetici(tupla_consumi_energetici, citta, risorsa)}")
