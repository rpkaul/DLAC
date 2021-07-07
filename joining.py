import numpy


import pandas as pd
from math import sqrt,asin,atan2,pi


df3 = pd.read_csv("killtest.csv")

print(df3.columns)
#df3 = df3.set_index('TICK')
df3 = df3[df3["AttackerName"] == "TeiToN"]



victims = [x for x in df3["VictimName"]]
for x in victims:
    df = pd.read_csv("test.csv")

    df1 = df[df["Name"] == "TeiToN"]
    df2 = df[df["Name"] == x]
    print(x)
    df1 = df1.set_index("TICK")

    df2 = df2[["TICK","X","Y","Z"]]
    df2=df2.set_index("TICK")

    # Convert 0-360 range to -180 - 180 range for easier trig
    df1['ViewX'] = (df1['ViewX'] + 180) % 360 - 180
    df1['ViewY'] = (df1['ViewY'] + 180) % 360 - 180

    big = df1.merge(df2,on='TICK')

    x_off = []
    y_off = []

    for row in range(len(big)):
        x1 = big.iloc[row]["X_x"]
        y1 = big.iloc[row]["Y_x"]
        z1 = big.iloc[row]["Z_x"]

        x2 = big.iloc[row]["X_y"]
        y2 = big.iloc[row]["Y_y"]
        z2 = big.iloc[row]["Z_y"]

        xdif = x2 - x1
        ydif = y2 - y1
        zdif = z2 - z1

        x = atan2(ydif, xdif) * (180 / pi)
        hypot3D = sqrt(zdif ** 2 + xdif ** 2 + ydif ** 2)

        rightLeft = x
        upDown = -asin(zdif / hypot3D) * (180 / pi)

        x_off.append(rightLeft)
        y_off.append(upDown)

    big["X_Off_By_Degrees"] = x_off
    big["Y_Off_By_Degrees"] = y_off

    big.to_csv(f"meme{x}.csv")



"""# drop dupes
df2 = df2.drop_duplicates()
# Check how many files in output dir so to know what name to give file
n_files = len([name for name in os.listdir(out_folder)])
print("n_files",n_files)

for cnt, x in enumerate(range(len(df2))):
    # Get the next kill and append to list
    mintick = min(df2["TICK"])
    out_df = df1[df1['TICK'] <= mintick]

    if len(out_df)>0:
        retruning_list.append(out_df)
        if write_to_csv is True:
            out_df.to_csv(f"{out_folder}/singlekills/{n_files + cnt}.csv")

    # Cut off kill from big dfs
    df1 = df1[df1['TICK'] > mintick]
    df2 = df2[df2['TICK'] > mintick]"""