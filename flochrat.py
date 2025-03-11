import graphviz

def create_flowchart():
    dot = graphviz.Digraph()
    
    # Start
    dot.node('Start', 'Start', shape='oval')
    
    # Initialisatie
    dot.node('Init', 'Score = 0\nRonde = 1', shape='rectangle')
    dot.edge('Start', 'Init')
    
    # Nieuwe ronde check
    dot.node('NewRound?', 'Nieuwe ronde? (max 20)', shape='diamond')
    dot.edge('Init', 'NewRound?')
    
    # Stop als geen nieuwe ronde
    dot.node('End', 'Einde', shape='oval')
    dot.edge('NewRound?', 'End', label='Nee')
    
    # Genereer geheim getal
    dot.node('Generate', 'Geheim getal =\nrandom(1-1000)', shape='rectangle')
    dot.edge('NewRound?', 'Generate', label='Ja')
    
    # Beurt starten
    dot.node('Turn', 'Beurt = 1', shape='rectangle')
    dot.edge('Generate', 'Turn')
    
    # Speler raadt getal
    dot.node('Guess', 'Speler raadt getal', shape='parallelogram')
    dot.edge('Turn', 'Guess')
    
    # Vergelijking
    dot.node('Compare', 'Getal correct?', shape='diamond')
    dot.edge('Guess', 'Compare')
    
    # Correct geraden
    dot.node('Correct', 'Score += 1\nRonde stopt', shape='rectangle')
    dot.edge('Compare', 'Correct', label='Ja')
    dot.edge('Correct', 'NewRound?')
    
    # Hoger/Lager feedback
    dot.node('Higher', 'Hoger! Probeer opnieuw', shape='rectangle')
    dot.node('Lower', 'Lager! Probeer opnieuw', shape='rectangle')
    dot.edge('Compare', 'Higher', label='Nee & te laag')
    dot.edge('Compare', 'Lower', label='Nee & te hoog')
    dot.edge('Higher', 'Guess')
    dot.edge('Lower', 'Guess')
    
    # Warm en heel warm feedback
    dot.node('Warm', 'Je bent warm! (verschil <50)', shape='rectangle')
    dot.node('Hot', 'Je bent heel warm! (verschil <20)', shape='rectangle')
    dot.edge('Higher', 'Warm', constraint='false')
    dot.edge('Lower', 'Warm', constraint='false')
    dot.edge('Warm', 'Hot', constraint='false')
    dot.edge('Hot', 'Guess', constraint='false')
    
    # Beurten check
    dot.node('TurnsLeft?', 'Max 10 beurten?', shape='diamond')
    dot.edge('Compare', 'TurnsLeft?', label='Nee')
    dot.edge('TurnsLeft?', 'Guess', label='Nee')
    
    # Ronde einde bij 10 beurten
    dot.node('RoundEnd', 'Ronde voorbij\nToon score', shape='parallelogram')
    dot.edge('TurnsLeft?', 'RoundEnd', label='Ja')
    dot.edge('RoundEnd', 'NewRound?')
    
    # Eindscore
    dot.node('FinalScore', 'Toon eindscore', shape='parallelogram')
    dot.edge('End', 'FinalScore')
    
    return dot

# Maak en toon de flowchart
flowchart = create_flowchart()
flowchart.render('flowchart_guess_game', format='png', view=True)
