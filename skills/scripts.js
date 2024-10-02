// Prijzen per pizzagrootte
const pizzaPrices = {
    small: 8.50,
    medium: 10.50,
    large: 12.50
};

// Functie om het huidige jaar in de footer te zetten
document.getElementById('year').textContent = new Date().getFullYear();

// Functie om de totale prijs te berekenen en weer te geven
function calculateTotal() {
    // Haal de waarden van de inputvelden op
    const smallQty = parseInt(document.getElementById('small').value) || 0;
    const mediumQty = parseInt(document.getElementById('medium').value) || 0;
    const largeQty = parseInt(document.getElementById('large').value) || 0;

    // Bereken de totale kosten per afmeting
    const smallTotal = smallQty * pizzaPrices.small;
    const mediumTotal = mediumQty * pizzaPrices.medium;
    const largeTotal = largeQty * pizzaPrices.large;
    const grandTotal = smallTotal + mediumTotal + largeTotal;

    // Bouw de HTML voor de resultaten
    let resultHTML = "<h2>Besteloverzicht</h2><ul>";

    if (smallQty > 0) {
        resultHTML += `<li>${smallQty}x small pizza(s) - €${smallTotal.toFixed(2)}</li>`;
    }
    if (mediumQty > 0) {
        resultHTML += `<li>${mediumQty}x medium pizza(s) - €${mediumTotal.toFixed(2)}</li>`;
    }
    if (largeQty > 0) {
        resultHTML += `<li>${largeQty}x large pizza(s) - €${largeTotal.toFixed(2)}</li>`;
    }

    resultHTML += `</ul><h3>Totaal: €${grandTotal.toFixed(2)}</h3>`;

    // Toon het resultaat op het scherm
    document.getElementById('result').innerHTML = resultHTML;
}
