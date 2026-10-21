# Så delar du filer mellan styrande och styrda enheter {#how-to-share-files-between-controlling-and-controlled-devices}

GL.iNet KVM emulerar en USB-enhet med läs- och skrivåtkomst, så att du kan dela och hantera filer mellan den styrande och den styrda enheten.

I stegen nedan används Comet (GL-RM1) som exempel.

## Skicka filer till den styrda enheten {#send-files-to-controlled-device}

Följ stegen nedan för att dela filer från den styrande enheten till den styrda enheten.

1. Gå till **Virtual Media** i konsolen. Dra filer till rutan eller klicka på den för att ladda upp filer från den styrande enheten, eller ladda upp från en URL.

    När filerna har laddats upp visas de enligt nedan.

    ![Ladda upp filer](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/file-sharing1.png){class="glboxshadow"}

2. Klicka på **Mount To Remote** -> **File Sharing**.

    ![Fildelning](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/file-sharing2.png){class="glboxshadow"}

3. Ett fönster med stegen för fildelning visas i konsolen, enligt bilden nedan.

    ![Tips om fildelning](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/file-sharing3.png){class="glboxshadow"}

4. Vänta ett ögonblick, så visas en enhet med namnet **"GLKVM"** automatiskt på skärmen. Comet emulerar nu en USB-enhet med läs- och skrivåtkomst på den styrda enheten, och du ser att filerna som du tidigare laddade upp har delats med den styrda enheten.

    Nu kan du visa, flytta eller ta bort filerna på den här enheten från den styrda enheten.

    ![Filen har delats](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/file-sharing4.png){class="glboxshadow"}

    **Tips!** Om enheten inte visas automatiskt öppnar du **This PC** på den styrda enheten.

    ![Den här datorn](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/thispc.png){class="glboxshadow"}

    Leta upp enheten med namnet **"GLKVM"**. Nu kan du visa, flytta eller ta bort filerna på den här enheten.

5. Om du vill sluta dela klickar du på **Virtual Media** i verktygsfältet och klickar på **Stop Sharing**.

    ![Sluta dela](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/stop-sharing1.png){class="glboxshadow"}

## Hämta filer från den styrda enheten {#get-files-from-controlled-device}

Följ stegen nedan för att ta emot filer från den styrda enheten.

1. Flytta eller kopiera filerna som du vill dela till enheten **GLKVM** på den styrda enheten.

    Som bilden nedan visar har en fil flyttats från den styrda enhetens skrivbord till disken **GLKVM**.

    ![Kopiera filen till disken](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/file-sharing5.png){class="glboxshadow"}

2. Gå till Comets konsol, klicka på **Virtual Media** i verktygsfältet och klicka på **Stop Sharing**.

    ![Sluta dela](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/stop-sharing2.png){class="glboxshadow"}

3. Filen visas sedan under **Virtual Media** enligt nedan. Nu kan du ladda ned filen från Comet till den styrande enheten.

    ![Filen har delats](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/file-sharing6.png){class="glboxshadow"}

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
