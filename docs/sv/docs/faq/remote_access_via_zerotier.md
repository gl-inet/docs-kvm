# Så kommer du åt KVM-enheten på distans via ZeroTier {#how-to-access-kvm-remotely-via-zerotier}

> Obs! Uppgradera KVM-enhetens firmware till v1.8.0 innan du använder den här funktionen.

GL.iNet KVM har integrerat stöd för ZeroTier, så att du kan koppla enheten till ZeroTier-nätverket för fjärråtkomst – utan att installera GLKVM-appen eller använda molntjänsten.

Följ stegen nedan för att komma åt din GL.iNet KVM på distans via ZeroTier.

## Aktivera ZeroTier {#enable-zerotier}

**Anslut KVM-enheten och den styrande enheten till samma lokala nätverk innan du börjar.**

1. Öppna en webbläsare på den styrande enheten. Chrome eller Edge rekommenderas för bättre kompatibilitet.

2. Logga in på KVM-konsolen lokalt via domännamn eller IP-adress. Här används den lokala IP-adressen som exempel.

    Ange KVM-enhetens **LAN-IP-adress** (som visas på pekskärmen eller i routern) i adressfältet. Du kommer till inloggningssidan för GLKVM. Ange ditt administratörslösenord.

    ![Lokal åtkomst via IP](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/1_local_access.png){class="glboxshadow"}

3. När du har loggat in går du till **Apps Center** -> **ZeroTier**. Aktivera ZeroTier, så visas ett gult meddelande enligt bilden nedan.

    Klicka på länken eller [här](https://my.zerotier.com/){target="_blank"} för att logga in på ZeroTier Central och skapa ditt ZeroTier-nätverk.

    ![Aktivera ZeroTier](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/2_enable_zerotier.png){class="glboxshadow"}

## Koppla KVM-enheten till ZeroTier {#bind-kvm-to-zerotier}

1. Första gången du loggar in på [ZeroTier](https://my.zerotier.com/){target="_blank"} kan du behöva välja ZeroTier Central.

    ![Välj Central](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/3_select_central.png){class="glboxshadow"}

    Välj lämplig version för att fortsätta. Här används **New Central** som exempel.

    Logga in med din e-postadress och ditt lösenord. Om du inte har något konto registrerar du dig först.

    ![Inloggning på ZeroTier](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/4_zerotier_signin.png){class="glboxshadow"}

2. Skapa en organisation när du har loggat in.

    ![Skapa organisation](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/5_create_org.png){class="glboxshadow"}

3. Välj ett abonnemang. Här väljs abonnemanget **Personal** som exempel, vilket omfattar 10 enheter, 1 nätverksadministratör och 1 nätverk. Om du behöver skapa fler nätverk, lägga till fler enheter eller lägga till anpassade rutter och DNS väljer du abonnemanget Essential eller Scale.

    ![Välj abonnemang](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/6_select_plan.png){class="glboxshadow"}

4. Nu har ditt ZeroTier-nätverk skapats. Kopiera **Network ID**, som är en alfanumerisk sträng på 16 tecken. Du behöver det senare när du lägger till enheter i ZeroTier-nätverket. Låt fliken vara öppen.

    ![Nätverks-ID](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/7_copy_network_id.png){class="glboxshadow"}

5. Gå tillbaka till KVM-konsolen och gå till **Apps Center** -> **ZeroTier**. Leta upp **Network ID** och klicka på **Set**.

    ![Nätverks-ID](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/8_set_network_id1.png){class="glboxshadow"}

    Klistra in **Network ID** i popup-fönstret och klicka på **Confirm**.

    ![Nätverks-ID](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/8_set_network_id2.png){class="glboxshadow"}

    Ett gult meddelande visas i konsolen om att enheten behöver auktoriseras.

    ![Auktorisering 1](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/9_authorize1.png){class="glboxshadow"}

6. Gå tillbaka till ZeroTier Central. En enhet (din KVM) väntar på godkännande. Klicka på **Authorize**.

    ![Auktorisering 2](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/9_authorize2.png){class="glboxshadow"}

    När enheten har auktoriserats ändras statusen till Authorized i grönt, enligt bilden nedan.

    ![Auktoriserad 1](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/10_authorized1.png){class="glboxshadow"}

    I KVM-konsolen kan du också se **Network ID** och **Virtual IP**, enligt bilden nedan.

    ![Auktoriserad 2](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/10_authorized2.png){class="glboxshadow"}

## Koppla den styrande enheten {#bind-the-controlling-device}

Exemplet nedan visar hur du kopplar en bärbar Windows-dator (som styrande enhet) till ZeroTier-nätverket.

1. Installera ZeroTier på den bärbara datorn [här](https://www.zerotier.com/download/){target="_blank"}.

2. Kör ZeroTier på den bärbara datorn och lägg till den i samma ZeroTier-nätverk.

    Observera att ZeroTier inte visar något separat fönster eller gränssnitt på skrivbordet, utan bara finns som en ikon i systemfältet (i det nedre högra hörnet). Alla åtgärder görs via högerklicksmenyn.

    Högerklicka på ZeroTier-ikonen och klicka på **Join New Network**. Ange samma **Network ID** i popup-fönstret för att lägga till datorn i samma ZeroTier-nätverk.

    ![Anslut till nätverket](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/11_pc_join_network.jpg){class="glboxshadow"}

    Gå sedan till ZeroTier Central, leta upp enheten med statusen Pending och auktorisera den.

    ![Auktorisera](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/12_authorize.png){class="glboxshadow"}

3. När enheten har auktoriserats ändras statusen till Authorized i grönt, enligt bilden nedan.

    ![Auktoriserad](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/13_authorized.png){class="glboxshadow"}

4. Nu har både KVM-enheten och den bärbara datorn lagts till i samma ZeroTier-nätverk. Det framgår av deras nätverks-ID, enligt bilden nedan.

    ![Samma ZeroTier-nätverk](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/14_same_zt_network.png){class="glboxshadow"}

## Fjärråtkomst via ZeroTier {#remote-access-via-zerotier}

Exemplet nedan visar hur du kommer åt KVM-konsolen på distans via ZeroTier-IP-adressen.

1. Logga in på ZeroTier Central med ditt konto på den bärbara datorn, leta upp KVM-enheten och klicka på dess **ZT IP** för att kopiera den.

    ![ZeroTier-IP](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/15_zerotier_ip.png){class="glboxshadow"}

2. Öppna en ny flik i webbläsaren, klistra in den kopierade ZeroTier-IP-adressen i adressfältet och tryck på Enter. Du kommer till inloggningssidan för GLKVM.

    Ange ditt administratörslösenord för att logga in. Nu kan du komma åt din GL.iNet KVM och den styrda enheten via ZeroTier-IP-adressen.

    ![Fjärråtkomst](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/16_remote_access.png){class="glboxshadow"}

    **Tips!** Ett sekretessfel kan visas första gången du öppnar ZeroTier-IP-adressen. Klicka bara på **Advanced** -> **Proceed** för att fortsätta. Mer information finns i [Sekretessfel i webbläsaren](privacy_error_from_your_browser.md){target="_blank"}.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
