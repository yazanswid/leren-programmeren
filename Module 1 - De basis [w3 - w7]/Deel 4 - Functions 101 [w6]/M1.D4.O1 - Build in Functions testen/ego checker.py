import re

def split_into_sub_sentences(text):
    # Vervang alle separators door een marker "|"
    marked_text = re.sub(r"\.|,|!|\?| en |omdat |zodat |want |wanneer |dat ", "|", text)
    # Splits de tekst op de marker "|"
    return marked_text.split("|")

def calculate_ego_score(sub_sentences):
    ego_score = 0
    for sentence in sub_sentences:
        sentence = sentence.strip().lower()  # Verwijder spaties en maak kleine letters
        if len(sentence) > 0:
            words = sentence.split(' ')  # Splits zin in woorden
            # Controleer of de eerste of tweede woord 'ik' of 'mijn' is
            if len(words) >= 2 and (words[0] in ('ik', 'mijn') or words[1] in ('ik', 'mijn')):
                ego_score += 1
    return ego_score

# Voorbeeld tekst voor testen
text = """
Geachte heer/mevrouw,
Ik wil graag solliciteren naar de functie van programmeur bij uw bedrijf. 
Ik ben de beste kandidaat voor deze functie omdat ik al jaren ervaring heb in deze branche 
en ik weet dat niemand anders mijn niveau van kennis en vaardigheden kan evenaren. 
"""

# Functie aanroepen en ego-score berekenen
sub_sentences = split_into_sub_sentences(text)
ego_score = calculate_ego_score(sub_sentences)

# Resultaat printen
print(f"Ego-score: {ego_score}")