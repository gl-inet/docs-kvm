# Jak uzyskać zdalny dostęp do KVM przez NetBird {#how-to-access-kvm-remotely-via-netbird}

> Uwaga: Przed użyciem tej funkcji zaktualizuj oprogramowanie sprzętowe KVM do wersji v1.9.0.

[NetBird](https://netbird.io/){target="_blank"} to otwarta platforma sieciowa oparta na zasadzie zero trust, umożliwiająca tworzenie bezpiecznych sieci prywatnych w domu i firmie. Jako sieć nakładkowa oparta na WireGuard® NetBird zapewnia bezpieczny dostęp do urządzeń z dowolnego miejsca i o dowolnej porze.

GL.iNet KVM ma zintegrowaną obsługę NetBird, dzięki czemu możesz powiązać go z wirtualną siecią NetBird w celu uzyskania dostępu zdalnego, bez instalacji aplikacji GLKVM ani korzystania z usługi chmurowej.

Wykonaj poniższe czynności, aby uzyskać zdalny dostęp do GL.iNet KVM przez NetBird.

## Powiązanie KVM z NetBird {#bind-kvm-to-netbird}

**Przed rozpoczęciem podłącz KVM i urządzenie sterujące do tej samej sieci lokalnej.**

1. Zaloguj się lokalnie do konsoli KVM za pomocą nazwy domeny lub adresu IP, następnie przejdź do **Apps Center** -> **NetBird**. Włącz NetBird i kliknij **Bind Device**.

    ![Powiązanie urządzenia](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/1-bind-device.png){class="glboxshadow"}

2. Nastąpi przekierowanie do strony potwierdzenia urządzenia. Kliknij **Confirm**.

    ![Potwierdzanie urządzenia](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/2-confirm.png){class="glboxshadow"}

3. Zaloguj się na konto NetBird. Jeśli nie masz konta, najpierw je utwórz.

    ![Logowanie do NetBird](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/3-signin.png){class="glboxshadow"}

4. Po zalogowaniu urządzenie KVM zostanie automatycznie powiązane z kontem.

    ![KVM jest połączony](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/4-connected.png){class="glboxshadow"}

    W panelu NetBird urządzenie KVM będzie też widoczne na stronie **Peers**.

    ![Panel NetBird](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/5-dashboard.png){class="glboxshadow"}

## Powiązanie urządzenia sterującego {#bind-the-controlling-device}

Poniższy przykład pokazuje, jak powiązać laptop z Windows, pełniący rolę urządzenia sterującego, z siecią NetBird.

1. Zainstaluj na laptopie NetBird, pobierając go [tutaj](https://app.netbird.io/install){target="_blank"}.

    ![Instalacja NetBird](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/6-install.png){class="glboxshadow"}

2. Uruchom NetBird na laptopie i dodaj go do tej samej sieci NetBird.

    NetBird nie wyświetla osobnego okna ani interfejsu na pulpicie. Działa jako ikona w zasobniku systemowym (w prawym dolnym rogu), a wszystkie operacje wykonuje się przez menu dostępne po kliknięciu prawym przyciskiem myszy.

    Kliknij prawym przyciskiem ikonę NetBird i wybierz **Connect**.

    ![Łączenie komputera](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/7-pc-connect.png){class="glboxshadow gl-50-desktop"}

3. W wyświetlonym oknie kliknij **Accept**, aby udzielić uprawnienia.

    ![Autoryzacja](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/8-authorize.png){class="glboxshadow"}

    Laptop zostanie automatycznie powiązany z kontem i dodany do tej samej sieci NetBird.

    ![Komputer jest połączony](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/9-login-success.png){class="glboxshadow"}

4. W panelu NetBird na stronie **Peers** będą widoczne dwa urządzenia: KVM i laptop sterujący.

    ![Panel NetBird](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/10-dashboard.png){class="glboxshadow"}

## Dostęp zdalny przez NetBird {#remote-access-via-netbird}

Poniższy przykład pokazuje, jak uzyskać zdalny dostęp do konsoli KVM za pomocą wirtualnego adresu IP NetBird.

1. Na laptopie zaloguj się do panelu NetBird i przejdź do **Peers**.

    Znajdź urządzenie KVM i kliknij jego **NetBird IP** (w tym przykładzie `100.100.141.229`), aby skopiować wirtualny adres IP.

    ![Adres IP NetBird urządzenia KVM](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/11-kvm-netbird-ip.png){class="glboxshadow"}

    Najedź kursorem na adres IP, aby wyświetlić więcej szczegółów, takich jak publiczny adres IP, domena i region.

2. Otwórz nową kartę przeglądarki, wklej skopiowany adres IP NetBird w pasku adresu i naciśnij Enter. Nastąpi przekierowanie do strony logowania GLKVM.

    ![Logowanie do dostępu zdalnego](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/12-ip-login.png){class="glboxshadow"}

    Wpisz hasło administratora, aby się zalogować. Możesz teraz uzyskać dostęp do GL.iNet KVM i urządzenia docelowego przez adres IP NetBird.

    ![Dostęp zdalny został nawiązany](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/12-ip-access.png){class="glboxshadow"}

    **Wskazówka**: Przy pierwszym otwarciu tego adresu IP NetBird może pojawić się ostrzeżenie o prywatności. Kliknij **Advanced** -> **Proceed**, aby kontynuować. Szczegóły znajdziesz w artykule [Ostrzeżenie o prywatności w przeglądarce](privacy_error_from_your_browser.md){target="_blank"}.

---

Masz jeszcze pytania? Odwiedź nasze [forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
