# De KVM op afstand openen via NetBird {#how-to-access-kvm-remotely-via-netbird}

> Opmerking: voer een upgrade uit van de firmware van uw KVM naar v1.9.0 voordat u deze functie gebruikt.

[NetBird](https://netbird.io/){target="_blank"} is een opensource zero-trust-netwerkplatform waarmee u veilige privénetwerken kunt opzetten voor thuis- en zakelijk gebruik. Als overlaynetwerk op basis van WireGuard® biedt NetBird altijd en overal veilige toegang tot uw apparaten.

De GL.iNet KVM is geïntegreerd met NetBird, zodat u de KVM voor externe toegang aan het virtuele NetBird-netwerk kunt koppelen – zonder de GLKVM-app te installeren of de cloudservice te gebruiken.

Volg deze stappen om uw GL.iNet KVM op afstand te openen via NetBird.

## De KVM aan NetBird koppelen {#bind-kvm-to-netbird}

**Verbind uw KVM en het besturende apparaat voordat u begint met hetzelfde lokale netwerk.**

1. Meld u lokaal aan bij de console van uw KVM via de domeinnaam of het IP-adres en ga naar **Apps Center** -> **NetBird**. Schakel NetBird in en klik op **Bind Device**.

    ![Apparaat koppelen](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/1-bind-device.png){class="glboxshadow"}

2. U wordt doorgestuurd naar de pagina voor apparaatbevestiging. Klik op **Confirm**.

    ![Apparaat bevestigen](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/2-confirm.png){class="glboxshadow"}

3. Meld u aan bij uw NetBird-account. Als u nog geen account hebt, registreert u zich eerst.

    ![Aanmelden bij NetBird](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/3-signin.png){class="glboxshadow"}

4. Na het aanmelden wordt het KVM-apparaat automatisch aan uw account gekoppeld.

    ![KVM verbonden](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/4-connected.png){class="glboxshadow"}

    In het NetBird-dashboard ziet u uw KVM ook op de pagina **Peers** staan.

    ![NetBird-dashboard](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/5-dashboard.png){class="glboxshadow"}

## Het besturende apparaat koppelen {#bind-the-controlling-device}

In het onderstaande voorbeeld ziet u hoe u een Windows-laptop (als besturend apparaat) aan het NetBird-netwerk koppelt.

1. Installeer NetBird op uw laptop via [deze pagina](https://app.netbird.io/install){target="_blank"}.

    ![NetBird installeren](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/6-install.png){class="glboxshadow"}

2. Start NetBird op de laptop en voeg de laptop toe aan hetzelfde NetBird-netwerk.

    NetBird toont geen apart venster of aparte interface op het bureaublad; het programma staat alleen als pictogram in het systeemvak (rechtsonder). Alle handelingen voert u uit via het snelmenu.

    Klik met de rechtermuisknop op het NetBird-pictogram en klik op **Connect**.

    ![Pc verbinden](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/7-pc-connect.png){class="glboxshadow gl-50-desktop"}

3. Klik in het pop-upvenster op **Accept** om te autoriseren.

    ![Autoriseren](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/8-authorize.png){class="glboxshadow"}

    Uw laptop wordt automatisch aan uw account gekoppeld en aan hetzelfde NetBird-netwerk toegevoegd.

    ![Pc verbonden](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/9-login-success.png){class="glboxshadow"}

4. In het NetBird-dashboard staan nu twee apparaten op de pagina **Peers**: uw KVM en de besturende laptop.

    ![NetBird-dashboard](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/10-dashboard.png){class="glboxshadow"}

## Externe toegang via NetBird {#remote-access-via-netbird}

In het onderstaande voorbeeld ziet u hoe u de KVM-console op afstand opent via het virtuele IP-adres van NetBird.

1. Meld u op uw laptop aan bij het NetBird-dashboard en ga naar **Peers**.

    Zoek uw KVM-apparaat en klik op het **NetBird IP** ervan (in dit voorbeeld `100.100.141.229`) om het virtuele IP-adres te kopiëren.

    ![NetBird-IP-adres van de KVM](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/11-kvm-netbird-ip.png){class="glboxshadow"}

    Beweeg de aanwijzer over het IP-adres om meer details te bekijken, zoals het openbare IP-adres, de domeinnaam en de regio.

2. Open een nieuw browsertabblad, plak het gekopieerde NetBird-IP-adres in de adresbalk en druk op Enter. U wordt doorgestuurd naar de aanmeldpagina van GLKVM.

    ![Aanmelden voor externe toegang](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/12-ip-login.png){class="glboxshadow"}

    Voer uw beheerderswachtwoord in om u aan te melden. U kunt uw GL.iNet KVM en het bestuurde apparaat nu openen via het NetBird-IP-adres.

    ![Externe toegang gelukt](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/12-ip-access.png){class="glboxshadow"}

    **Tip**: Wanneer u dit NetBird-IP-adres voor het eerst opent, kan er een privacyfout verschijnen. Klik op **Advanced** -> **Proceed** om door te gaan. Zie [Privacyfout in uw browser](privacy_error_from_your_browser.md){target="_blank"} voor meer informatie.

---

Hebt u nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
