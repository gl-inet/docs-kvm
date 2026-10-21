# Vad gör jag om muspekarna inte är i linje med varandra? {#what-should-i-do-if-mouse-cursors-fail-to-align}

Om muspekaren på den styrande enheten inte är i linje med muspekaren på den styrda enheten följer du felsökningsstegen nedan.

![Felaktigt justerade pekare](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/mouse_cursor.png){class="glboxshadow"}

1. **Ta reda på om problemet uppstår när musen rör sig eller är stilla.**

    <u>Fall 1</u>. Om pekarna är i linje när musen är stilla men hamnar ur synk när den rör sig kontrollerar du nätverket på båda sidor och ser till att anslutningen är stabil.

    Du kan också dölja den lokala pekaren så att bara fjärrpekaren visas på styrskärmen, vilket förhindrar problem med felaktigt justerade pekare.

    Gå till **Settings** -> **Remote Device Settings** -> **Show Local Cursor** i KVM-konsolen och inaktivera alternativet.

    ![Dölj lokal pekare](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/hide_local_cursor.jpg){class="glboxshadow"}

    <u>Fall 2</u>. Om pekarna inte är i linje ens när musen är stilla väljer du enhetstyp på nytt i KVM-konsolen (gäller endast Comet Q/GL-RMQ1).

    ![Enhetstyp](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/device_type.png){class="glboxshadow"}

    Gå vidare till nästa steg om problemet kvarstår.

2. **Om den styrda enheten är en bärbar dator beror problemet troligen på en felaktig skärmupplösning.**

    Ta reda på den bärbara datorns bildförhållande. Du kan sedan antingen justera upplösningen på den styrda bärbara datorn eller ändra KVM-enhetens EDID-inställning.

    ??? note "Justera upplösningen på den styrda bärbara datorn"

        **För macOS**:

        1. Gå till **Settings** -> **Displays** -> **Optimize for**.

            ![Bildskärmar i macOS](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/macos1.png){class="glboxshadow" width="582"}

        2. Ändra till **GLKVM**.

            ![Välj GLKVM](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/macos2.png){class="glboxshadow" width="582"}

        3. Välj motsvarande upplösning och kontrollera sedan om muspekarna sammanfaller.

            ![Upplösning](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/macos3.png){class="glboxshadow"}

        **För Windows**:

        1. Gå till **Settings** -> **System** -> **Displays**.

            ![Bildskärm i Windows](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/windows1.png){class="glboxshadow"}

        2. Rulla nedåt till **Display resolution** och klicka på rutan till höger.

            ![Skärmupplösning](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/windows2.png){class="glboxshadow"}

        3. Välj lämplig skärmupplösning och klicka sedan på **Keep changes** i popup-fönstret för att tillämpa den.

            ![Skärmupplösning](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/windows3.png){class="glboxshadow"}

            ![Skärmupplösning](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/windows4.png){class="glboxshadow"}

    ??? note "Ändra KVM-enhetens EDID-inställning"

        EDID, förkortning för Extended Display Identification Data, matchar automatiskt de optimala visningsparametrarna. Standard-EDID passar de flesta scenarier och behöver i regel inte ändras. Mer information finns [här](../tutorials/how_to_set_edid_for_glkvm.md){target="_blank"}.

        Om EDID har ändrats men skärmen inte uppdateras kan du prova att starta om den styrda enheten.

3. **Om den styrda enheten inte är en bärbar dator (t.ex. en stationär dator ansluten till en extern skärm)** tar du reda på bildförhållandet för den primära skärmen och byter sedan EDID för din KVM i enlighet med det. Mer information finns [här](../tutorials/how_to_set_edid_for_glkvm.md){target="_blank"}.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
