# Så kommer du åt KVM-enheten på distans via NetBird {#how-to-access-kvm-remotely-via-netbird}

> Obs! Uppgradera KVM-enhetens firmware till v1.9.0 innan du använder den här funktionen.

[NetBird](https://netbird.io/){target="_blank"} är en nätverksplattform med öppen källkod baserad på nolltillit (zero trust) som låter dig bygga säkra privata nätverk för hem- och företagsbruk. Som ett WireGuard®-baserat overlay-nätverk ger NetBird säker åtkomst till dina enheter när som helst och var som helst.

GL.iNet KVM har integrerat stöd för NetBird, så att du kan koppla enheten till det virtuella NetBird-nätverket för fjärråtkomst – utan att installera GLKVM-appen eller använda molntjänsten.

Följ stegen nedan för att komma åt din GL.iNet KVM på distans via NetBird.

## Koppla KVM-enheten till NetBird {#bind-kvm-to-netbird}

**Anslut KVM-enheten och den styrande enheten till samma lokala nätverk innan du börjar.**

1. Logga in på KVM-konsolen lokalt via domännamn eller IP-adress och gå sedan till **Apps Center** -> **NetBird**. Aktivera NetBird och klicka på **Bind Device**.

    ![Koppla enheten](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/1-bind-device.png){class="glboxshadow"}

2. Du omdirigeras till sidan för bekräftelse av enheten. Klicka på **Confirm**.

    ![Bekräfta enheten](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/2-confirm.png){class="glboxshadow"}

3. Logga in på ditt NetBird-konto. Om du inte har något konto registrerar du dig först.

    ![Logga in på NetBird](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/3-signin.png){class="glboxshadow"}

4. När du har loggat in kopplas KVM-enheten automatiskt till ditt konto.

    ![KVM-enheten är ansluten](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/4-connected.png){class="glboxshadow"}

    I NetBird-instrumentpanelen kan du även se din KVM i listan på sidan **Peers**.

    ![NetBird-instrumentpanel](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/5-dashboard.png){class="glboxshadow"}

## Koppla den styrande enheten {#bind-the-controlling-device}

Exemplet nedan visar hur du kopplar en bärbar Windows-dator (som styrande enhet) till NetBird-nätverket.

1. Installera NetBird på den bärbara datorn [här](https://app.netbird.io/install){target="_blank"}.

    ![Installera NetBird](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/6-install.png){class="glboxshadow"}

2. Kör NetBird på den bärbara datorn och lägg till den i samma NetBird-nätverk.

    NetBird visar inget separat fönster eller gränssnitt på skrivbordet, utan finns bara som en ikon i systemfältet (i det nedre högra hörnet). Alla åtgärder görs via högerklicksmenyn.

    Högerklicka på NetBird-ikonen och klicka på **Connect**.

    ![Anslut datorn](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/7-pc-connect.png){class="glboxshadow gl-50-desktop"}

3. Klicka på **Accept** i popup-fönstret för att auktorisera.

    ![Auktorisera](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/8-authorize.png){class="glboxshadow"}

    Den bärbara datorn kopplas automatiskt till ditt konto och läggs till i samma NetBird-nätverk.

    ![Datorn är ansluten](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/9-login-success.png){class="glboxshadow"}

4. I NetBird-instrumentpanelen finns nu två enheter på sidan **Peers**: din KVM och den styrande bärbara datorn.

    ![NetBird-instrumentpanel](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/10-dashboard.png){class="glboxshadow"}

## Fjärråtkomst via NetBird {#remote-access-via-netbird}

Exemplet nedan visar hur du kommer åt KVM-konsolen på distans via den virtuella NetBird-IP-adressen.

1. Logga in på NetBird-instrumentpanelen på den bärbara datorn och gå till **Peers**.

    Leta upp din KVM-enhet och klicka på dess **NetBird IP** (`100.100.141.229` i det här exemplet) för att kopiera den virtuella IP-adressen.

    ![KVM-enhetens NetBird-IP](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/11-kvm-netbird-ip.png){class="glboxshadow"}

    Håll markören över IP-adressen för att visa mer information, till exempel publik IP-adress, domän och region.

2. Öppna en ny flik i webbläsaren, klistra in den kopierade NetBird-IP-adressen i adressfältet och tryck på Enter. Du kommer till inloggningssidan för GLKVM.

    ![Inloggning för fjärråtkomst](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/12-ip-login.png){class="glboxshadow"}

    Ange ditt administratörslösenord för att logga in. Nu kan du komma åt din GL.iNet KVM och den styrda enheten via NetBird-IP-adressen.

    ![Fjärråtkomst lyckades](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/12-ip-access.png){class="glboxshadow"}

    **Tips!** Ett sekretessfel kan visas första gången du öppnar NetBird-IP-adressen. Klicka bara på **Advanced** -> **Proceed** för att fortsätta. Mer information finns i [Sekretessfel i webbläsaren](privacy_error_from_your_browser.md){target="_blank"}.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
