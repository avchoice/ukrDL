import pandas as pd
import readTournament as readt
import tourneyTablesDict as ttd


tourneyNames = []
tourneyDLs = []


def pl1takDL(address: str, name: str):
    tour = readt.readTournament(address)
    tourDifficulty = ((1 - tour.mean(numeric_only=True, axis=0)).mean() * 10).round(2)      # кількість невзятих поділити на загальну кількість, помножити на 10
    tourneyNames.append(name)
    tourneyDLs.append(tourDifficulty)
    print(f'pl1takDL турніру "{name}": {tourDifficulty}')


for key, value in ttd.tourneyTables.items():
    pl1takDL(key, value)
print("------")
for key, value in ttd.tourneyTables2.items():
    pl1takDL(key, value)


table = pd.DataFrame({"Назва": tourneyNames, "pl1takDL": tourneyDLs})
table.to_excel('output/pl1takdl.xlsx', index=False)