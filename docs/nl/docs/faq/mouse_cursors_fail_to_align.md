# Wat moet ik doen als de muisaanwijzers niet samenvallen? {#what-should-i-do-if-mouse-cursors-fail-to-align}

Als de muisaanwijzer op het besturende apparaat niet samenvalt met de aanwijzer op het bestuurde apparaat, volgt u de onderstaande stappen om het probleem op te lossen.

![Verschoven aanwijzer](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/mouse_cursor.png){class="glboxshadow"}

1. **Controleer of het probleem optreedt wanneer de muis beweegt of stilstaat.**

    <u>Situatie 1</u>. Als de aanwijzers samenvallen wanneer de muis stilstaat, maar tijdens het bewegen uit elkaar lopen, controleer dan het netwerk aan beide kanten en zorg voor een stabiele verbinding.

    Daarnaast kunt u de lokale aanwijzer verbergen, zodat alleen de externe aanwijzer op het bedieningsscherm wordt weergegeven en de aanwijzers niet meer verschoven lijken.

    Ga in de KVM-console naar **Settings** -> **Remote Device Settings** -> **Show Local Cursor** en schakel deze optie uit.

    ![Lokale aanwijzer verbergen](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/hide_local_cursor.jpg){class="glboxshadow"}

    <u>Situatie 2</u>. Als de aanwijzers ook niet samenvallen wanneer de muis stilstaat, selecteert u in de KVM-console opnieuw uw apparaattype (alleen voor Comet Q / GL-RMQ1).
    
    ![Apparaattype](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/device_type.png){class="glboxshadow"}
    
    Als het probleem zich blijft voordoen, gaat u verder met de volgende stap.

2. **Als het bestuurde apparaat een laptop is, wordt het probleem waarschijnlijk veroorzaakt door een onjuiste beeldschermresolutie.**

    Controleer de beeldverhouding van het laptopscherm. Vervolgens kunt u de resolutie op de bestuurde laptop aanpassen of de EDID-instelling van uw KVM-apparaat wijzigen.
    
    ??? note "Resolutie aanpassen op de bestuurde laptop"
    
        **Voor macOS**:

        1. Ga naar **Settings** -> **Displays** -> **Optimize for**.

            ![Beeldschermen op de Mac](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/macos1.png){class="glboxshadow" width="582"}

        2. Wijzig de instelling in **GLKVM**.

            ![GLKVM selecteren](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/macos2.png){class="glboxshadow" width="582"}

        3. Kies de bijbehorende resolutie en controleer of de muisaanwijzers nu samenvallen.

            ![Resolutie](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/macos3.png){class="glboxshadow"}

        **Voor Windows**:

        1. Ga naar **Settings** -> **System** -> **Displays**.

            ![Beeldscherm in Windows](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/windows1.png){class="glboxshadow"}

        2. Scrol omlaag naar **Display resolution** en klik op het vak rechts.

            ![Beeldschermresolutie](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/windows2.png){class="glboxshadow"}

        3. Selecteer de juiste beeldschermresolutie en klik in het pop-upvenster op **Keep changes** om deze toe te passen.

            ![Beeldschermresolutie](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/windows3.png){class="glboxshadow"}

            ![Beeldschermresolutie](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/windows4.png){class="glboxshadow"}

    ??? note "EDID-instelling van uw KVM-apparaat wijzigen"

        EDID, afkorting van Extended Display Identification Data, kiest automatisch de optimale weergaveparameters. De standaard-EDID is geschikt voor de meeste situaties en hoeft doorgaans niet te worden gewijzigd. Zie [hier](../tutorials/how_to_set_edid_for_glkvm.md){target="_blank"} voor meer informatie.
        
        Als de EDID is gewijzigd maar het scherm niet wordt bijgewerkt, start u het bestuurde apparaat opnieuw op.

3. **Als het bestuurde apparaat geen laptop is (bijvoorbeeld een desktop-pc met een externe monitor)**, controleert u de beeldverhouding van het primaire beeldscherm en wijzigt u de EDID van uw KVM dienovereenkomstig. Zie [hier](../tutorials/how_to_set_edid_for_glkvm.md){target="_blank"} voor meer informatie.

---

Hebt u nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
