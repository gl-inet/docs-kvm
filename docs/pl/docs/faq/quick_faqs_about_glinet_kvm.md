# Podstawowe pytania o GL.iNet KVM {#quick-faqs-about-glinet-kvm}

Ten krótki zbiór pytań i odpowiedzi dotyczących GL.iNet KVM pozwala szybko znaleźć odpowiedzi na częste pytania podstawowe.

## Informacje podstawowe {#basic-information}

**P1. Jakimi urządzeniami można sterować przez GL.iNet KVM?**

O1. GL.iNet KVM może sterować dowolnym urządzeniem z wyjściem HDMI i wejściem USB, np. laptopem, komputerem stacjonarnym, Raspberry Pi czy minikomputerem.

Ponadto Comet Q (GL-RMQ1) może sterować dowolnym urządzeniem, którego port USB‑C obsługuje DisplayPort Alt Mode do przesyłania obrazu; port HDMI nie jest wymagany. Dotyczy to m.in. wybranych modeli iPhone, iPad, telefonów z Androidem, MacBooków, komputerów Mac mini i większości nowoczesnych laptopów z Windows. Szczegóły znajdziesz [tutaj](../user_guide/gl-rmq1/product_overview.md#compatibility).

---

**P2. Czy trzeba zainstalować oprogramowanie, aby korzystać z GL.iNet KVM?**

O2. Na urządzeniu docelowym nie trzeba instalować żadnego oprogramowania. Może ono działać pod kontrolą Windows, macOS, ChromeOS, Linux itp.

To, czy oprogramowanie trzeba zainstalować na urządzeniu sterującym, zależy od wybranej metody dostępu do KVM.

??? "Sterowanie z bliska (tylko Comet 5G)"

    **Uwaga**: Ta metoda jest dostępna tylko w Comet 5G (GL-RM10RC).

    Comet 5G oferuje funkcję Wi-Fi Nearby Control, umożliwiającą szybkie zarządzanie lokalne bez połączeń przewodowych. Wystarczy przełączyć tryb sieci Wi-Fi Comet 5G na AP, aby urządzenie utworzyło unikatową sieć Wi-Fi (SSID). Połącz się z nią, aby bezpiecznie otworzyć konsolę Comet 5G. Szczegóły znajdziesz [tutaj](../user_guide/gl-rm10rc/quick_setup_guide.md#nearby-control).

    Włączenie trybu AP rozłącza Comet 5G z nadrzędną siecią Wi-Fi i zapewnia wyłącznie dostęp z bliska, bez połączenia z Internetem.

??? "Sterowanie lokalne (tylko Comet X)"

    **Uwaga**: Ta metoda jest dostępna tylko w Comet X (GL-RM4PE).

    Comet X ma port HDMI OUT i dwa dodatkowe porty USB, przydatne do lokalnej diagnostyki, konfiguracji i instalacji systemu operacyjnego. Podłącz monitor, mysz i klawiaturę, aby od razu sterować sprzętem lokalnie. Szczegóły znajdziesz [tutaj](../user_guide/gl-rm4pe/quick_setup_guide.md#local-control).

??? "Dostęp przez LAN"

    Jeśli chcesz uzyskać dostęp do KVM w tej samej sieci lokalnej (LAN), na urządzeniu sterującym nie trzeba instalować żadnego oprogramowania.

    Otwórz przeglądarkę na urządzeniu sterującym i wpisz adres IP KVM lub `glkvm.local` w pasku adresu, aby uzyskać dostęp lokalny.

    Szczegóły znajdziesz [tutaj](local_access_via_browser.md){target="_blank"}.

??? "Dostęp zdalny"

    - **Aplikacja GLKVM**

        Jeśli urządzenie sterujące działa pod kontrolą Windows, macOS, Androida lub iOS, możesz zainstalować na nim [aplikację GLKVM](https://www.gl-inet.com/app-rm/){target="_blank"} i uzyskać zdalny dostęp do KVM, a za jego pośrednictwem do urządzenia docelowego.

        Szczegóły znajdziesz [tutaj](remote_access_via_glkvm_app.md){target="_blank"}.

    - **Usługa chmurowa**

        Ta metoda jest odpowiednia dla osób, które nie mogą lub nie chcą instalować aplikacji GLKVM.

        Powiąż KVM z usługą chmurową, a następnie wpisz `glkvm.com` w przeglądarce urządzenia sterującego, aby uzyskać zdalny dostęp do KVM i urządzenia docelowego bez instalowania aplikacji GLKVM.

        Szczegóły znajdziesz [tutaj](remote_access_via_cloud.md){target="_blank"}.

    - **Tailscale**

        Ta metoda jest odpowiednia dla osób, które nie mogą lub nie chcą korzystać z aplikacji GLKVM ani usługi chmurowej, choć wymaga wykonania większej liczby czynności.

        Powiąż KVM i urządzenie sterujące z tym samym kontem Tailscale. Następnie wpisz wirtualny adres IP Tailscale urządzenia KVM w przeglądarce urządzenia sterującego, aby uzyskać zdalny dostęp do KVM i urządzenia docelowego.

        Szczegóły znajdziesz [tutaj](remote_access_via_tailscale.md){target="_blank"}.

    - **ZeroTier**

        Ta metoda jest odpowiednia dla osób, które nie mogą lub nie chcą korzystać z aplikacji GLKVM ani usługi chmurowej, choć wymaga wykonania większej liczby czynności.

        Dodaj KVM i urządzenie sterujące do tej samej sieci ZeroTier. Następnie wpisz adres IP ZeroTier urządzenia KVM w przeglądarce urządzenia sterującego, aby uzyskać zdalny dostęp do KVM i urządzenia docelowego.

        Szczegóły znajdziesz [tutaj](remote_access_via_zerotier.md){target="_blank"}.

    - **NetBird**

        Ta metoda jest odpowiednia dla osób, które nie mogą lub nie chcą korzystać z aplikacji GLKVM ani usługi chmurowej, choć wymaga wykonania większej liczby czynności.

        [NetBird](https://netbird.io/){target="_blank"} to otwarta platforma sieciowa oparta na zasadzie zero trust, umożliwiająca tworzenie bezpiecznych sieci prywatnych w domu i firmie. Jako sieć nakładkowa oparta na WireGuard® NetBird zapewnia bezpieczny dostęp do urządzeń z dowolnego miejsca i o dowolnej porze.

        GL.iNet KVM ma zintegrowaną obsługę NetBird, dzięki czemu możesz powiązać go z wirtualną siecią NetBird w celu uzyskania dostępu zdalnego.

        Szczegóły znajdziesz [tutaj](remote_access_via_netbird.md){target="_blank"}.

---

**P3. Jak uzyskać dostęp do GL.iNet KVM?**

O3. Do GL.iNet KVM można uzyskać dostęp lokalnie lub zdalnie na kilka sposobów:

- [Dostęp w sieci LAN przez przeglądarkę](local_access_via_browser.md){target="_blank"}
- [Dostęp zdalny przez usługę chmurową](remote_access_via_cloud.md){target="_blank"}
- [Dostęp zdalny przez aplikację GLKVM](remote_access_via_glkvm_app.md){target="_blank"}
- [Dostęp zdalny przez Tailscale](remote_access_via_tailscale.md){target="_blank"}
- [Dostęp zdalny przez ZeroTier](remote_access_via_zerotier.md){target="_blank"}
- [Dostęp zdalny przez NetBird](remote_access_via_netbird.md){target="_blank"}

Ponadto niektóre modele GL.iNet KVM obsługują Nearby Control lub Local Control, co umożliwia dostęp na miejscu bez podłączania do innego routera.

- [Sterowanie z bliska (tylko Comet 5G)](../user_guide/gl-rm10rc/quick_setup_guide.md#nearby-control){target="_blank"}
- [Sterowanie lokalne (tylko Comet X)](../user_guide/gl-rm4pe/quick_setup_guide.md#local-control){target="_blank"}

---

**P4. Czy zdalny dostęp do GL.iNet KVM wymaga otwierania portów dostępnych z sieci WAN?**

O4. Nie. Nie trzeba otwierać portów ani nawet mieć publicznego adresu IP.

---

**P5. Czy aplikacja GLKVM obsługuje ChromeOS i Linux?**

O5. Nie. Obecnie aplikacji GLKVM nie można zainstalować w systemach ChromeOS ani Linux.

Jeśli urządzenie sterujące działa pod kontrolą ChromeOS lub Linux, nie można zainstalować na nim aplikacji GLKVM, więc zdalny dostęp do urządzenia docelowego przez tę aplikację nie jest obsługiwany.

Możesz jednak skorzystać z <u>usługi chmurowej</u>, <u>Tailscale</u>, <u>ZeroTier</u> lub <u>NetBird</u>, aby uzyskać dostęp zdalny. Szczegóły znajdziesz w pytaniu P3 powyżej.

Możesz też uzyskać lokalny dostęp do KVM przez przeglądarkę. Szczegóły znajdziesz w pytaniu P3 powyżej.

---

**P6. Czy Comet (GL-RM1) może łączyć się z siecią bezprzewodową?**

O6. Nie. Comet (GL-RM1) nie obsługuje połączenia z siecią bezprzewodową.

Aby uzyskać dostęp do Internetu, trzeba podłączyć go do urządzenia sieciowego (np. routera) przewodem Ethernet.

Jeśli potrzebujesz KVM z obsługą Wi-Fi, możesz rozważyć następujące modele:

* [Comet Pro (GL-RM10)](https://www.gl-inet.com/products/gl-rm10/){target="_blank"}
* [Comet 5G (GL-RM10RC)](https://www.gl-inet.com/products/gl-rm10rc/){target="_blank"}
* [Comet Q (GL-RMQ1)](https://www.gl-inet.com/products/gl-rmq1/){target="_blank"}

---

## Sterowanie zasilaniem {#power-control}

**P1. Czy GL.iNet KVM może zdalnie włączać i wyłączać urządzenie docelowe?**

O1. GL.iNet KVM umożliwia zdalne włączanie i wyłączanie urządzenia docelowego następującymi metodami:

- Wake-on-LAN (wbudowana usługa programowa)

- [Płytka ATX](../user_guide/gl-atx-board/index.md){target="_blank"} (sprzedawana oddzielnie; nie działa z Comet Q).

- [FingerBot](../user_guide/gl-fgb-01/index.md){target="_blank"} (sprzedawany oddzielnie; nie działa z Comet Q).

---

**P2. Jak używać płytki ATX do zdalnego sterowania zasilaniem?**

O2. Zobacz [instrukcję obsługi płytki ATX](../user_guide/gl-atx-board/index.md){target="_blank"}.

---

## Funkcje {#features}

!!! Tip

    Poniżej znajdują się odpowiedzi na pytania dotyczące kilku popularnych funkcji. Pełny opis funkcji znajdziesz w odpowiedniej [instrukcji obsługi](../user_guide/index.md).

**P1. Czy muszę korzystać z usługi KVM Cloud?**

O1. Nie. Korzystanie z usługi chmurowej jest opcjonalne.

Jeśli nie korzystasz z chmury do dostępu zdalnego, możesz użyć narzędzi sieci nakładkowych innych firm, takich jak Tailscale, ZeroTier i NetBird.

---

**P2. Czy jednym GL.iNet KVM można sterować wieloma urządzeniami?**

O2. Następujące urządzenia GL.iNet KVM mogą sterować tylko jednym urządzeniem docelowym:

* Comet (GL-RM1)
* Comet PoE (GL-RM1PE)
* Comet Pro (GL-RM10)
* Comet 5G (GL-RM10RC)
* Comet Q (GL-RMQ1)

Comet X (GL-RM4PE) można natomiast podłączyć jednocześnie do maksymalnie czterech urządzeń docelowych, choć w danej chwili można sterować tylko jednym z nich. Między czterema podłączonymi urządzeniami możesz szybko przełączać się przyciskiem na panelu przednim na miejscu lub przez konsolę zdalną, gdy jesteś poza miejscem instalacji.

Comet X (GL-RM4PE) ma cztery niezależne kanały na panelu tylnym. Każdy kanał ma port HDMI do przesyłania obrazu, port Type-C do przesyłania sygnałów klawiatury i myszy oraz port USB 2.0 do urządzeń peryferyjnych USB (np. Fingerbot lub płytki ATX).

---

**P3. Co to jest Wake-on-LAN?**

O3. Wake-on-LAN (WOL) to technologia umożliwiająca zdalne włączenie komputera lub urządzenia albo wybudzenie go ze stanu niskiego poboru energii przez sieć. Polega na wysłaniu „magicznego pakietu” zawierającego adres MAC urządzenia docelowego, co powoduje jego uruchomienie. Typowe zastosowania obejmują zdalną administrację, energooszczędne konfiguracje czuwania i scentralizowane zarządzanie systemami.

---

**P4. Czy GL.iNet KVM obsługuje Mouse Jiggle?**

O4. Tak. Możesz włączyć Mouse Jiggle w konsoli KVM.

Funkcja Mouse Jiggler symuluje niewielkie, okresowe ruchy myszy, aby zapobiec uśpieniu komputera (urządzenia docelowego) wskutek dłuższej bezczynności, np. podczas spotkań zdalnych i zarządzania serwerami.

---

**P5. Czy GL.iNet KVM obsługuje dźwięk dwukierunkowy?**

O5. Tak. Możesz włączyć Speaker i Microphone w konsoli KVM, aby uzyskać dwukierunkową transmisję dźwięku.

---

Masz jeszcze pytania? Odwiedź nasze [forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
