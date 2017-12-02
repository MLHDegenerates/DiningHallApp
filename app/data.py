halls = [
    {
        "name": "Lenny",
        "lat": 44.224267,
        "lng": -76.500690,
        "infobox": "",
        "icon": "http://maps.google.com/mapfiles/ms/icons/green-dot.png",
        "people": 0
    },
    {
        "name": "Ban Righ",
        "lat": 44.224628,
        "lng": -76.496264,
        "infobox": "",
        "icon": "http://maps.google.com/mapfiles/ms/icons/blue-dot.png",
        "people": 0
    }
]
lat = 44.226122
lng = -76.495110


def update():
    for hall in halls:
        hall["infobox"] = "%d people<br><a href=''>Check In</a>" % hall["people"]


