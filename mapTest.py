import pandas as pd
import folium as F
import csv 
longboi = pd.read_csv("LongBoi.csv")
#53.0765452103364, 8.820692530590472

lokationer = []


for row in longboi.iterrows():
    lok = (
            row[1].get('latitude'),
            row[1].get('longitude')
    )
    lokationer.append(lok)
    
map = F.Map(location=lokationer[0], zoom_start=17)


last_lok = None
for lok in lokationer:
    F.Marker(lok, popup='Binaur').add_to(map)
    
    if last_lok:
        F.PolyLine(locations=[last_lok, lok], color='red').add_to(map)        
    
    last_lok = lok


# F.PolyLine(locations=[(16.350000, 81.050000), (26.383333, 80.166667)], color='blue').add_to(map)
# F.PolyLine(locations=lokationer, color='blue').add_to(map)
map.show_in_browser()
map.save("Map.html")
input("wait for exit")
