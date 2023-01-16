# Cute-Interpreter
Projekt realizowany razem z [Jakub Domogała](https://github.com/Jakub-Domogala) na przedmiot Metody i Algorytmy Kompilacji.

Jest to interpreter wymyślonego przez nas języka Cute :sparkles:

## Opis zasad
### Zmienne
Język jest typowany, więc potrzebujemy deklaracji każdej zmiennej przed jej  wywołaniem. Mamy dostępne 3 typy zmiennych: zerojedynek - wartość boolowska, bezprzecinek - liczba całkowita i zprzecinek - liczba wymierna. Wartości liczbowe mogą być dodatnie jak i ujemne. Przy deklaracji zmiennej musimy użyć między jej typem, a nazwą zmiennej symbolu ->, a jeśli chcemy przypisać do niej wartość to możemy to zrobić po symbolu <-. Oczywiście nie zapominamy o znaku końca linii. W nazwie zmiennej może występować symbol “_”, ale nie może znajdować się na początku.

    bezprzecinek -> count <- 0 |<3|
    zerojedynek -> flag_to_Print |<3|


### Operacje arytmetyczne 
W naszym języku mamy dostępne operacje arytmetyczne: dodawanie, odejmowanie, mnożenie i dzielenie. Ze znakami odpowiednio: +,  -,  * i /. Postanowiliśmy wykonywać operacje tylko na jeśli typy są takie same, więc nie jest możliwe dodanie bezprzecinka do zprzecinka. 
Dostępna jest również standardowa operacja modulo - |%|, dzielenie całkowitoliczbowe - |/|, maximum - |^| i minimum - |v| dwóch liczb oraz potęgowanie - |*|.

    bezprzecinek -> nazwazmiennej <- 5 |^| 1 |^| 10 |<3|
    count <- (5 + 3) |%| (4 |v| 1) |<3|

### Operacje logiczne
Dostępne są dwie operacje logiczne oraz i lub. Możemy porównywać wartości, słowem kropkawkropke sprawdzamy czy dane wartości są takie same. Słowem innyod sprawdzamy czy wartości są od siebie różne. Możemy również sprawdzić która z wartości jest większa lub mniejsza, słowami wiekszyod i mniejszyod. Możemy użyć również zaprzeczenia wartości logicznej lub wyrażenia przez  zastosowanie symbolu not  przed.

    var <- count mniejszyod amount_to_print |<3|
    val <- 5 kropkawkropke 3 |<3|

### Bloki
Ograniczone są w nawiasach “{  }”. Wewnątrz takiego bloku możemy wykonywać pętle, deklarować zmienne, przypisywać wartości, sprawdzać warunki oraz wypisywać wartości. Bloki mogą być zagnieżdżane w sobie.

    powielanko(a1 mniejszyod 10) {
       waruneczek(1 kropkawkropke nieprawda) {
           drukareczka(a1) |<3|
       }
    }


### Pętla oraz if.
Możemy wywołać pętle powielanko  z warunkiem logicznym w nawiasie “(  )”. Po warunku następuje instrukcja w bloku. Podobnie możemy sprawdzać warunki poprzez słowo waruneczek. Po nim znajduje się warunek w nawiasie “(  ) “ oraz instrukcja w bloku.

    powielanko(a1 mniejszyod 10) {
     . . .
    }

    waruneczek(1 kropkawkropke nieprawda) {
    . . .
    }

### Wypisywanie
Dostępne jest wypisywane wartości  na konsole poprzez słowo drukareczka . Wartość którą chcemy wypisać musi być w nawiasie “(  )”. Jeśli chcemy wypisać wartość  zmiennej wcześniej zadeklarowanej podajemy jej nazwę w nawiasie  w wyniku dostaniemy również informacje o jej typie. 

    drukareczka(a1) |<3|

### Komentarze
Możemy pisać komentarze jednolinijkowe poprzez wystąpienie symbolu |<3|  na początku linii. Po tym symbolu może występować dowolny ciąg.

    |<3| to jest komentarz


#### Przykład 
Poniżej znajduje się zaimplementowany algorytm do wypisywania 20 pierwszych wyrazów ciągu Fibonacciego w naszym języku.

    bezprzecinek -> amount_to_print <- 20|<3|
    bezprzecinek -> count <- 0 |<3|
    bezprzecinek -> n1 <- 0 |<3|
    bezprzecinek -> n2 <- 1 |<3|
    bezprzecinek -> n3 |<3|

    powielanko(count mniejszyod amount_to_print) {
       drukareczka(n1) |<3|
       n3 <- n1 + n2 |<3|
       n1 <- n2 |<3|
       n2 <- n3 |<3|
       count <- count + 1 |<3|
    }

