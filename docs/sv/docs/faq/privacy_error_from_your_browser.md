# Sekretessfel vid åtkomst till KVM-enheten via webbläsaren {#privacy-error-when-accessing-kvm-via-browser}

När du öppnar GL.iNet KVM via webbläsaren kan webbläsaren visa en varning: **Your connection isn't private**.

![Sekretessfel](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/privacy_error_1.png){class="glboxshadow"}

Varningen betyder att webbläsaren inte kan validera det SSL/TLS-certifikat som KVM-enheten visar. Certifikatet kanske till exempel inte har utfärdats av en certifikatutfärdare som webbläsaren litar på, eller så stämmer det inte med den IP-adress eller det värdnamn som du använde för att öppna konsolen.

## Varför får jag den här varningen? {#why-do-i-get-this-warning}

I exemplet ovan är **192.168.8.11** KVM-enhetens lokala IP-adress, som har tilldelats dynamiskt av den överordnade routern via DHCP.

!!! Note "Obs!"

    Om gatewayen för routern som din GL.iNet KVM är ansluten till är "192.168.x.1" (där x i privata nätverk vanligtvis är 0, 1 eller 8) bör KVM-enhetens lokala IP-adress vara "192.168.x.y" (där y är en giltig värdadress i subnätet).

Den här lokala IP-adressen används för att komma åt GL.iNet KVM-konsolen, inte en offentlig webbplats.

KVM-enheten använder ett standardcertifikat för TLS vid HTTPS-åtkomst via webbläsare. Webbläsare validerar certifikat för lokala konsoler på samma sätt som för offentliga webbplatser: certifikatet måste vara betrott, giltigt och stämma med adressen som används.

Om webbläsaren inte litar på standardcertifikatet, eller om certifikatet inte omfattar den lokala IP-adress eller det värdnamn som du angav, visar webbläsaren en varning. Varningen betyder inte att KVM-enheten saknar certifikat. HTTPS kan fortfarande kryptera anslutningen, men webbläsaren kan inte verifiera KVM-enhetens identitet.

## Hur åtgärdar jag varningen? {#how-to-resolve-the-warning}

Vid lokal åtkomst kontrollerar du först att adressen tillhör din KVM. Klicka sedan på **Advanced** och **Continue to "192.168.8.11"** (den exakta formuleringen varierar mellan webbläsare).

![Fortsätt till 192.168.8.11](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/privacy_error_2.jpg){class="glboxshadow"}

Därefter omdirigeras du till GL.iNet KVM-konsolen.

![Lokal åtkomst till KVM-administrationen](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/local_access.png){class="glboxshadow"}

## Kan jag använda ett eget certifikat? {#can-i-use-my-own-certificate}

Ja. Du kan installera och använda ett eget SSL/TLS-certifikat på KVM-enheten. Följ stegen nedan.

1. Skaffa ett SSL/TLS-certifikat som omfattar det värdnamn eller den IP-adress som du använder för att komma åt KVM-enheten. För att undvika varningar i webbläsaren måste certifikatet vara giltigt och utfärdat av en certifikatutfärdare som webbläsaren litar på. Ett självsignerat certifikat ger fortfarande en varning, om du inte uttryckligen konfigurerar den styrande enheten att lita på det.

2. Logga in på KVM-konsolen. Klicka på sköldikonen i det övre högra hörnet för att gå till **Security** -> **TLS Certificate**.

    ![Eget certifikat 1](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/custom_cert1.png){class="glboxshadow"}

    Välj **Custom Certificate** i popup-fönstret och ladda sedan upp certifikatfilen och den privata nyckeln. Funktionen finns sedan firmware v1.8.0.

    ![Eget certifikat 2](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/custom_cert2.png){class="glboxshadow"}

    Du kan också byta ut certifikatet och den privata nyckeln på KVM-enheten via en SSH-terminal eller WinSCP. Certifikatet och nyckeln lagras i följande katalog:

    `/etc/kvmd/user/ssl`

    Ersätt dem med ditt nya SSL-certifikat och din nya privata nyckel.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
