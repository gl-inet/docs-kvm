# Så använder du kameragenomkoppling i fjärrmöten {#how-can-i-use-camera-passthrough-for-remote-meetings}

**Obs!** Funktionen introducerades i firmware v1.10.0 och stöds endast i läget WebRTC (FEC). Den är för närvarande tillgänglig via webbläsare och skrivbordsklienten, men stöds ännu inte i mobilappen.

---

När du arbetar hemifrån kan du använda KVM för att komma åt din kontorsdator och delta i ett videomöte i Zoom, Microsoft Teams eller en liknande app. Kameran kanske dock bara visar kontoret och inte dig.

Med funktionen **Camera** i GL.iNet KVM kan du överföra video från kameran på din hemdator till kontorsdatorn som en virtuell USB-kamera. Välj den här kameran i mötesappen så att andra deltagare kan se dig medan du delar filer eller program från kontorsdatorn.

## Snabbinstallation {#quick-setup}

Följ stegen nedan för att använda funktionen Camera, med ett Zoom-videomöte som exempel.

1. Innan du ansluter till mötet loggar du in på din KVM på den styrande datorn och går till **Session** -> **Audio & Camera**. Aktivera Camera och klicka sedan på kameraikonen för att starta.

    ![enable camera 1](https://static.gl-inet.com/docs/kvm/faq/use-camera-for-remote-meeting/enable-camera.png){class="glboxshadow"}

    Om ett meddelande om USB-resursgränsen visas när du aktiverar Camera går du till **Settings** -> **USB Devices** och inaktiverar oanvända emulerade USB-enheter för att frigöra resurser. Aktivera sedan Camera och försök igen.

    ![enable camera 3](https://static.gl-inet.com/docs/kvm/faq/use-camera-for-remote-meeting/enable-camera-3.png){class="glboxshadow"}

    Webbläsaren kan be om åtkomst till kameran. Välj den kamera du vill använda, kontrollera videoförhandsvisningen och tillåt åtkomst.

    ![enable camera 2](https://static.gl-inet.com/docs/kvm/faq/use-camera-for-remote-meeting/enable-camera-2.png){class="glboxshadow"}

2. Öppna Zoom och anslut till ett möte på den styrda datorn. Klicka på pilen bredvid videoknappen och välj **UVC camera**.

    ![uvc-camera](https://static.gl-inet.com/docs/kvm/faq/use-camera-for-remote-meeting/uvc-camera.png){class="glboxshadow"}

    Slå sedan på videon så att andra deltagare kan se bilden från den styrande enhetens kamera.

    **Obs!** Se till att ha en stabil nätverksanslutning för jämn och tydlig video under mötet.

## Felsökning {#troubleshooting}

??? note "Vad gör jag om kamerabilden inte når den styrda datorn?"

    Kontrollera om den styrda datorn känner igen KVM-enhetens virtuella kamera.

    Gå till **Settings** -> **Bluetooth & devices** -> **Cameras** på den styrda datorn och leta efter UVC Camera under Connected cameras.

    ![check camera settings](https://static.gl-inet.com/docs/kvm/faq/use-camera-for-remote-meeting/check-camera-settings.png){class="glboxshadow"}

    Om den inte visas kan USB-dataanslutningen mellan KVM-enheten och den styrda datorn vara frånkopplad eller lös.

??? note "Vad gör jag om meddelandet 'Camera Access Denied' visas när jag aktiverar Camera i KVM-konsolen?"

    ![camera access denied](https://static.gl-inet.com/docs/kvm/faq/use-camera-for-remote-meeting/camera-access-denied.png){class="glboxshadow"}

    Kontrollera följande på den styrande datorn:

    - **Kamerans tillgänglighet**: Kontrollera att kameran är ansluten och fungerar. Testa den med systemets kameraapp och stäng sedan appen innan du försöker igen.

    - **Systembehörigheter**: I Windows 11 går du till Settings -> Privacy & security -> Camera och aktiverar följande alternativ: Camera access, Let apps access your camera och Let desktop apps access your camera.

    - **Webbläsarbehörigheter**: Tillåt att KVM-webbplatsen får åtkomst till kameran. Om åtkomsten tidigare blockerats uppdaterar du webbplatsens kamerabehörigheter och laddar om sidan.

    - **Kameraanvändning**: Stäng andra appar eller webbläsarflikar som kan använda kameran, som Zoom eller Microsoft Teams.

    Aktivera Camera i KVM-konsolen igen efter dessa kontroller.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
