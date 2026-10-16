# Jak uzyskać dostęp do konsoli szeregowej przez USB TTL

Aby użyć adaptera USB TTL do debugowania przez port szeregowy, wykonaj poniższe kroki:

1. Podłącz adapter USB TTL do portu USB urządzenia KVM.
2. Uruchom następujące polecenie, aby otworzyć połączenie z portem szeregowym:

```bash
minicom -D /dev/ttyUSB0 -b 115200
```

Polecenie nawiązuje połączenie szeregowe z `/dev/ttyUSB0` z szybkością transmisji `115200` bodów.

---

Masz pytania? Odwiedź nasze [forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
