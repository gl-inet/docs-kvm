# Czym różni się tryb myszy Absolute od Relative {#what-is-the-difference-between-absolute-mouse-and-relative-mouse}

W konsoli GL.iNet KVM ustawienie **Mouse Mode** oferuje dwie opcje: **Absolute** i **Relative**. Tryby te znacznie różnią się sposobem sterowania myszą, zastosowaniem i wygodą obsługi. Poniższy opis pomoże dobrać tryb do swoich potrzeb.

![Tryb myszy](https://static.gl-inet.com/docs/kvm/faq/difference_between_absolute_and_relative_mouse/mouse_mode.jpg){class="glboxshadow"}

## Mysz w trybie Absolute {#absolute-mouse}

Tryb Absolute zapewnia płynne i zsynchronizowane sterowanie myszą na komputerze lokalnym i urządzeniu docelowym. Po jego włączeniu kursory myszy obu urządzeń są odwzorowywane w tym samym układzie współrzędnych. Możesz płynnie przesuwać lokalny kursor między konsolą KVM a ekranem zdalnym — zdalny kursor będzie na bieżąco podążał za ruchem lokalnego kursora.

Podczas pracy może wystąpić niewielkie opóźnienie, co jest normalnym skutkiem transmisji sieciowej i kodowania obrazu. Zdalny kursor reaguje wtedy nieco wolniej niż lokalny, ale nie wpływa to na ogólną płynność obsługi.

![Tryb Absolute](https://static.gl-inet.com/docs/kvm/faq/difference_between_absolute_and_relative_mouse/absolute.gif)

## Mysz w trybie Relative {#relative-mouse}

Tryb Relative nie synchronizuje współrzędnych lokalnego i zdalnego kursora myszy; działają one w osobnych warstwach. Aby sterować urządzeniem docelowym, najpierw kliknij wewnątrz okna zdalnego, aby przechwycić kursor.

W tym trybie zdalny kursor pozostaje „zamknięty” w oknie zdalnym i nie może płynnie przejść poza jego granice na pulpit lokalny. Krawędzie okna ograniczają jego ruch do środowiska sterowanego. Aby zwolnić kursor i odzyskać kontrolę nad komputerem lokalnym, naciśnij klawisz `Esc`.

![Tryb Relative](https://static.gl-inet.com/docs/kvm/faq/difference_between_absolute_and_relative_mouse/relative.gif)

W trybie Relative możesz zmienić ustawienie **Relative Sensitivity** w zakresie od 0.1 do 2.0.

![Czułość w trybie Relative](https://static.gl-inet.com/docs/kvm/faq/difference_between_absolute_and_relative_mouse/relative_sensitivity.jpg){class="glboxshadow"}

## Najważniejsze różnice {#key-differences}

| Cecha | Mysz w trybie Absolute | Mysz w trybie Relative |
| -------------------- | ------------------------------ | ----------------------------- |
| Koordynacja kursorów | Kursory lokalny i zdalny są zsynchronizowane (ten sam układ współrzędnych) | Kursory lokalny i zdalny działają w osobnych warstwach (bez synchronizacji współrzędnych) |
| Obsługa | Nie wymaga kliknięcia w celu przechwycenia kursora; płynne przechodzenie między ekranami | Wymaga kliknięcia ekranu zdalnego w celu przechwycenia kursora; brak płynnego przechodzenia między ekranami |
| Opóźnienie | Niewielkie (transmisja sieciowa i kodowanie obrazu) | Niemal niezauważalne (przesyłane są tylko przyrosty ruchu) |
| Zastosowanie | Płynna obsługa wielu ekranów, częste przełączanie, precyzyjne wskazywanie (praca zdalna, projektowanie graficzne) | Starsze urządzenia / BIOS / UEFI bez obsługi trybu Absolute; unikanie przypadkowych kliknięć; niestabilne sieci (mniejsze opóźnienie) |

## Podsumowanie {#summary}

Tryb Absolute stawia na płynną, spójną obsługę, a tryb Relative na zgodność i stabilność.

W większości codziennych zastosowań zdalnego sterowania przez GL.iNet KVM zalecanym ustawieniem domyślnym jest tryb Absolute. Tryb Relative warto wybrać w razie problemów ze zgodnością lub szczególnych wymagań obsługi.

- Używaj **Absolute Mouse** do płynnego, codziennego sterowania zdalnego.
- Używaj **Relative Mouse** do dostępu do BIOS, obsługi starszych urządzeń bez pozycjonowania bezwzględnego lub w celu uniknięcia przypadkowych kliknięć.

---

Masz jeszcze pytania? Odwiedź nasze [forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
