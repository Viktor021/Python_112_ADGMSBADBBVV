import folium

m = folium.Map(location=[46.25603836330232, 20.13858684535948], zoom_start=13)

folium.CircleMarker(
    location=[46.25603836330232, 20.13858684535948],
    radius=50,
    popup="Gábor Dénes Szeged",
    color="blue",
    fill=True,
    fill_color="blue",
).add_to(m)

m.save("map.html")