# Jak zmniejszyć częstotliwość wykrywania publicznego adresu IP przez STUN {#how-to-reduce-stun-public-ip-detection-frequency}

Urządzenie KVM używa żądań STUN do wykrywania publicznego adresu IP na potrzeby zdalnego dostępu. Domyślnie wysyła je w regularnych odstępach czasu. Jeśli uzyskujesz dostęp do KVM wyłącznie przez sieć lokalną lub VPN, możesz zmienić konfigurację, aby zmniejszyć częstotliwość żądań STUN.

Zaloguj się do KVM przez SSH lub otwórz **Toolbox** > **Terminal** w konsoli KVM. Przed edycją utwórz kopię zapasową istniejącego pliku nadpisań konfiguracji:

```bash
cp -p /etc/kvmd/override.yaml /etc/kvmd/override.yaml.bak
vi /etc/kvmd/override.yaml
```

Jeśli kopia `override.yaml.bak` już istnieje, wybierz inną nazwę pliku kopii, aby jej nie nadpisać. Jeśli plik `override.yaml` nie istnieje, pomiń polecenie tworzenia kopii i utwórz plik w edytorze.

Dodaj poniższe ustawienie do pliku, zachowując wszystkie dotychczasowe nadpisania:

```yaml
janus:
    check:
        retries: 10000
```

Jeśli sekcja `janus` już istnieje, dodaj lub zaktualizuj `check.retries` w tej sekcji. Jeśli pod `janus` jest już sekcja `check`, zaktualizuj w niej wartość `retries` lub dodaj ją w tym miejscu. Nie twórz zduplikowanych kluczy `janus` ani `check`. Do wcięć w YAML używaj spacji. Po zakończeniu zapisz plik.

> **Uwaga:** Ta konfiguracja znacznie zmniejsza liczbę żądań STUN inicjowanych przez Janus. Może jednak obniżyć skuteczność przebijania NAT za pomocą STUN przy dostępie z sieci zewnętrznej. **Stosuj ją tylko wtedy, gdy uzyskujesz dostęp do KVM wyłącznie przez sieć lokalną lub VPN.**

---

Masz pytania? Odwiedź nasze [forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
