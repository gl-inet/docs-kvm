# De KVM op afstand openen via ZeroTier {#how-to-access-kvm-remotely-via-zerotier}

> Opmerking: voer een upgrade uit van de firmware van uw KVM naar v1.8.0 voordat u deze functie gebruikt.

De GL.iNet KVM is geïntegreerd met ZeroTier, zodat u de KVM voor externe toegang aan het ZeroTier-netwerk kunt koppelen – zonder de GLKVM-app te installeren of de cloudservice te gebruiken.

Volg deze stappen om uw GL.iNet KVM op afstand te openen via ZeroTier.

## ZeroTier inschakelen {#enable-zerotier}

**Verbind uw KVM en het besturende apparaat voordat u begint met hetzelfde lokale netwerk.**

1. Open een browser op het besturende apparaat. Voor een betere compatibiliteit wordt Chrome of Edge aanbevolen.
    
2. Meld u lokaal aan bij de console van uw KVM via de domeinnaam of het IP-adres. Hier gebruiken we het lokale IP-adres als voorbeeld.

    Voer het **LAN-IP-adres** van de KVM (te vinden op het touchscreen of in uw router) in de adresbalk in. U wordt naar de aanmeldpagina van GLKVM geleid. Voer uw beheerderswachtwoord in.

    ![Lokale toegang via IP-adres](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/1_local_access.png){class="glboxshadow"}

3. Ga na het aanmelden naar **Apps Center** -> **ZeroTier**. Schakel ZeroTier in; er verschijnt dan een gele melding zoals hieronder weergegeven.

    Klik op de hyperlink of [hier](https://my.zerotier.com/){target="_blank"} om u aan te melden bij ZeroTier Central en uw ZeroTier-netwerk te maken.

    ![ZeroTier inschakelen](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/2_enable_zerotier.png){class="glboxshadow"}
    
## De KVM aan ZeroTier koppelen {#bind-kvm-to-zerotier}

1. Wanneer u zich voor het eerst aanmeldt bij [ZeroTier](https://my.zerotier.com/){target="_blank"}, moet u mogelijk ZeroTier Central selecteren.

    ![Central selecteren](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/3_select_central.png){class="glboxshadow"}

    Selecteer de gewenste versie om verder te gaan. Hier nemen we **New Central** als voorbeeld.
    
    Meld u aan met uw e-mailadres en wachtwoord. Als u nog geen account hebt, registreert u zich eerst.

    ![Aanmelden bij ZeroTier](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/4_zerotier_signin.png){class="glboxshadow"}

2. Maak na het aanmelden een organisatie aan.

    ![Organisatie aanmaken](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/5_create_org.png){class="glboxshadow"}

3. Kies een abonnement. Hier kiezen we als voorbeeld het abonnement **Personal**, met 10 apparaten, 1 netwerkbeheerder en 1 netwerk. Als u meer netwerken wilt maken, meer apparaten wilt toevoegen of aangepaste routes en DNS wilt toevoegen, kiest u het abonnement Essential of Scale.

    ![Abonnement kiezen](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/6_select_plan.png){class="glboxshadow"}

4. Uw ZeroTier-netwerk is nu gemaakt. Kopieer de **Network ID**, een alfanumerieke reeks van 16 tekens. U hebt deze later nodig wanneer u apparaten aan uw ZeroTier-netwerk toevoegt. Houd dit tabblad open.

    ![Netwerk-ID](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/7_copy_network_id.png){class="glboxshadow"}

5. Ga terug naar de console van uw KVM en ga naar **Apps Center** -> **ZeroTier**. Zoek **Network ID** en klik op **Set**.

    ![Netwerk-ID](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/8_set_network_id1.png){class="glboxshadow"}

    Plak in het pop-upvenster de **Network ID** en klik op **Confirm**.

    ![Netwerk-ID](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/8_set_network_id2.png){class="glboxshadow"}

    In de console verschijnt een gele melding dat dit apparaat moet worden geautoriseerd.

    ![Autoriseren 1](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/9_authorize1.png){class="glboxshadow"}

6. Ga terug naar ZeroTier Central. U ziet een apparaat (uw KVM) dat op goedkeuring wacht. Klik op **Authorize**.

    ![Autoriseren 2](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/9_authorize2.png){class="glboxshadow"}

    Na de autorisatie verandert de status in een groene status Authorized, zoals hieronder weergegeven.

    ![Geautoriseerd 1](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/10_authorized1.png){class="glboxshadow"}

    In de KVM-console ziet u ook de **Network ID** en het **Virtual IP**, zoals hieronder weergegeven.

    ![Geautoriseerd 2](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/10_authorized2.png){class="glboxshadow"}

## Het besturende apparaat koppelen {#bind-the-controlling-device}

In het onderstaande voorbeeld ziet u hoe u een Windows-laptop (als besturend apparaat) aan het ZeroTier-netwerk koppelt.

1. Installeer ZeroTier op uw laptop via [deze pagina](https://www.zerotier.com/download/){target="_blank"}.

2. Start ZeroTier op de laptop en voeg de laptop toe aan hetzelfde ZeroTier-netwerk.

    Let op: ZeroTier toont geen apart venster of aparte interface op het bureaublad; het programma staat alleen als pictogram in het systeemvak (rechtsonder). Alle handelingen voert u uit via het snelmenu.

    Klik met de rechtermuisknop op het ZeroTier-pictogram en klik op **Join New Network**. Voer in het pop-upvenster dezelfde **Network ID** in om deze pc aan hetzelfde ZeroTier-netwerk toe te voegen.

    ![Netwerk toevoegen](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/11_pc_join_network.jpg){class="glboxshadow"}

    Ga vervolgens naar ZeroTier Central, zoek het apparaat met de status Pending en autoriseer het.

    ![Autoriseren](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/12_authorize.png){class="glboxshadow"}

2. Na de autorisatie verandert de status in een groene status Authorized, zoals hieronder weergegeven.

    ![Geautoriseerd](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/13_authorized.png){class="glboxshadow"}

3. Uw KVM en de laptop zijn nu allebei toegevoegd aan hetzelfde ZeroTier-netwerk. U ziet dit aan de netwerk-ID, zoals hieronder weergegeven.

    ![Hetzelfde ZeroTier-netwerk](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/14_same_zt_network.png){class="glboxshadow"}

## Externe toegang via ZeroTier {#remote-access-via-zerotier}

In het onderstaande voorbeeld ziet u hoe u de KVM-console op afstand opent via het ZeroTier-IP-adres.

1. Meld u op uw laptop met uw account aan bij ZeroTier Central, zoek uw KVM-apparaat en klik op het **ZT IP** ervan om het te kopiëren.

    ![ZeroTier-IP-adres](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/15_zerotier_ip.png){class="glboxshadow"}

2. Open een nieuw browsertabblad, plak het gekopieerde ZeroTier-IP-adres in de adresbalk en druk op Enter. U wordt doorgestuurd naar de aanmeldpagina van GLKVM.

    Voer uw beheerderswachtwoord in om u aan te melden. U kunt uw GL.iNet KVM en het bestuurde apparaat nu openen via het ZeroTier-IP-adres.

    ![Externe toegang](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/16_remote_access.png){class="glboxshadow"}

    **Tip**: Wanneer u dit ZeroTier-IP-adres voor het eerst opent, kan er een privacyfout verschijnen. Klik op **Advanced** -> **Proceed** om door te gaan. Zie [Privacyfout in uw browser](privacy_error_from_your_browser.md){target="_blank"} voor meer informatie.

---

Hebt u nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
