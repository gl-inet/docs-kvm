# Så ändrar du KVM-enhetens värdnamn {#how-to-change-kvm-hostname}

Standardvärdnamnet för GL.iNet KVM är **glkvm**, vilket innebär att du kan komma åt enheten lokalt via domänen `glkvm.local` när du är ansluten till samma nätverk.

Den här guiden beskriver två sätt att ändra värdnamnet: via KVM-konsolen eller med terminalkommandon.

## Metod 1. KVM-konsolen {#method-1-kvm-console}

> **Obs!** Funktionen finns i firmwareversion 1.7.0 och senare.

### Firmware v1.10 och senare {#firmware-v110-and-above}

1.  Logga in på din KVM och klicka på inställningsikonen i navigeringsfältet för att öppna inställningssidan.

    ![Nätverksinställningar](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/settings-network.png){class="glboxshadow"}

2. Gå till **Network** och ange ditt anpassade värdnamn, så träder ändringen i kraft.

    ![Ändra värdnamn](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/modify-hostname.png){class="glboxshadow"}

### Firmware v1.9 och tidigare {#firmware-v19-and-earlier}

1. Logga in på din KVM och gå till **Settings** -> **Network**. Klicka på värdnamnet eller högerpilen.

    ![Nätverksinställningar](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/settings_network.png){class="glboxshadow"}

2. Anpassa värdnamnet och klicka på **Apply**.

    ![Ändra värdnamn](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/modify_hostname.png){class="glboxshadow"}

## Metod 2. Terminalkommandon {#method-2-terminal-commands}

1. Logga in på din KVM och gå till **Toolbox** -> **Terminal**. Klicka på **Access**.

    ![Öppna terminalen](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/access_terminal.png){class="glboxshadow"}

2. Ange följande kommando i terminalen och tryck på Enter (ersätt "example" med önskat värdnamn). KVM-enheten startas sedan om.

    `echo example > /etc/hostname && reboot`

    ![Ange kommandot](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/input_command.png){class="glboxshadow"}

3. Vänta tills enheten har startat om. Därefter kan du komma åt din KVM med det nya värdnamnet.

    ![Åtkomst med nytt värdnamn](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/access_new_hostname.png){class="glboxshadow"}

    Om du glömmer värdnamnet eller behöver kontrollera att ändringen har trätt i kraft anger du följande kommando i terminalen för att visa det aktuella värdnamnet.

    `cat /etc/hostname`

    ![Verifiera värdnamnet](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/verify_hostname.png){class="glboxshadow"}

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
