'use strict'

let total = 0;

function cyfry(a) {
	let suma = 0;
    // replace() - zamienia podaną wartość na inną
    // [^0-9]/g 
    //      [^0-9] - dopasuj znaki, których nie ma w tej liście
    //      /g - global pattern flag - nie przestawaj po pierwszym dopasowaniu - zwróć wszyskie dopasowania
    // split() - dzieli tekst według podanego ograniczenia, np. spacja, przecinek...
    // parseInt() - parsuje łańcuch znaków i próbuje zwrócić liczbę całkowitą typu integer
    a.replace(/[^0-9]/g, '').split('').forEach((element) => {
		suma += parseInt(element);
	});

    return suma;
}

function litery(a) {
    // match() - dopasowuje do wzorca
    // \p{L} - dopasowuje dowolną literę
    // u - stosujemy unicode
    // || - operator "lub"
    return (a.match(/\p{L}/gu) || []).length;
}

function suma(a) {
    let sumaCala = parseInt(a);
    // isNaN - not-a-number - sprawdza, czy zmienna jest typu NaN czy też jest liczbą
    //  Zwraca true, gdy zmienna nie jest liczbą
    if (!isNaN(s))
        total += sumaCala;
    return total;
}