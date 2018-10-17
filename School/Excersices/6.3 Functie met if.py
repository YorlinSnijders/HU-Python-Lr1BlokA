def lang_genoeg(lengte):
    if lengte >= 120:
        return ("Je bent lang genoeg voor de attractie!")
    return ("Sorry, je bent te klein!”")

print(lang_genoeg(120))
print(lang_genoeg(119))