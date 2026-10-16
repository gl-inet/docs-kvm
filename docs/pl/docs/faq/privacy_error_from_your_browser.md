# Ostrzeżenie o prywatności podczas dostępu do KVM przez przeglądarkę {#privacy-error-when-accessing-kvm-via-browser}

Podczas dostępu do GL.iNet KVM przez przeglądarkę może pojawić się ostrzeżenie: **Your connection isn't private**.

![Ostrzeżenie o prywatności](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/privacy_error_1.png){class="glboxshadow"}

Oznacza ono, że przeglądarka nie może zweryfikować certyfikatu SSL/TLS przedstawionego przez KVM. Na przykład certyfikat może nie pochodzić od urzędu certyfikacji zaufanego przez przeglądarkę lub nie odpowiadać adresowi IP albo nazwie hosta użytej do otwarcia konsoli.

## Dlaczego pojawia się to ostrzeżenie? {#why-do-i-get-this-warning}

W powyższym przykładzie **192.168.8.11** jest lokalnym adresem IP KVM, przydzielonym dynamicznie przez router nadrzędny za pomocą DHCP.

!!! Note

    Jeśli adres bramy routera, do którego podłączono GL.iNet KVM, ma postać „192.168.x.1” (gdzie x w sieciach prywatnych to zwykle 0, 1 lub 8), lokalny adres IP KVM powinien mieć postać „192.168.x.y” (gdzie y jest prawidłowym adresem hosta w podsieci).

Ten lokalny adres IP służy do otwierania konsoli GL.iNet KVM, a nie publicznej witryny internetowej.

KVM używa domyślnego certyfikatu TLS do dostępu przez HTTPS w przeglądarce. Przeglądarki weryfikują certyfikaty konsol lokalnych tak samo jak certyfikaty publicznych stron: certyfikat musi być zaufany, ważny i zgodny z adresem, pod którym uzyskuje się dostęp.

Jeśli przeglądarka nie ufa domyślnemu certyfikatowi lub certyfikat nie obejmuje podanego lokalnego adresu IP albo nazwy hosta, pojawia się ostrzeżenie. Nie oznacza ono, że KVM nie ma certyfikatu. HTTPS może nadal szyfrować połączenie, ale przeglądarka nie może potwierdzić tożsamości KVM.

## Jak rozwiązać problem z ostrzeżeniem? {#how-to-resolve-the-warning}

Przy dostępie lokalnym najpierw upewnij się, że adres należy do Twojego KVM. Następnie kliknij **Advanced** i **Continue to "192.168.8.11"** (dokładna treść zależy od przeglądarki).

![Przejście do 192.168.8.11](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/privacy_error_2.jpg){class="glboxshadow"}

Nastąpi przekierowanie do konsoli GL.iNet KVM.

![Lokalny dostęp do konsoli administracyjnej KVM](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/local_access.png){class="glboxshadow"}

## Czy mogę użyć własnego certyfikatu? {#can-i-use-my-own-certificate}

Tak. Na KVM można zainstalować i używać własnego certyfikatu SSL/TLS. Wykonaj poniższe czynności.

1. Uzyskaj certyfikat SSL/TLS obejmujący nazwę hosta lub adres IP, pod którym uzyskujesz dostęp do KVM. Aby uniknąć ostrzeżeń przeglądarki, certyfikat musi być ważny i wystawiony przez zaufany urząd certyfikacji. Certyfikat z podpisem własnym nadal będzie powodował ostrzeżenie, chyba że jawnie skonfigurujesz urządzenie sterujące, aby mu ufało.

2. Zaloguj się do konsoli KVM. Kliknij ikonę tarczy w prawym górnym rogu, aby przejść do **Security** -> **TLS Certificate**.

    ![Własny certyfikat — krok 1](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/custom_cert1.png){class="glboxshadow"}

    W wyświetlonym oknie wybierz **Custom Certificate**, a następnie prześlij plik certyfikatu i klucz prywatny. Ta funkcja jest dostępna od wersji oprogramowania sprzętowego v1.8.0.

    ![Własny certyfikat — krok 2](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/custom_cert2.png){class="glboxshadow"}

    Możesz też zastąpić certyfikat i klucz prywatny na KVM przez terminal SSH lub WinSCP. Certyfikat i klucz znajdują się w katalogu:

    `/etc/kvmd/user/ssl`

    Zastąp je nowym certyfikatem SSL i kluczem prywatnym.

---

Masz jeszcze pytania? Odwiedź nasze [forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
