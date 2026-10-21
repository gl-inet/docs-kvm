# Bestanden delen tussen het besturende en het bestuurde apparaat {#how-to-share-files-between-controlling-and-controlled-devices}

De GL.iNet KVM emuleert een USB-stick met lees- en schrijftoegang, zodat u bestanden kunt delen en beheren tussen het besturende en het bestuurde apparaat.

In de volgende stappen gebruiken we de Comet (GL-RM1) als voorbeeld.

## Bestanden naar het bestuurde apparaat sturen {#send-files-to-controlled-device}

Volg de onderstaande stappen om bestanden van het besturende apparaat met het bestuurde apparaat te delen.

1. Ga in de console naar **Virtual Media**. Sleep bestanden naar het vak of klik op het vak om bestanden van uw besturende apparaat te uploaden, of upload ze via een URL.

    Na het uploaden worden de bestanden als volgt weergegeven.

    ![Bestanden uploaden](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/file-sharing1.png){class="glboxshadow"}

2. Klik op **Mount To Remote** -> **File Sharing**.

    ![Bestanden delen](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/file-sharing2.png){class="glboxshadow"}

3. In de console verschijnt een venster met de stappen voor het delen van bestanden, zoals hieronder weergegeven.
    
    ![Tips voor het delen van bestanden](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/file-sharing3.png){class="glboxshadow"}

4. Even later verschijnt automatisch een station met de naam **"GLKVM"** op het scherm. De Comet emuleert nu een USB-stick met lees- en schrijftoegang op het bestuurde apparaat, en u ziet dat de bestanden die u eerder hebt geüpload met het bestuurde apparaat zijn gedeeld.

    U kunt de bestanden in dit station nu op het bestuurde apparaat bekijken, verplaatsen of verwijderen.

    ![Bestand gedeeld](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/file-sharing4.png){class="glboxshadow"}
    
    **Tip**: Als het station niet automatisch verschijnt, gaat u op het bestuurde apparaat naar **This PC**.

    ![Deze pc](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/thispc.png){class="glboxshadow"}

    Zoek het station met de naam **"GLKVM"**. U kunt de bestanden in dit station nu bekijken, verplaatsen of verwijderen.

5. Als u wilt stoppen met delen, klikt u in de werkbalk op **Virtual Media** en vervolgens op **Stop Sharing**.

    ![Delen stoppen](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/stop-sharing1.png){class="glboxshadow"}

## Bestanden van het bestuurde apparaat ophalen {#get-files-from-controlled-device}

Volg de onderstaande stappen om bestanden van het bestuurde apparaat te ontvangen.

1. Verplaats of kopieer op het bestuurde apparaat de bestanden die u wilt delen naar het station **GLKVM**.

    Zoals hieronder te zien is, is een bestand van het bureaublad van het bestuurde apparaat naar de schijf **GLKVM** verplaatst.

    ![Bestand naar schijf kopiëren](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/file-sharing5.png){class="glboxshadow"}
    
2. Ga naar de console van de Comet, klik in de werkbalk op **Virtual Media** en klik op **Stop Sharing**.

    ![Delen stoppen](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/stop-sharing2.png){class="glboxshadow"}
    
3. Het bestand wordt dan als volgt onder **Virtual Media** weergegeven. U kunt dit bestand nu van de Comet naar uw besturende apparaat downloaden.

    ![Bestand gedeeld](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/file-sharing6.png){class="glboxshadow"}

---

Hebt u nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
