# Jak udostępniać pliki między urządzeniem sterującym a sterowanym {#how-to-share-files-between-controlling-and-controlled-devices}

GL.iNet KVM emuluje dysk USB z możliwością odczytu i zapisu, dzięki czemu można udostępniać pliki i zarządzać nimi między urządzeniem sterującym a sterowanym.

W poniższych krokach użyto Comet (GL-RM1) jako przykładu.

## Wysyłanie plików do sterowanego urządzenia {#send-files-to-controlled-device}

Aby udostępnić pliki z urządzenia sterującego urządzeniu sterowanemu, wykonaj poniższe kroki.

1. W konsoli przejdź do **Virtual Media**. Przeciągnij pliki do pola lub kliknij je, aby przesłać pliki z urządzenia sterującego. Możesz też przesłać pliki z adresu URL.

    Po przesłaniu pliki będą wyświetlane w następujący sposób.

    ![Przesyłanie plików](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/file-sharing1.png){class="glboxshadow"}

2. Kliknij **Mount To Remote** -> **File Sharing**.

    ![Udostępnianie plików](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/file-sharing2.png){class="glboxshadow"}

3. W konsoli pojawi się okno z instrukcją udostępniania plików, jak pokazano poniżej.

    ![Instrukcja udostępniania](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/file-sharing3.png){class="glboxshadow"}

4. Po chwili na ekranie automatycznie pojawi się dysk o nazwie **„GLKVM”**. Comet emuluje teraz na sterowanym urządzeniu dysk USB z możliwością odczytu i zapisu. Wcześniej przesłane pliki będą dostępne na tym urządzeniu.

    Na sterowanym urządzeniu możesz teraz przeglądać, przenosić i usuwać pliki z tego dysku.

    ![Udostępnione pliki](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/file-sharing4.png){class="glboxshadow"}

    **Wskazówka**: Jeśli dysk nie pojawi się automatycznie, otwórz **This PC** na sterowanym urządzeniu.

    ![This PC](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/thispc.png){class="glboxshadow"}

    Znajdź dysk o nazwie **„GLKVM”**. Możesz teraz przeglądać, przenosić i usuwać znajdujące się na nim pliki.

5. Aby zakończyć udostępnianie, kliknij **Virtual Media** na pasku narzędzi, a następnie **Stop Sharing**.

    ![Zatrzymywanie udostępniania](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/stop-sharing1.png){class="glboxshadow"}

## Pobieranie plików ze sterowanego urządzenia {#get-files-from-controlled-device}

Aby odebrać pliki ze sterowanego urządzenia, wykonaj poniższe kroki.

1. Na sterowanym urządzeniu przenieś lub skopiuj pliki do udostępnienia na dysk **GLKVM**.

    Poniższy przykład pokazuje plik przeniesiony z pulpitu sterowanego urządzenia na dysk **GLKVM**.

    ![Kopiowanie pliku na dysk](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/file-sharing5.png){class="glboxshadow"}

2. Wróć do konsoli Comet, kliknij **Virtual Media** na pasku narzędzi, a następnie **Stop Sharing**.

    ![Zatrzymywanie udostępniania](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/stop-sharing2.png){class="glboxshadow"}

3. Plik pojawi się w **Virtual Media**, jak pokazano poniżej. Możesz go teraz pobrać z Comet na urządzenie sterujące.

    ![Plik gotowy do pobrania](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/file-sharing6.png){class="glboxshadow"}

---

Masz pytania? Odwiedź nasze [forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
