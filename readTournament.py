import pandas as pd
import makeTeamLists as mtl


def readTournament(address: str) -> pd.core.frame.DataFrame:
    tour = pd.read_excel(address)
    tour.dropna(axis=0, inplace=True)
    if 'Team ID' in tour.columns:
        tour.drop(columns=['Team ID'], inplace=True)
    if 'Название' in tour.columns:
        tour.rename(columns={"Название": "Команда"}, inplace=True)
    if 'Город' in tour.columns:
        tour.rename(columns={"Город": "Місто"}, inplace=True)
    for key, value in mtl.TEAM_MAPPING.items():
        for team in tour["Команда"]:
            if team in value:
                tour.replace({team: key}, inplace=True)
    # tour = tour[tour['Команда'].isin(ratingList)]
    return tour