# Jak zdalnie zainstalować system operacyjny na sterowanym komputerze za pomocą Virtual Media

Ten poradnik pokazuje, jak zdalnie zainstalować system operacyjny na sterowanym komputerze za pomocą funkcji Virtual Media w GL.iNet KVM.

1. Zaloguj się do GL.iNet KVM i przejdź do **Virtual Media**.

2. Prześlij plik ISO systemu operacyjnego do Virtual Media.

    ![Przesyłanie pliku](https://static.gl-inet.com/docs/kvm/tutorials/install_os_remotely/upload_file.png){class="glboxshadow"}

3. Po przesłaniu kliknij **Mount To Remote** i wybierz **Image mounting**, aby zamontować obraz ISO.

    ![Montowanie obrazu](https://static.gl-inet.com/docs/kvm/tutorials/install_os_remotely/image-mounting-1.png){class="glboxshadow"}

    Wybierz plik obrazu i kliknij **Mount Image**.

    ![Wybór pliku obrazu](https://static.gl-inet.com/docs/kvm/tutorials/install_os_remotely/image-mounting-2.png){class="glboxshadow"}

4. Uruchom zdalnie sterowany komputer ponownie i podczas rozruchu **od razu naciśnij odpowiedni klawisz** (np. DEL w tym przykładzie), aby wejść do BIOS/UEFI.

    ![Wejście do BIOS](https://static.gl-inet.com/docs/kvm/tutorials/install_os_remotely/enter_bios.png){class="glboxshadow"}

5. W menu rozruchowym ustaw **„Glinet Flash Drive 1.00”** jako Boot Option #1.

    ![Ustawianie kolejności rozruchu](https://static.gl-inet.com/docs/kvm/tutorials/install_os_remotely/set_boot_option_priority.png){class="glboxshadow"}

6. Zapisz zmiany i wyjdź z BIOS. Komputer uruchomi się z zamontowanego obrazu ISO i rozpocznie instalację systemu.

---

Masz pytania? Odwiedź nasze [forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
