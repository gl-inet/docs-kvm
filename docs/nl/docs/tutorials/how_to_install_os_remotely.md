# Op afstand een besturingssysteem installeren op de bestuurde computer met virtuele media {#how-to-install-an-os-on-the-controlled-computer-remotely-using-virtual-media}

In deze handleiding leest u hoe u op afstand een besturingssysteem op de bestuurde computer installeert met virtuele media, een functie van de GL.iNet KVM.

1. Meld u aan bij uw GL.iNet KVM en ga naar **Virtual Media**.

2. Upload het ISO-bestand van het besturingssysteem naar Virtual Media.

    ![Bestand uploaden](https://static.gl-inet.com/docs/kvm/tutorials/install_os_remotely/upload_file.png){class="glboxshadow"}

3. Klik na het uploaden op **Mount To Remote** en selecteer **Image mounting** om het ISO-image te koppelen.

    ![Image koppelen](https://static.gl-inet.com/docs/kvm/tutorials/install_os_remotely/image-mounting-1.png){class="glboxshadow"}

    Selecteer het imagebestand en klik op **Mount Image**.

    ![Image koppelen](https://static.gl-inet.com/docs/kvm/tutorials/install_os_remotely/image-mounting-2.png){class="glboxshadow"}

4. Start de op afstand bestuurde computer opnieuw op en **druk tijdens het opstarten direct op de juiste toets** (in dit voorbeeld DEL) om het BIOS/UEFI te openen.

    ![BIOS openen](https://static.gl-inet.com/docs/kvm/tutorials/install_os_remotely/enter_bios.png){class="glboxshadow"}

5. Stel in het opstartmenu **"Glinet Flash Drive 1.00"** in als Boot Option #1.

    ![Opstartvolgorde instellen](https://static.gl-inet.com/docs/kvm/tutorials/install_os_remotely/set_boot_option_priority.png){class="glboxshadow"}

6. Sla de instellingen op en sluit het BIOS af. Het systeem start dan op vanaf het gekoppelde ISO-image en de installatie van het besturingssysteem begint.

---

Hebt u nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
