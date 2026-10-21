# Anslutningen misslyckas vid fjärråtkomst via GLKVM-appen {#connection-failed-when-remote-access-via-glkvm-app}

Vid fjärråtkomst via GLKVM-appen kan det ibland hända att KVM-enheten visas som Online i GLKVM-appen, men fastnar på "Connecting" när du klickar på den.

![Enheten är online](https://static.gl-inet.com/docs/kvm/faq/connection_failed_when_remotely_accessing_via_glkvm/device_online.png){class="glboxshadow"}

![Ansluter](https://static.gl-inet.com/docs/kvm/faq/connection_failed_when_remotely_accessing_via_glkvm/connecting.png){class="glboxshadow"}

Felsökningsguide:

1. Säkerställ en stabil nätverksanslutning.

    Kontrollera att KVM-enheten har en stabil internetanslutning. En lysdiod med fast vitt sken anger normal nätverksanslutning.

2. Kontrollera brandväggsreglerna i nätverket.

    Inaktivera den lokala brandväggen tillfälligt, eller lägg till GL.iNet-relaterade domäner (t.ex. glkvm.com) i brandväggens lista över tillåtna adresser. Försök ansluta igen när du har gjort ändringarna.

    Nedan beskrivs som referens hur du ändrar brandväggsreglerna i Sky Network.

    ??? note "Sky Network (t.ex. Sky Max Hub)"

        Säkerhetsmekanismen i Sky Network kan identifiera domännamnet `glkvm.com` som en misstänkt webbplats och blockera åtkomsten. Du kan häva begränsningarna via Sky-appen.<br>

        1. Öppna MySky-appen, gå till **Broadband** -> **Advanced Security** och kontrollera om några GL.iNet-relaterade domäner är begränsade.

            ![MySky 1](https://static.gl-inet.com/docs/kvm/faq/connection_failed_when_remotely_accessing_via_glkvm/mysky-1.png){class="glboxshadow"}

        2. Om domänen är blockerad klickar du på nedåtpilen för att visa detaljer och väljer sedan **Allow Access** för att häva begränsningen.

            ![MySky 2](https://static.gl-inet.com/docs/kvm/faq/connection_failed_when_remotely_accessing_via_glkvm/mysky-2.png){class="glboxshadow" width="300"}

3. Inaktivera VPN/proxy på den styrande enheten.

    Kontrollera att enheten som kör GLKVM-appen inte har VPN- eller proxytjänster aktiverade, eftersom de kan störa anslutningen.

4. Starta om KVM-enheten om möjligt.

    Gör om möjligt en maskinvaruomstart av KVM-enheten för att åtgärda tillfälliga nätverks- eller programvaruproblem.

    Om du inte befinner dig nära KVM-enheten kan du starta om den på distans via GLKVM-appen:

    1. Klicka på **Manage** i det övre högra hörnet av enheten i enhetslistan.

        ![Omstart via appen 1](https://static.gl-inet.com/docs/kvm/faq/connection_failed_when_remotely_accessing_via_glkvm/app_reboot_1.png){class="glboxshadow"}

    2. Klicka på **More** och välj **Reboot**.

        ![Omstart via appen 2](https://static.gl-inet.com/docs/kvm/faq/connection_failed_when_remotely_accessing_via_glkvm/app_reboot_2.png){class="glboxshadow"}

Ytterligare tekniska anmärkningar:

1. Kontrollera att DNS-uppslag fungerar för domänerna.

2. Kontrollera att utgående trafik till standardportar för KVM/fjärråtkomst inte blockeras.

3. I företagsnätverk bör du rådfråga IT-administratörerna om eventuella policyer för trafikfiltrering.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
