import csv
import matplotlib.pyplot as plt
import pandas as pd

TARGET=""

def main():
    found_list = dict()
    streamer_names = list()
    overlab_amount = list()
    data_source = open("2021_04_13_twitch_edglist.csv")
    data = csv.reader(data_source, delimiter=",")
    for row in data:
        if row[0].lower() == TARGET.lower():
            found_list[row[1]] = int(row[2])
        elif row[1].lower() == TARGET.lower():
            found_list[row[0]] = int(row[2])
    # plt.bar(x=streamer_names, height=overlab_amount)
    df = pd.DataFrame({"Streamer":found_list.keys(), "Chatter:innen":found_list.values()})
    df.sort_values("Chatter:innen", inplace=True, ascending=False)
    df = df[:60]
    df.plot(kind="bar", y="Chatter:innen",x="Streamer")
    plt.title(f"{TARGET} Chatter:innen Crossover aus top 2000 Streamer:innen")
    plt.xticks(rotation=90)
    plt.grid(axis="y")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()