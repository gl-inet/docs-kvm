# Płytka ATX (GL-ATXPC) — podręcznik użytkownika {#atx-board-gl-atxpc-user-guide}

Płytka ATX to opcjonalne akcesorium do urządzeń KVM GL.iNet. Ten inteligentny moduł zarządzania zasilaniem umożliwia zdalne sterowanie zasilaniem sterowanego urządzenia przez symulowanie naciśnięć fizycznego przycisku zasilania (włączanie, wyłączanie i ponowne uruchamianie).

Płytkę ATX instaluje się wewnątrz obudowy sterowanego urządzenia, co zapewnia dyskretne i stabilne sterowanie zasilaniem.

**Uwaga**: Comet Q (GL-RMQ1) nie współpracuje z płytką ATX.

![Comet GL-RM1 z płytką ATX](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/rm1-and-atx-borad.jpg){class="glboxshadow"}

## Zawartość opakowania {#package-contents}

![Zawartość opakowania](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/inside-the-box.png){class="glboxshadow gl-80-desktop"}

- 1 x płytka główna ATX
- 1 x zestaw przewodów 9-PIN
- 1 x zestaw śrub
- 1 x kabel USB-A na Type-C
- 1 x zestaw mocujący ATX

## Układ pinów {#pin-out}

![Układ pinów](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/pinout.jpg){class="glboxshadow gl-80-desktop"}

Opis złączy:

1. Złącze Type-C: służy do połączenia z urządzeniem KVM.
2. Przycisk aktualizacji oprogramowania układowego mikrokontrolera na płytce głównej ATX.
3. Przycisk resetowania.
4. Złącze przewodów sterujących panelu komputera.
5. Złącze interfejsu F_PANEL komputera.

!!! note "Uwaga"

    1. Złączy 4 i 5 można używać zamiennie. Oznacza to, że do złącza 5 można podłączyć przewody sterujące panelu komputera, a do złącza 4 — interfejs F_PANEL.

    2. Na płytce ATX znajdują się dwie diody LED, które działają tak samo jak dioda zasilania (niebieska wskazuje stan układu ATX, a zielona — zasilania komputera). Płytka ATX nie ma diody HDD. Stan diod na płytce odpowiada stanowi diody zasilania na panelu komputera.

Schemat złączy 4/5:

![Złącza](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/interface.png){class="glboxshadow gl-60-desktop"}

## Instalacja {#installation}

Obejrzyj ten film lub wykonaj poniższe kroki, aby zainstalować płytkę ATX.

<iframe width="560" height="315" src="https://www.youtube.com/embed/3VEjZgzgI44" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Przykręć płytkę ATX do uchwytu {#1-screw-atx-board-and-bracket}

Przymocuj płytkę ATX do uchwytu ATX za pomocą dołączonych śrub.

![Przykręcanie płytki](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/screwing.jpg){class="glboxshadow gl-90-desktop"}

### 2. Zainstaluj płytkę ATX w obudowie komputera {#2-install-atx-board-into-pc-case}

Połącz złącza 4 i 5 odpowiednio z przewodami sterującymi i interfejsem F_PANEL sterowanego komputera.

![Podłączanie złączy](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/interface_connect.jpg){class="glboxshadow gl-90-desktop"}

Dołączony do zestawu ATX zestaw przewodów 9-PIN umożliwia połączenie jednego ze złączy 4/5 płytki ATX z przewodami sterującymi lub interfejsem F_PANEL sterowanego komputera.

Aby połączyć drugie złącze 4/5 płytki ATX z przewodami sterującymi lub interfejsem F_PANEL sterowanego komputera, użyj przewodów dołączonych do obudowy komputera.

**Uwaga**: Biegunowość złączy może różnić się w zależności od obudowy komputera. Dokładnie sprawdź ją przed instalacją.

Poniżej przedstawiono przykładowe połączenia złącza 4/5 z interfejsem F_PANEL sterowanego komputera.

??? "Złącze PANEL 10-1 pin"

    Jeśli złącze panelu sterującego na płycie głównej sterowanego komputera to PANEL 10-1 pin, jak pokazano poniżej:

    ![Złącze PANEL 10-1 pin — krok 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/10-1pin_panel_1.png){class="glboxshadow"}

    Wykonaj połączenie zgodnie z poniższym schematem. Upewnij się, że oznaczenia (np. HDDLED−, RESET SW, POWER SW, POWERLED+) są skierowane na zewnątrz i widoczne, a nie zasłonięte od wewnątrz.

    ![Złącze PANEL 10-1 pin — krok 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/10-1pin_panel_2.jpg){class="glboxshadow"}
    <small>Front View</small>

    ![Złącze PANEL 10-1 pin — krok 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/10-1pin_panel_3.jpg){class="glboxshadow"}
    <small>Rear View</small>

    Następnie użyj przewodów dołączonych do obudowy komputera, aby połączyć drugie złącze płytki ATX z przewodami sterującymi komputera.

??? "Złącze PANEL 20-5 pin"

    Jeśli złącze panelu sterującego na płycie głównej sterowanego komputera to PANEL 20-5 pin, jak pokazano poniżej:

    ![Złącze PANEL 20-5 pin — krok 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/20-5pin_panel_1.jpg){class="glboxshadow"}

    Wykonaj połączenie zgodnie z poniższym schematem. Upewnij się, że oznaczenia (np. HDDLED−, RESET SW, POWER SW, POWERLED+) są skierowane na zewnątrz i widoczne, a nie zasłonięte od wewnątrz.

    ![Złącze PANEL 20-5 pin — krok 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/20-5pin_panel_2.jpg){class="glboxshadow"}
    <small>Front View</small>

    ![Złącze PANEL 20-5 pin — krok 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/20-5pin_panel_3.png){class="glboxshadow"}
    <small>Rear View</small>

    Następnie użyj przewodów dołączonych do obudowy komputera, aby połączyć drugie złącze płytki ATX z przewodami sterującymi komputera.

??? "Złącze PANEL 20-8 pin"

    Jeśli złącze panelu sterującego na płycie głównej sterowanego komputera to PANEL 20-8 pin, jak pokazano poniżej:

    ![Złącze PANEL 20-8 pin — krok 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/20-8pin_panel_1.jpg){class="glboxshadow"}

    Wykonaj połączenie zgodnie z poniższym schematem. Upewnij się, że oznaczenia (np. HDDLED−, RESET SW, POWER SW, POWERLED+) są skierowane na zewnątrz i widoczne, a nie zasłonięte od wewnątrz.

    ![Złącze PANEL 20-8 pin — krok 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/20-8pin_panel_2.png){class="glboxshadow"}

    Następnie użyj przewodów dołączonych do obudowy komputera, aby połączyć drugie złącze płytki ATX z przewodami sterującymi komputera.

Tak wygląda ostatecznie podłączona płytka ATX.

![Podłączona płytka ATX](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/connected1.png){class="glboxshadow gl-90-desktop"}

![Podłączona płytka ATX](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/connected2.png){class="glboxshadow gl-90-desktop"}

Następnie zamontuj uchwyt płytki ATX w obudowie komputera.

![Montaż płytki ATX](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/install1.png){class="glboxshadow gl-90-desktop"}

![Montaż płytki ATX](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/install2.png){class="glboxshadow gl-90-desktop"}

### 3. Połącz płytkę ATX z urządzeniem KVM {#3-connect-atx-board-and-kvm}

Połącz port Type-C płytki ATX z portem USB-A urządzenia KVM (np. Comet GL-RM1) za pomocą dołączonego kabla USB.

![Montaż płytki ATX](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/install3.png){class="glboxshadow gl-90-desktop"}

![Montaż płytki ATX](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/install4.png){class="glboxshadow gl-90-desktop"}

Instalacja płytki ATX została zakończona.

![Montaż płytki ATX](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/install5.png){class="glboxshadow gl-90-desktop"}

Teraz możesz zalogować się do urządzenia KVM i przejść do **Accessories**, aby sterować zasilaniem ATX.

![Sterowanie zasilaniem ATX](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/atx_power.png){class="glboxshadow gl-90-desktop"}

## Często zadawane pytania {#faq}

**P1. Czy mogę używać płytki GL-ATXPC z urządzeniami KVM innych producentów niż GL.iNet?**

O1. Nie. Płytka GL-ATXPC jest akcesorium do urządzeń KVM GL.iNet i należy jej używać razem z nimi.

---

**P2. Co zrobić, jeśli po zainstalowaniu płytki ATX nie mogę sterować zasilaniem zdalnego urządzenia (włączać go i wyłączać) przez KVM?**

O2. Wypróbuj poniższe metody.

- Upewnij się, że sterowane urządzenie można normalnie włączać i wyłączać fizycznym przyciskiem zasilania na przednim panelu obudowy komputera.

- Sprawdź biegunowość połączeń. Spróbuj odwrócić wtyczkę POWER SW na płycie głównej sterowanego urządzenia, aby wykluczyć nieprawidłowe podłączenie.

    ![Biegunowość złącza](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/power-sw-connector.png){class="glboxshadow gl-90-desktop"}

- Przy podłączaniu do interfejsu F_PANEL na płycie głównej sterowanego urządzenia upewnij się, że oznaczenia (np. HDDLED−, RESET SW, POWER SW, POWERLED+) są skierowane na zewnątrz i widoczne, a nie zasłonięte od wewnątrz.

- Zaktualizuj oprogramowanie układowe urządzenia KVM.

---

**P3. Czy mogę sterować wieloma płytkami ATX za pomocą jednego urządzenia KVM GL.iNet?**

O3. Poniższe urządzenia KVM GL.iNet obsługują tylko jedną płytkę ATX.

* Comet (GL-RM1)
* Comet PoE (GL-RM1PE)
* Comet Pro (GL-RM10)
* Comet 5G (GL-RM10RC)

Model Comet X (GL-RM4PE) obsługuje jednak do czterech płytek ATX jednocześnie. Comet X ma na tylnym panelu cztery niezależne kanały. Każdy kanał zawiera port HDMI do przesyłania obrazu, port Type-C do przesyłania sygnałów klawiatury i myszy oraz port USB 2.0 do urządzeń peryferyjnych USB (np. Fingerbot lub płytka ATX).

**Uwaga**: Comet Q (GL-RMQ1) nie współpracuje z płytką ATX.

---

Masz dodatkowe pytania? Odwiedź nasze [forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
