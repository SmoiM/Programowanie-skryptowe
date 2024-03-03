// typeof - zwraca typ wprowadzonych danych
// alert - wyświetla komunikat
// document - reprezentuje naszą stronę
// document.forms - zwraca wszystkie elementy <form>
function printForm() {
    alert("Tekstowe: " + typeof(document.forms['formularz'].elements[0].value) + " " + document.forms['formularz'].elements[0].value + "\nLiczbowe: " + typeof(document.forms[0].elements[1].value) + " " + document.forms[0].elements[1].value);
}

// onclick - zdarzenie kliknięcia w element
// wywołujemy funkcję prontForm, gdy klikniemy w wypisz (document.forms[0].elements[2])
document.forms[0].elements[2].onclick = printForm;