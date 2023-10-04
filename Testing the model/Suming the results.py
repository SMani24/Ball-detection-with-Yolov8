# In the name of God
# SMani24
import pandas as pd
import os

finalResult= pd.DataFrame(index=["Detected", "Not Detected"], columns=["Ball in frame", "Ball not in frame", "Half ball"]) 
finalResult["Ball in frame"]["Detected"] = 0
finalResult["Ball not in frame"]["Detected"] = 0
finalResult["Half ball"]["Detected"] = 0
finalResult["Ball in frame"]["Not Detected"] = 0
finalResult["Ball not in frame"]["Not Detected"] = 0
finalResult["Half ball"]["Not Detected"] = 0

for resultPath in os.listdir("./results"):
    result = pd.read_csv("./results/" + resultPath)
    print(result)
    finalResult["Ball in frame"]["Detected"] += result["Ball in frame"][0]
    finalResult["Ball not in frame"]["Detected"] += result["Ball not in frame"][0] 
    finalResult["Half ball"]["Detected"] += result["Half ball"][0]
    finalResult["Ball in frame"]["Not Detected"] += result["Ball in frame"][1]
    finalResult["Ball not in frame"]["Not Detected"] += result["Ball not in frame"][1]
    finalResult["Half ball"]["Not Detected"] += result["Half ball"][1]

finalResult.to_csv("finalResults.csv")