# Co zrobić, jeśli KVM się nie włącza {#what-should-i-do-if-my-kvm-does-not-power-on}

Jeśli urządzenie KVM nie uruchamia się mimo podłączenia przewodu zasilającego, wykonaj poniższe czynności diagnostyczne.

1. Upewnij się, że przewód zasilający jest podłączony do właściwego portu USB Type-C.

    Jako przykład posłuży Comet (GL-RM1). Ma on dwa porty USB Type-C: jeden służy do zasilania (podłączenia zasilacza), a drugi do transmisji sygnału (połączenia przewodem USB z urządzeniem docelowym).

    Jeśli zamienisz te porty, KVM nie włączy się, a mysz i klawiatura nie będą reagować.

    Podłącz przewód zasilający do portu USB Type-C obok portu Ethernet.

    ![Podłączanie przewodu zasilającego](https://static.gl-inet.com/docs/kvm/faq/power_cable_connected_but_device_unpowered/plug_in_power_cable.jpg){class="glboxshadow"}

2. Do testu użyj standardowego zasilacza 5V 2A i sprawdź, czy dioda LED się zapala.

    Unikaj używania zasilaczy obsługujących protokół PD.

    Ciągłe niebieskie światło diody LED oznacza uruchamianie urządzenia.

3. Naciśnij i przytrzymaj przycisk Reset przez ponad 8 sekund, aby przywrócić ustawienia fabryczne.

---

Masz jeszcze pytania? Odwiedź nasze [forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
