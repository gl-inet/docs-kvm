# Så installerar du ett operativsystem på den styrda datorn på distans med virtuella medier {#how-to-install-an-os-on-the-controlled-computer-remotely-using-virtual-media}

Den här guiden visar hur du installerar ett operativsystem på den styrda datorn på distans med virtuella medier, en funktion i GL.iNet KVM.

1. Logga in på din GL.iNet KVM och gå till **Virtual Media**.

2. Ladda upp ISO-filen för operativsystemet till Virtual Media.

    ![Ladda upp fil](https://static.gl-inet.com/docs/kvm/tutorials/install_os_remotely/upload_file.png){class="glboxshadow"}

3. När filen har laddats upp klickar du på **Mount To Remote** och väljer **Image mounting** för att montera ISO-avbildningen.

    ![Montering av avbildning](https://static.gl-inet.com/docs/kvm/tutorials/install_os_remotely/image-mounting-1.png){class="glboxshadow"}

    Välj avbildningsfilen och klicka på **Mount Image**.

    ![Montering av avbildning](https://static.gl-inet.com/docs/kvm/tutorials/install_os_remotely/image-mounting-2.png){class="glboxshadow"}

4. Starta om den fjärrstyrda datorn och **tryck omedelbart på rätt tangent** (t.ex. DEL i det här exemplet) under uppstarten för att öppna BIOS/UEFI.

    ![Öppna BIOS](https://static.gl-inet.com/docs/kvm/tutorials/install_os_remotely/enter_bios.png){class="glboxshadow"}

5. Ange **"Glinet Flash Drive 1.00"** som Boot Option #1 i startmenyn.

    ![Ställ in startordning](https://static.gl-inet.com/docs/kvm/tutorials/install_os_remotely/set_boot_option_priority.png){class="glboxshadow"}

6. Spara och avsluta BIOS. Systemet startar sedan från den monterade ISO-filen och påbörjar installationen av operativsystemet.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
