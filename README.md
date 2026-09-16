# UmaMusume Trainee Dataset
Simple script to web scrap Umamusume trainee's information and create a dataset

> This script scraps the [umamusume wiki](https://umamusu.wiki/Game:List_of_Trainees) list of trainees page 

> The resultant dataset can be found on [Kaggle](https://www.kaggle.com/datasets/kokoapo/umamusume-trainees/data)

## How to run this script

1. Download the [dependencies](requirements.txt) using `pip install -r requirements.txt`
2. Run `python main.py` in the root folder
3. The results will be on [data.csv file](data.csv)

## Columns in the table

The table currently has the following columns:

- Id: Trainee Id in the dataframe
- Name: Trainee name (in japanese if there's no english version)
- Character: Trainee uma musume
- Release Date (JP): Release date in Japan server (null if it didn't released yet)
- Release Date (EN): Release date in English server (null if it didn't released yet)
- Rarity: Trainee rarity by star count
- Speed%: Bonus percentage on Speed stat training
- Stamina%: Bonus percentage on Stamina stat training
- Power%: Bonus percentage on Power stat training
- Guts%: Bonus percentage on Guts stat training
- Wit%: Bonus percentage on Wit stat training
- Turf: Turf terrain aptitude
- Dirt: Dirt terrain aptitude
- Sprint: Sprint distance aptitude
- Mile: Mile distance aptitude
- Middle: Middle distance aptitude
- Long: Long distance aptitude
- Front: Front style aptitude
- Pace: Pace style aptitude
- Late: Late style aptitude
- End: End style aptitude