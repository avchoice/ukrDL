import pandas as pd
import makeTeamLists as mtl
import tourneyTablesDict as ttd
import readTournament as readt


tourneyNames = []
tourneyDLs = []


def ukrDL(address: str, name: str, rated: bool, season: str):
    if season == "24/25":
        teams15 = mtl.teams15_2425
        teams610 = mtl.teams610_2425
        teams1115 = mtl.teams1115_2425
        teams1630 = mtl.teams1630_2425
        teams31plus = mtl.teams31plus_2425
    elif season == "25/26":
        teams15 = mtl.teams15
        teams610 = mtl.teams610
        teams1115 = mtl.teams1115
        teams1630 = mtl.teams1630
        teams31plus = mtl.teams31plus
    tour = readt.readTournament(address)
    dls = []
    N = tour.sum(numeric_only=True, axis=0).count()
    for team in tour["Команда"]:
        if team in teams15:
            if rated: C = coeffs["1-5"]
            if not rated: C = coeffsNotRated["1-5"]
        elif team in teams610:
            if rated: C = coeffs["6-10"]
            if not rated: C = coeffsNotRated["6-10"]
        elif team in teams1115:
            if rated: C = coeffs["11-15"]
            if not rated: C = coeffsNotRated["11-15"]
        elif team in teams1630:
            if rated: C = coeffs["16-30"]
            if not rated: C = coeffsNotRated["16-30"]
        elif team in teams31plus:
            if rated: C = coeffs["31+"]
            if not rated: C = coeffsNotRated["31+"]
        else:
            if rated: C = coeffs["UR"]
            if not rated: C = coeffsNotRated["UR"]
        Q = tour[tour["Команда"]==team].sum(numeric_only=True, axis=1).item()
        teamDL = (1 - min(Q/C, N) / N) * 10
        dls.append(teamDL)
    ukrdl = (sum(dls) / len(dls)).round(2)
    tourneyNames.append(name)
    tourneyDLs.append(ukrdl)
    print(f'"{name}": {ukrdl}')


coeffs = {"1-5": 1.28, "6-10": 1.18, "11-15": 1.11, "16-30": 1.0, "31+": 0.71, "UR": 0.71}
coeffsNotRated = {"1-5": 1.28, "6-10": 1.18, "11-15": 1.11, "16-30": 1.0, "31+": 0.73, "UR": 1.0}
for key, value in ttd.tourneyTables.items():
    ukrDL(key, value, rated=True, season="24/25")
print("------")
for key, value in ttd.tourneyTables2.items():
    ukrDL(key, value, rated=False, season="24/25")
print("------")
for key, value in ttd.tourneyTables3.items():
    ukrDL(key, value, rated=True, season="25/26")
print("------")
for key, value in ttd.tourneyTables4.items():
    ukrDL(key, value, rated=False, season="25/26")
print("------")

table = pd.DataFrame({"Назва": tourneyNames, "ukrDL": tourneyDLs})
table.to_excel('output/ukrdl.xlsx', index=False)