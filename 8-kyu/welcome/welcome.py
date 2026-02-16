def greet(language):
    choice = [ ("english", "Welcome")
              ,("czech", "Vitejte")
              ,("danish", "Velkomst")
              ,("dutch", "Welkom")
              ,("estonian", "Tere tulemast")
              ,("finnish", "Tervetuloa")
              ,("flemish", "Welgekomen")
              ,("french", "Bienvenue")
              ,("german", "Willkommen")
              ,("irish", "Failte")
              ,("italian", "Benvenuto")
              ,("latvian", "Gaidits")
              ,("lithuanian", "Laukiamas")
              ,("polish", "Witamy")
              ,("spanish", "Bienvenido")
              ,("swedish", "Valkommen")
              ,("welsh", "Croeso")
              ]
    for a, b in choice:
        if a == language:
            return b
    return "Welcome"