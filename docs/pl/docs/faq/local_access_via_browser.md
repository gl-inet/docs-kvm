# Jak uzyskać lokalny dostęp do KVM przez przeglądarkę {#how-to-access-the-kvm-locally-via-browser}

Przed rozpoczęciem upewnij się, że urządzenie sterujące i KVM znajdują się w tej samej sieci LAN.

Lokalny dostęp do KVM przez przeglądarkę można uzyskać na dwa sposoby: za pomocą nazwy domeny lub adresu IP.

## Dostęp lokalny za pomocą nazwy domeny {#local-access-via-domain}

1. Otwórz przeglądarkę na urządzeniu sterującym. Zalecamy Chrome lub Edge ze względu na lepszą zgodność.

2. Wpisz `glkvm.local` w pasku adresu. Nastąpi przekierowanie do strony logowania GLKVM. Wpisz hasło administratora.

    ![Dostęp lokalny za pomocą nazwy domeny](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_1.png){class="glboxshadow"}

    Możesz teraz uzyskać lokalny dostęp do konsoli KVM, a za jej pośrednictwem do urządzenia docelowego.

    ![Dostęp lokalny za pomocą nazwy domeny](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_2.jpg){class="glboxshadow"}

## Dostęp lokalny za pomocą adresu IP {#local-access-via-ip-address}

Znajdź adres IP KVM w sieci nadrzędnej (np. na routerze) i wpisz go w przeglądarce. Uzyskasz lokalny dostęp do KVM, a za jego pośrednictwem do urządzenia docelowego.

Jako przykład posłużą router **GL-AXT1800** i KVM **GL-RM1 Comet**: Comet jest podłączony przewodem Ethernet do portu LAN routera GL-AXT1800. Urządzenie docelowe jest prawidłowo podłączone do Comet przewodami HDMI i USB.

Aby uzyskać dostęp do konsoli KVM, wykonaj poniższe czynności.

1. Zaloguj się do panelu administracyjnego WWW GL-AXT1800. Router musi być skonfigurowany do dostępu do Internetu.

    ![Logowanie do routera](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/log_in_router.png){class="glboxshadow"}

2. W panelu administracyjnym routera przejdź do **Client** i znajdź adres IP Comet na liście klientów. W poniższym przykładzie adres IP Comet to **192.168.8.197**.

    ![Wyszukiwanie adresu IP GLKVM](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/find_glkvm_ip.png){class="glboxshadow"}

3. Otwórz nową kartę w przeglądarce i wpisz adres IP Comet **192.168.8.197** w pasku adresu.

    Nastąpi przekierowanie do strony logowania GLKVM. Wpisz hasło administratora.

    ![Dostęp lokalny za pomocą adresu IP](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_1.jpg){class="glboxshadow"}

    Możesz teraz uzyskać lokalny dostęp do konsoli KVM, a za jej pośrednictwem do urządzenia docelowego.

    ![Dostęp lokalny za pomocą adresu IP](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_2.jpg){class="glboxshadow"}

---

Masz jeszcze pytania? Odwiedź nasze [forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
