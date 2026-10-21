# Jak wyłączyć wysyłanie pakietów PING/ICMP z KVM {#how-to-disable-outgoing-pingicmp-packets-from-kvm}

Urządzenie KVM okresowo wysyła pakiety PING (ICMP), aby sprawdzać łączność sieciową. Ten dokument wyjaśnia, jak wyłączyć tę funkcję i jakie są tego skutki uboczne.

## Urządzenia obsługujące wyłącznie Ethernet {#for-ethernet-only-devices}

W urządzeniach z samym połączeniem Ethernet, takich jak Comet (GL-RM1) i Comet PoE (GL-RM1PE), system wysyła pakiety PING do bramy domyślnej, aby sprawdzić dostęp do internetu. Wynik jest sygnalizowany stanem diody LED.

Aby tymczasowo wyłączyć tę funkcję, uruchom poniższe polecenie:

```bash
/etc/init.d/S23led stop
```

> **Uwaga:** Wyłączenie tej usługi spowoduje również wyłączenie **przycisku Reset**.

## Urządzenia obsługujące Ethernet i Wi-Fi {#for-devices-with-both-ethernet-and-wi-fi}

W urządzeniach wyposażonych w Ethernet i Wi-Fi system wysyła pakiety PING do publicznych serwerów DNS, aby sprawdzać dostęp do internetu na każdym interfejsie sieciowym. Mechanizm ten służy do dynamicznego przełączania awaryjnego między łączami WAN i umożliwia przełączenie na Wi-Fi, gdy połączenie Ethernet utraci dostęp do internetu.

Aby tymczasowo wyłączyć tę funkcję, uruchom poniższe polecenie:

```bash
/etc/init.d/S98multi-wan stop
```

---

Masz pytania? Odwiedź nasze [forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
