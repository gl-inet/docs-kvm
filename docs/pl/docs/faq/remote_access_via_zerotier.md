# Jak uzyskać zdalny dostęp do KVM przez ZeroTier {#how-to-access-kvm-remotely-via-zerotier}

> Uwaga: Przed użyciem tej funkcji zaktualizuj oprogramowanie sprzętowe KVM do wersji v1.8.0.

GL.iNet KVM ma zintegrowaną obsługę ZeroTier, dzięki czemu możesz powiązać go z siecią ZeroTier w celu uzyskania dostępu zdalnego, bez instalacji aplikacji GLKVM ani korzystania z usługi chmurowej.

Wykonaj poniższe czynności, aby uzyskać zdalny dostęp do GL.iNet KVM przez ZeroTier.

## Włączenie ZeroTier {#enable-zerotier}

**Przed rozpoczęciem podłącz KVM i urządzenie sterujące do tej samej sieci lokalnej.**

1. Otwórz przeglądarkę na urządzeniu sterującym. Zalecamy Chrome lub Edge ze względu na lepszą zgodność.

2. Zaloguj się lokalnie do konsoli KVM za pomocą nazwy domeny lub adresu IP. W tym przykładzie użyjemy lokalnego adresu IP.

    Wpisz **adres IP KVM w sieci LAN** (widoczny na ekranie dotykowym lub na routerze) w pasku adresu. Nastąpi przekierowanie do strony logowania GLKVM. Wpisz hasło administratora.

    ![Dostęp lokalny za pomocą adresu IP](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/1_local_access.png){class="glboxshadow"}

3. Po zalogowaniu przejdź do **Apps Center** -> **ZeroTier**. Włącz ZeroTier. Zobaczysz żółty komunikat pokazany poniżej.

    Kliknij odnośnik lub otwórz [tę stronę](https://my.zerotier.com/){target="_blank"}, aby zalogować się do ZeroTier Central i utworzyć sieć ZeroTier.

    ![Włączanie ZeroTier](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/2_enable_zerotier.png){class="glboxshadow"}

## Powiązanie KVM z ZeroTier {#bind-kvm-to-zerotier}

1. Przy pierwszym logowaniu do [ZeroTier](https://my.zerotier.com/){target="_blank"} może być konieczne wybranie wersji ZeroTier Central.

    ![Wybór wersji Central](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/3_select_central.png){class="glboxshadow"}

    Wybierz odpowiednią wersję, aby kontynuować. W tym przykładzie użyjemy **New Central**.

    Zaloguj się za pomocą adresu e-mail i hasła. Jeśli nie masz konta, najpierw je utwórz.

    ![Logowanie do ZeroTier](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/4_zerotier_signin.png){class="glboxshadow"}

2. Po zalogowaniu utwórz organizację.

    ![Tworzenie organizacji](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/5_create_org.png){class="glboxshadow"}

3. Wybierz plan. W tym przykładzie wybieramy **Personal**, który obejmuje 10 urządzeń, 1 administratora sieci i 1 sieć. Jeśli potrzebujesz więcej sieci lub urządzeń albo niestandardowych tras i DNS, wybierz plan Essential lub Scale.

    ![Wybór planu](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/6_select_plan.png){class="glboxshadow"}

4. Sieć ZeroTier została utworzona. Skopiuj **Network ID**, czyli 16-znakowy ciąg liter i cyfr. Będzie potrzebny później podczas dodawania urządzeń do sieci ZeroTier. Pozostaw tę kartę otwartą.

    ![Identyfikator sieci](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/7_copy_network_id.png){class="glboxshadow"}

5. Wróć do konsoli KVM i przejdź do **Apps Center** -> **ZeroTier**. Znajdź **Network ID** i kliknij **Set**.

    ![Identyfikator sieci](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/8_set_network_id1.png){class="glboxshadow"}

    W wyświetlonym oknie wklej **Network ID** i kliknij **Confirm**.

    ![Identyfikator sieci](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/8_set_network_id2.png){class="glboxshadow"}

    W konsoli pojawi się żółty komunikat informujący, że urządzenie wymaga autoryzacji.

    ![Urządzenie oczekujące na autoryzację](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/9_authorize1.png){class="glboxshadow"}

6. Wróć do ZeroTier Central. Zobaczysz urządzenie (Twój KVM) oczekujące na zatwierdzenie. Kliknij **Authorize**.

    ![Autoryzowanie urządzenia](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/9_authorize2.png){class="glboxshadow"}

    Po autoryzacji status zmieni się na zielony Authorized, jak pokazano poniżej.

    ![Urządzenie zostało autoryzowane w ZeroTier](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/10_authorized1.png){class="glboxshadow"}

    W konsoli KVM możesz też sprawdzić **Network ID** i **Virtual IP**, jak pokazano poniżej.

    ![Autoryzowane urządzenie w konsoli KVM](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/10_authorized2.png){class="glboxshadow"}

## Powiązanie urządzenia sterującego {#bind-the-controlling-device}

Poniższy przykład pokazuje, jak powiązać laptop z Windows, pełniący rolę urządzenia sterującego, z siecią ZeroTier.

1. Zainstaluj na laptopie ZeroTier, pobierając go [tutaj](https://www.zerotier.com/download/){target="_blank"}.

2. Uruchom ZeroTier na laptopie i dodaj go do tej samej sieci ZeroTier.

    ZeroTier nie wyświetla osobnego okna ani interfejsu na pulpicie. Działa jako ikona w zasobniku systemowym (w prawym dolnym rogu), a wszystkie operacje wykonuje się przez menu dostępne po kliknięciu prawym przyciskiem myszy.

    Kliknij prawym przyciskiem ikonę ZeroTier i wybierz **Join New Network**. W wyświetlonym oknie wpisz ten sam **Network ID**, aby dodać komputer do tej samej sieci ZeroTier.

    ![Dołączanie do sieci](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/11_pc_join_network.jpg){class="glboxshadow"}

    Następnie przejdź do ZeroTier Central, znajdź urządzenie ze statusem Pending i autoryzuj je.

    ![Autoryzacja](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/12_authorize.png){class="glboxshadow"}

3. Po autoryzacji status zmieni się na zielony Authorized, jak pokazano poniżej.

    ![Urządzenie zostało autoryzowane](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/13_authorized.png){class="glboxshadow"}

4. KVM i laptop są teraz dodane do tej samej sieci ZeroTier. Możesz to potwierdzić na podstawie ich Network ID, jak pokazano poniżej.

    ![Urządzenia w tej samej sieci ZeroTier](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/14_same_zt_network.png){class="glboxshadow"}

## Dostęp zdalny przez ZeroTier {#remote-access-via-zerotier}

Poniższy przykład pokazuje, jak uzyskać zdalny dostęp do konsoli KVM za pomocą adresu IP ZeroTier.

1. Na laptopie zaloguj się do ZeroTier Central na swoje konto, znajdź urządzenie KVM i kliknij jego **ZT IP**, aby skopiować adres.

    ![Adres IP ZeroTier](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/15_zerotier_ip.png){class="glboxshadow"}

2. Otwórz nową kartę przeglądarki, wklej skopiowany adres IP ZeroTier w pasku adresu i naciśnij Enter. Nastąpi przekierowanie do strony logowania GLKVM.

    Wpisz hasło administratora, aby się zalogować. Możesz teraz uzyskać dostęp do GL.iNet KVM i urządzenia docelowego przez adres IP ZeroTier.

    ![Dostęp zdalny](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/16_remote_access.png){class="glboxshadow"}

    **Wskazówka**: Przy pierwszym otwarciu tego adresu IP ZeroTier może pojawić się ostrzeżenie o prywatności. Kliknij **Advanced** -> **Proceed**, aby kontynuować. Szczegóły znajdziesz w artykule [Ostrzeżenie o prywatności w przeglądarce](privacy_error_from_your_browser.md){target="_blank"}.

---

Masz jeszcze pytania? Odwiedź nasze [forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
