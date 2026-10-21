# Vad gör jag om jag inte kan styra musen och tangentbordet? {#what-should-i-do-if-i-cannot-control-the-mouse-and-keyboard}

Om du inte kan styra musen och tangentbordet på den styrda enheten via KVM-enheten trots att alla kablar är korrekt anslutna kan du prova följande.

1. Kontrollera kopplingen.

    Vi tar Comet (GL-RM1) som exempel. Den har två USB Type-C-portar:

    - Porten på sidan är märkt "5V 2A" och används för strömförsörjning (ansluts till en nätadapter).
    - Porten på baksidan är märkt med mus- och tangentbordssymboler och ansluts till den styrda enhetens USB-port för att ta emot tangentbords- och mussignaler.

    Om du förväxlar de här två anslutningarna startar inte KVM-enheten, och musen och tangentbordet slutar svara.

    Kontrollera att de två Type-C-gränssnitten är korrekt anslutna.

    ![Portar på GL-RM1](https://static.gl-inet.com/docs/kvm/faq/cannot_control_mouse/gl-rm1-ports.png){class="glboxshadow gl-80-desktop"}

2. Kontrollera USB-kabeln.

    Använd den medföljande USB-kabeln. Kontrollera att den ansluter den styrda enhetens USB-port till KVM-enhetens USB-port och att den stöder dataöverföring.

    Det är bara kablar som klarar dataöverföring som gör det möjligt att styra fjärrenheten med tangentbord och mus.

    Anslut USB-kabeln på nytt och starta om den styrda enheten.

3. Växla musläget till relativt läge.

    Logga in på din KVM, gå till Settings -> Mouse Mode, växla till Relative och kontrollera om problemet är löst.

    ![Musläge](https://static.gl-inet.com/docs/kvm/faq/cannot_control_mouse/mouse_mode.jpg){class="glboxshadow"}

4. Inaktivera de virtuella medierna.

    Logga in på din KVM, gå till Virtual Media, klicka på ikonen med tre punkter och inaktivera funktionen.

    ![Inaktivera virtuella medier](https://static.gl-inet.com/docs/kvm/faq/cannot_control_mouse/disable_virtual_media.png){class="glboxshadow" width="422"}

    Anledningen är att KVM-enheten, när virtuella medier är aktiverade, kan simulera en USB-lagringsenhet som är ansluten till den styrda enheten. Vissa enheter inaktiverar dock alla USB-indata när de identifierar en okänd USB-lagringsenhet, vilket gör att musen och tangentbordet slutar svara.

5. Ändra enhetsidentiteten.

    Logga in på din KVM, gå till Settings -> System -> Device Identity och ändra den KVM-identitet som den styrda enheten identifierar.

    ![Ändra enhetsidentitet](https://static.gl-inet.com/docs/kvm/faq/cannot_control_mouse/change_device_identity.png){class="glboxshadow"}

6. Uppgradera KVM-enhetens firmware till den senaste versionen. [KVM Firmware Download Center](https://dl.gl-inet.com/kvm){target="_blank"}

7. Kontrollera i Enhetshanteraren på den styrda datorn om några drivrutiner inte fungerar.

8. Kontrollera om den styrda enheten blockeras av IT-säkerhetsprogramvara.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
