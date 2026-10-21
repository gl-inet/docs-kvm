# Vad gör jag om min KVM inte startar? {#what-should-i-do-if-my-kvm-does-not-power-on}

Om KVM-enheten inte startar trots att strömkabeln är ansluten kan du felsöka med hjälp av följande metoder.

1. Kontrollera att strömkabeln är ansluten till rätt USB Type-C-port.

    Vi tar Comet (GL-RM1) som exempel. Den har två USB Type-C-portar: en för strömförsörjning (ansluts till en nätadapter) och en för signalöverföring (ansluts till den styrda enheten med en USB-kabel).

    Om de två portarna förväxlas startar inte KVM-enheten, och mus och tangentbord svarar inte på inmatning.

    Anslut strömkabeln till den USB Type-C-port som sitter bredvid Ethernet-porten.

    ![Anslut strömkabeln](https://static.gl-inet.com/docs/kvm/faq/power_cable_connected_but_device_unpowered/plug_in_power_cable.jpg){class="glboxshadow"}

2. Testa med en vanlig nätadapter på 5V 2A och kontrollera om lysdioden tänds.

    Undvik nätadaptrar med PD-protokoll.

    En lysdiod med fast blått sken anger att enheten startar.

3. Håll återställningsknappen (Reset) intryckt i mer än 8 sekunder för att återställa fabriksinställningarna.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
