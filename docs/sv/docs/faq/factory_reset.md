# Så fabriksåterställer du din GL.iNet KVM-enhet {#how-do-i-factory-reset-my-glinet-kvm}

## Metod 1 – Använd den fysiska återställningsknappen {#method-1-use-the-physical-reset-button}

Kontrollera att KVM-enheten är påslagen och har startat klart.

Håll den fysiska RESET-knappen intryckt i **8 till 10 sekunder** och släpp den sedan. Om KVM-enheten har ett återställningshål använder du en nål för att hålla knappen i hålet intryckt i 8 sekunder innan du släpper den. Använd växlingsknappen på frontpanelen på Comet X (GL-RM4PE).

Vänta tills KVM-enheten startar om automatiskt. Koppla inte bort strömmen under återställningen.

Håll inte återställningsknappen intryckt när du slår på KVM-enheten. Använd inte återställningsknappen på den anslutna datorn eller på ATX-kortet.

## Metod 2 – Använd det lokala webbgränssnittet {#method-2-use-the-local-web-interface}

Anslut datorn och KVM-enheten till samma lokala nätverk. Öppna KVM-enhetens lokala IP-adress i en webbläsare och logga in. Se [Så kommer du åt KVM-enheten lokalt via webbläsaren](local_access_via_browser.md).

Om KVM-enheten kör firmware v1.10 eller senare öppnar du **Settings** i det övre högra hörnet och går till **System** -> **Reset Device**. Klicka på **Reset**, bekräfta och vänta tills KVM-enheten startar om automatiskt. Koppla inte bort strömmen under återställningen.

![reset 1](https://static.gl-inet.com/docs/kvm/faq/factory_reset/reset1.png){class="glboxshadow"}

Om KVM-enheten kör firmware v1.9 eller tidigare öppnar du **Settings** i det övre vänstra hörnet och går till **System** -> **Reset KVM**. Klicka på **Reset**, bekräfta och vänta tills KVM-enheten startar om automatiskt. Koppla inte bort strömmen under återställningen.

![reset 2](https://static.gl-inet.com/docs/kvm/faq/factory_reset/reset2.png){class="glboxshadow"}

## Efter återställningen {#after-the-reset}

En fabriksåterställning raderar de anpassade inställningarna på KVM-enheten. KVM-enhetens lokala IP-adress kan ändras efter omstarten. Öppna det lokala webbgränssnittet igen, följ anvisningarna för den första konfigurationen för att ställa in ett administratörslösenord och konfigurera de inställningar du behöver på nytt manuellt.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
