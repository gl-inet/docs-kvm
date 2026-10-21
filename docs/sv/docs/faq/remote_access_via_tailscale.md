# Så kommer du åt KVM-enheten på distans via Tailscale {#how-to-access-kvm-remotely-via-tailscale}

GL.iNet KVM har integrerat stöd för Tailscale, så att du kan koppla enheten till det virtuella Tailscale-nätverket för fjärråtkomst – utan att installera GLKVM-appen eller använda molntjänsten. Det är särskilt användbart när den styrande enheten inte kör Windows, macOS, Android eller iOS (och därför inte kan installera GLKVM-appen), eller när du inte vill använda GLKVM-appen eller molntjänsten.

Följ stegen nedan för att komma åt din GL.iNet KVM på distans via Tailscale.

## Koppla KVM-enheten till Tailscale {#bind-kvm-to-tailscale}

**Anslut KVM-enheten och den styrande enheten till samma lokala nätverk innan du börjar.**

1. Öppna en webbläsare på den styrande enheten. Chrome eller Edge rekommenderas för bättre kompatibilitet.

2. Logga in på KVM-konsolen lokalt via domännamn eller IP-adress. Här används standarddomänen som exempel.

    Ange `glkvm.local` i adressfältet. Du kommer till inloggningssidan för GLKVM. Ange ditt administratörslösenord.

    ![Lokal åtkomst via domän](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_1.png){class="glboxshadow"}

3. När du har loggat in går du till **Apps Center** -> **Tailscale**. Aktivera Tailscale och klicka på **Bind Device**.

    ![Aktivera Tailscale](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/enable_tailscale.png){class="glboxshadow"}

4. Du kommer till inloggningssidan för Tailscale. Ange din e-postadress för att logga in.

    ![Logga in på Tailscale](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/log_in_tailscale.png){class="glboxshadow"}

5. När du har loggat in visar sidan att du är på väg att ansluta enheten glkvm till ditt tailnet. Klicka på **Connect**.

    ![Anslut KVM-enheten till tailnet](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/connect_kvm_to_tailscale.png){class="glboxshadow"}

    KVM-enheten kopplas sedan till ditt tailnet.

    ![KVM-enheten har kopplats](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/bind_kvm_successful.png){class="glboxshadow"}

6. Du omdirigeras till Tailscale-konsolen, där en enhet med namnet **glkvm** visas under **Machines**.

    ![Tailscale-konsolen 1](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/tailscale_panel_1.png){class="glboxshadow"}

## Koppla den styrande enheten {#bind-the-controlling-device}

Exemplet nedan visar hur du kopplar en bärbar Windows-dator (som styrande enhet) till Tailscale-nätverket.

1. Installera Tailscale på den bärbara datorn [här](https://tailscale.com/download){target="_blank"}.

2. Kör Tailscale på den bärbara datorn och logga in med samma e-postadress.

    ![Logga in på Tailscale](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/log_in_tailscale.png){class="glboxshadow"}

3. När du har loggat in visar sidan att du är på väg att ansluta den bärbara datorn (dvs. den styrande enheten) till ditt tailnet. Klicka på **Connect**.

    ![Anslut datorn till tailnet](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/connect_pc_to_tailscale.png){class="glboxshadow"}

    Den bärbara datorn kopplas sedan till ditt tailnet.

    ![Datorn har kopplats](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/bind_pc_successful.png){class="glboxshadow"}

4. Du omdirigeras till Tailscale-konsolen, där även den styrande enheten visas under **Machines**.

    ![Tailscale-konsolen 2](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/tailscale_panel_2.png){class="glboxshadow"}

## Fjärråtkomst via Tailscale {#remote-access-via-tailscale}

Klicka på glkvm-enhetens **Address** (`100.104.185.26` i det här exemplet) i Tailscale-konsolen.

![Hämta virtuell IP-adress](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/get_vitual_ip.png){class="glboxshadow"}

Fyra värden visas:

- glkvm (enhetsnamn)
- glkvm.tail1fd0.ts.net (domän som tilldelats av Tailscale)
- fd7a:115c:a1e0:301:b92f (virtuell IPv6-adress)
- 100.104.185.26 (virtuell IPv4-adress).

De tilldelas av Tailscale för identifiering av enheten och kommunikation i det virtuella nätverket. Du kan komma åt KVM-enheten på distans med den domän som Tailscale har tilldelat, den virtuella IPv4-adressen eller den virtuella IPv6-adressen.

Vi tar den virtuella IPv4-adressen som exempel.

1. Kopiera KVM-enhetens virtuella IPv4-adress.

2. Öppna en ny flik och klistra in IP-adressen i adressfältet.

    ![Öppna den virtuella IP-adressen](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/enter_vitual_ip.png){class="glboxshadow"}

    Ett sekretessfel kan visas. [Varför får jag det här sekretessfelet?](privacy_error_from_your_browser.md){target="_blank"}

    ![Sekretessfel](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/privacy_error.png){class="glboxshadow"}

    Klicka på **Advanced** och sedan på **Proceed to 100.104.185.26**. Du omdirigeras till inloggningssidan för GLKVM.

    ![Fortsätt](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/proceed.png){class="glboxshadow"}

3. Ange ditt administratörslösenord för att logga in. Nu kan du komma åt din GL.iNet KVM och den styrda enheten via den virtuella Tailscale-IP-adressen.

    ![Fjärråtkomst lyckades](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/remote_access_via_tailscale.png){class="glboxshadow"}

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
