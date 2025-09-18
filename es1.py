tupla_partite = (
    ("SquadraA", "SquadraB", 3, 2),
    ("SquadraC", "SquadraD", 1, 1),
    ("SquadraB", "SquadraC", 2, 4),
    ("SquadraD", "SquadraA", 0, 3),
    ("SquadraB", "SquadraD", 1, 2),
)


def media_goal_partite(tupla):
    sommaGoal = 0 
    
    for _,_,goalCasa, goalOspite in tupla:
        sommaGoal += goalCasa + goalOspite

    if (len(tupla) > 0):
        return (sommaGoal / len(tupla))
    else:
        return "Impossibile procedere col calcolo della media."

def media_goal_squadre(tupla, squadra):
   goalSquadra = 0 
   partiteSquadra = 0

   for squadraCasa, squadraOspite, goalCasa, goalOspite in tupla:
        if(squadraCasa == squadra):
            goalSquadra += goalCasa
            partiteSquadra += 1
        elif(squadraOspite == squadra):
            goalSquadra += goalOspite
            partiteSquadra += 1

   if(partiteSquadra > 0):
        return (goalSquadra / partiteSquadra)
   else:
        return "Impossibile determinare i goal per questa squadra."
              

def partita_piu_goal(tupla):
    goalMax = 0
    partita = ""

    for sqCasa, sqOspite, goalCasa, goalOspite in tupla:
        if(goalMax < (goalCasa + goalOspite)):
            goalMax = goalCasa + goalOspite
            partita = f"{sqCasa} - {sqOspite}"

    return f"{partita} con {goalMax} goal."


def percentuale_vittorie_squadra(tupla, squadra):
    vittorieSquadra = 0
    partiteGiocate = 0

    print(squadra)

    for squadraCasa, squadraOspite, goalCasa, goalOspite in tupla:
        if(squadra == squadraCasa and goalCasa > goalOspite):
            vittorieSquadra += 1
        elif(squadra == squadraOspite and goalOspite > goalCasa):
            vittorieSquadra += 1
        
        if(squadraCasa == squadra or squadraOspite == squadra):
            partiteGiocate += 1

    if(partiteGiocate > 0):
        return f"Pecentuale di vittorie: {(vittorieSquadra / partiteGiocate * 100)}%"
    else:
        return "Impossibile determinare la percentuale di vittorie della squadra selezionata."

while True:
    print("Seleziona tra le seguenti opzioni:")
    print("1. Media Goal Partite")
    print("2. Media Goal Squadra")
    print("3. Partita con più goal")
    print("4. Percentuale vittorie squadra")
    print("5. Esci")
    scelta = int(input("Inserisci la tua scelta: "))

    match(scelta):
        case 1:
            print(f"\nLa media dei goal a partita è: {media_goal_partite(tupla_partite)}\n")
        case 2:
            squadraMedia = input("\nInserisci il nome della squadra: ")
            print(f"Media goal per quella squadra: {media_goal_squadre(tupla_partite, squadraMedia)}\n")
        case 3:
            print(f"\nLa partita con più goal è: {partita_piu_goal(tupla_partite)}\n")
        case 4:
            squadraPercentuale = input("\nInserisci il nome della squadra: ")
            print(f"Percentuale di vittorie: {percentuale_vittorie_squadra(tupla_partite, squadraPercentuale)}\n")
        case 5:
            break