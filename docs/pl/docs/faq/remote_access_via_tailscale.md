# Jak uzyskać zdalny dostęp do KVM przez Tailscale {#how-to-access-kvm-remotely-via-tailscale}

GL.iNet KVM ma zintegrowaną obsługę Tailscale, dzięki czemu możesz powiązać go z wirtualną siecią Tailscale w celu uzyskania dostępu zdalnego, bez instalacji aplikacji GLKVM ani korzystania z usługi chmurowej. Jest to szczególnie przydatne, gdy urządzenie sterujące nie działa pod kontrolą Windows, macOS, Androida ani iOS (więc nie można na nim zainstalować aplikacji GLKVM) lub gdy nie chcesz korzystać z aplikacji GLKVM ani usługi chmurowej.

Wykonaj poniższe czynności, aby uzyskać zdalny dostęp do GL.iNet KVM przez Tailscale.

## Powiązanie KVM z Tailscale {#bind-kvm-to-tailscale}

**Przed rozpoczęciem podłącz KVM i urządzenie sterujące do tej samej sieci lokalnej.**

1. Otwórz przeglądarkę na urządzeniu sterującym. Zalecamy Chrome lub Edge ze względu na lepszą zgodność.

2. Zaloguj się lokalnie do konsoli KVM za pomocą nazwy domeny lub adresu IP. W tym przykładzie użyjemy domyślnej domeny.

    Wpisz `glkvm.local` w pasku adresu. Nastąpi przekierowanie do strony logowania GLKVM. Wpisz hasło administratora.

    ![Dostęp lokalny za pomocą nazwy domeny](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_1.png){class="glboxshadow"}

3. Po zalogowaniu przejdź do **Apps Center** -> **Tailscale**. Włącz Tailscale i kliknij **Bind Device**.

    ![Włączanie Tailscale](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/enable_tailscale.png){class="glboxshadow"}

4. Nastąpi przekierowanie do strony logowania Tailscale. Wpisz adres e-mail, aby się zalogować.

    ![Logowanie do Tailscale](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/log_in_tailscale.png){class="glboxshadow"}

5. Po zalogowaniu strona poinformuje o zamiarze połączenia urządzenia glkvm z Twoją siecią tailnet. Kliknij **Connect**.

    ![Łączenie KVM z siecią tailnet](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/connect_kvm_to_tailscale.png){class="glboxshadow"}

    Urządzenie KVM zostanie powiązane z siecią tailnet.

    ![KVM został powiązany](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/bind_kvm_successful.png){class="glboxshadow"}

6. Nastąpi przekierowanie do konsoli Tailscale, gdzie w sekcji **Machines** będzie widoczne urządzenie o nazwie **glkvm**.

    ![Konsola Tailscale z urządzeniem KVM](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/tailscale_panel_1.png){class="glboxshadow"}

## Powiązanie urządzenia sterującego {#bind-the-controlling-device}

Poniższy przykład pokazuje, jak powiązać laptop z Windows, pełniący rolę urządzenia sterującego, z siecią Tailscale.

1. Zainstaluj na laptopie Tailscale, pobierając go [tutaj](https://tailscale.com/download){target="_blank"}.

2. Uruchom Tailscale na laptopie i zaloguj się za pomocą tego samego adresu e-mail.

    ![Logowanie do Tailscale](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/log_in_tailscale.png){class="glboxshadow"}

3. Po zalogowaniu strona poinformuje o zamiarze połączenia laptopa (urządzenia sterującego) z Twoją siecią tailnet. Kliknij **Connect**.

    ![Łączenie komputera z siecią tailnet](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/connect_pc_to_tailscale.png){class="glboxshadow"}

    Laptop zostanie powiązany z siecią tailnet.

    ![Komputer został powiązany](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/bind_pc_successful.png){class="glboxshadow"}

4. Nastąpi przekierowanie do konsoli Tailscale, gdzie urządzenie sterujące także będzie widoczne w sekcji **Machines**.

    ![Konsola Tailscale z oboma urządzeniami](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/tailscale_panel_2.png){class="glboxshadow"}

## Dostęp zdalny przez Tailscale {#remote-access-via-tailscale}

W konsoli Tailscale kliknij **Address** urządzenia glkvm (w tym przykładzie `100.104.185.26`).

![Odczytywanie wirtualnego adresu IP](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/get_vitual_ip.png){class="glboxshadow"}

Zobaczysz cztery wartości:

- glkvm (nazwa urządzenia)
- glkvm.tail1fd0.ts.net (domena przydzielona przez Tailscale)
- fd7a:115c:a1e0:301:b92f (wirtualny adres IPv6)
- 100.104.185.26 (wirtualny adres IPv4).

Są one przydzielane przez Tailscale do identyfikacji urządzenia i komunikacji w sieci wirtualnej. Możesz uzyskać zdalny dostęp do KVM za pomocą domeny przydzielonej przez Tailscale, wirtualnego adresu IPv4 lub wirtualnego adresu IPv6.

Jako przykład posłuży wirtualny adres IPv4.

1. Skopiuj wirtualny adres IPv4 urządzenia KVM.

2. Otwórz nową kartę i wklej adres IP w pasku adresu.

    ![Dostęp za pomocą wirtualnego adresu IP](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/enter_vitual_ip.png){class="glboxshadow"}

    Może pojawić się ostrzeżenie o prywatności. [Dlaczego pojawia się to ostrzeżenie?](privacy_error_from_your_browser.md){target="_blank"}

    ![Ostrzeżenie o prywatności](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/privacy_error.png){class="glboxshadow"}

    Kliknij **Advanced**, a następnie **Proceed to 100.104.185.26**. Nastąpi przekierowanie do strony logowania GLKVM.

    ![Kontynuowanie mimo ostrzeżenia](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/proceed.png){class="glboxshadow"}

3. Wpisz hasło administratora, aby się zalogować. Możesz teraz uzyskać dostęp do GL.iNet KVM i urządzenia docelowego przez wirtualny adres IP Tailscale.

    ![Dostęp zdalny został nawiązany](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/remote_access_via_tailscale.png){class="glboxshadow"}

---

Masz jeszcze pytania? Odwiedź nasze [forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
