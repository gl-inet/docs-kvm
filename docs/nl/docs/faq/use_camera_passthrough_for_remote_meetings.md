# Hoe kan ik de lokale camera delen in vergaderingen op afstand? (Camera Passthrough) {#how-can-i-share-the-local-camera-with-remote-meetings-camera-passthrough}

**Opmerking**: Deze functie is geïntroduceerd in firmware v1.10.0 en wordt alleen ondersteund in de modus WebRTC (FEC). De functie is momenteel beschikbaar via webbrowsers en de desktopclient, maar wordt nog niet ondersteund in de mobiele app.

---

Wanneer u thuiswerkt, kunt u via de KVM toegang krijgen tot uw kantoorcomputer en daar deelnemen aan een videovergadering in Zoom, Microsoft Teams of een vergelijkbare app. De camera toont mogelijk echter alleen uw kantoor en niet uzelf.

Met de functie **Camera** van GL.iNet KVM kunt u videobeelden van de camera van uw thuiscomputer als virtuele USB-camera naar uw kantoorcomputer verzenden. Selecteer deze camera in de vergaderapp zodat andere deelnemers u kunnen zien terwijl u bestanden of toepassingen van uw kantoorcomputer deelt.

## Snelle installatie {#quick-setup}

Volg de onderstaande stappen om de functie Camera te gebruiken, met een Zoom-videovergadering als voorbeeld.

1. Meld u vóór deelname aan de vergadering op de besturende computer aan bij uw KVM en ga naar **Session** -> **Audio & Camera**. Schakel Camera in en klik op het camerapictogram om te starten.

    ![enable camera 1](https://static.gl-inet.com/docs/kvm/faq/use-camera-for-remote-meeting/enable-camera.png){class="glboxshadow"}

    Als bij het inschakelen van Camera een melding over de limiet voor USB-bronnen verschijnt, gaat u naar **Settings** -> **USB Devices** en schakelt u ongebruikte geëmuleerde USB-apparaten uit om bronnen vrij te maken. Schakel Camera vervolgens in en probeer het opnieuw.

    ![enable camera 3](https://static.gl-inet.com/docs/kvm/faq/use-camera-for-remote-meeting/enable-camera-3.png){class="glboxshadow"}

    Uw browser vraagt mogelijk om toegang tot de camera. Selecteer de camera die u wilt gebruiken, controleer het videovoorbeeld en sta toegang toe.

    ![enable camera 2](https://static.gl-inet.com/docs/kvm/faq/use-camera-for-remote-meeting/enable-camera-2.png){class="glboxshadow"}

2. Open Zoom en neem deel aan een vergadering op de bestuurde computer. Klik op de pijl naast de videoknop en selecteer **UVC camera**.

    ![uvc-camera](https://static.gl-inet.com/docs/kvm/faq/use-camera-for-remote-meeting/uvc-camera.png){class="glboxshadow"}

    Schakel vervolgens video in zodat andere deelnemers de beelden van de camera van het besturende apparaat kunnen zien.

    **Opmerking**: Zorg voor een stabiele netwerkverbinding voor vloeiende en heldere video tijdens de vergadering.

## Probleemoplossing {#troubleshooting}

??? note "Wat moet ik doen als de camerabeelden de bestuurde computer niet bereiken?"

    Controleer of de bestuurde computer de virtuele camera van de KVM herkent.

    Ga op de bestuurde computer naar **Settings** -> **Bluetooth & devices** -> **Cameras** en zoek UVC Camera onder Connected cameras.

    ![check camera settings](https://static.gl-inet.com/docs/kvm/faq/use-camera-for-remote-meeting/check-camera-settings.png){class="glboxshadow"}

    Als deze niet wordt weergegeven, is de USB-dataverbinding tussen de KVM en de bestuurde computer mogelijk verbroken of losgeraakt.

??? note "Wat moet ik doen als de melding 'Camera Access Denied' verschijnt wanneer ik Camera in de KVM-console inschakel?"

    ![camera access denied](https://static.gl-inet.com/docs/kvm/faq/use-camera-for-remote-meeting/camera-access-denied.png){class="glboxshadow"}

    Controleer het volgende op de besturende computer:

    - **Beschikbaarheid van de camera**: Controleer of de camera is aangesloten en werkt. Test deze met de camera-app van het systeem en sluit de app voordat u het opnieuw probeert.

    - **Systeemmachtigingen**: Ga in Windows 11 naar Settings -> Privacy & security -> Camera en schakel de volgende opties in: Camera access, Let apps access your camera en Let desktop apps access your camera.

    - **Browsermachtigingen**: Geef de KVM-website toegang tot uw camera. Als toegang eerder is geblokkeerd, werkt u de cameramachtigingen van de website bij en vernieuwt u de pagina.

    - **Cameragebruik**: Sluit andere apps of browsertabbladen die de camera mogelijk gebruiken, zoals Zoom of Microsoft Teams.

    Schakel Camera na deze controles opnieuw in de KVM-console in.

---

Hebt u nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
