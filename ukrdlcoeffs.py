import pandas as pd
import readTournament as readt
import tourneyTablesDict as ttd


ratingFil = pd.read_csv("history2425only.csv")
ratingList = ratingFil["Команда"].to_list()
teams15 = ratingList[0:5]
teams610 = ratingList[5:10]
teams1115 = ratingList[10:15]
teams1630 = ratingList[15:30]
teams31plus = ratingList[30:]

means15 = []
means610 = []
means1115 = []
means1630 = []
means31plus = []
meansur = []


def avgResultPerPlaces(address: str, unratedPlace: str) -> pd.core.frame.DataFrame:
    tour = readt.readTournament(address)
    placesInRating = []
    for team in tour["Команда"]:
        if team in teams15:
            placesInRating.append("1-5")
        elif team in teams610:
            placesInRating.append("6-10")
        elif team in teams1115:
            placesInRating.append("11-15")
        elif team in teams1630:
            placesInRating.append("16-30")
        elif team in teams31plus:
            placesInRating.append("31+")
        else:
            placesInRating.append(unratedPlace)
    tour["Місце в рейтингу"] = placesInRating
    avgres15 = tour[tour["Місце в рейтингу"]=="1-5"].sum(numeric_only=True, axis=1).mean()
    avgres610 = tour[tour["Місце в рейтингу"]=="6-10"].sum(numeric_only=True, axis=1).mean()
    avgres1115 = tour[tour["Місце в рейтингу"]=="11-15"].sum(numeric_only=True, axis=1).mean()
    avgres1630 = tour[tour["Місце в рейтингу"]=="16-30"].sum(numeric_only=True, axis=1).mean()
    avgres31plus = tour[tour["Місце в рейтингу"]=="31+"].sum(numeric_only=True, axis=1).mean()
    avgresur = tour[tour["Місце в рейтингу"]=="UR"].sum(numeric_only=True, axis=1).mean()
    means15.append(avgres15)
    means610.append(avgres610)
    means1115.append(avgres1115)
    means1630.append(avgres1630)
    means31plus.append(avgres31plus)
    if str(avgresur) != "nan":
        meansur.append(avgresur)
    return tour


def evalCoeffs():
    avg15 = sum(means15)/len(means15)
    avg610 = sum(means610)/len(means610)
    avg1115 = sum(means1115)/len(means1115)
    avg1630 = sum(means1630)/len(means1630)
    avg31plus = sum(means31plus)/len(means31plus)
    if len(meansur) != 0:
        avgur = sum(meansur)/len(meansur)
    else: 
        avgur = 0
    
    if avgur != 0:
        averages = {"1-5": avg15, "6-10": avg610, "11-15": avg1115, "16-30": avg1630, "31+": avg31plus, "UR": avgur}
    else:
        averages = {"1-5": avg15, "6-10": avg610, "11-15": avg1115, "16-30": avg1630, "31+ and UR": avg31plus}
    normer = avg1630
    for key, value in averages.items():
        value = (value / normer).round(2)
        averages[key] = value
        print(f"{key}: {value}")


for key, value in ttd.tourneyTables.items():
    avgResultPerPlaces(key, "31+")
evalCoeffs()


print("------")
means15.clear()
means610.clear()
means1115.clear()
means1630.clear()
means31plus.clear()
meansur.clear()
for key, value in ttd.tourneyTables.items():
    avgResultPerPlaces(key, "UR")
evalCoeffs()