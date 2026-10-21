# Jak zmienić nazwę hosta KVM {#how-to-change-kvm-hostname}

Domyślna nazwa hosta GL.iNet KVM to **glkvm**. Gdy urządzenia są połączone z tą samą siecią, możesz uzyskać lokalny dostęp do KVM pod adresem `glkvm.local`.

Ten poradnik przedstawia dwie metody zmiany nazwy hosta: w konsoli KVM i za pomocą poleceń terminala.

## Metoda 1. Konsola KVM {#method-1-kvm-console}

> **Uwaga**: Ta funkcja jest dostępna w firmware w wersji 1.7.0 i nowszych.

### Firmware v1.10 i nowszy {#firmware-v110-and-above}

1. Zaloguj się do KVM i kliknij ikonę ustawień na pasku nawigacji, aby otworzyć stronę ustawień.

    ![Ustawienia sieci](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/settings-network.png){class="glboxshadow"}

2. Przejdź do **Network** i wpisz własną nazwę hosta. Zmiana zostanie zastosowana.

    ![Zmiana nazwy hosta](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/modify-hostname.png){class="glboxshadow"}

### Firmware v1.9 i starszy {#firmware-v19-and-earlier}

1. Zaloguj się do KVM i przejdź do **Settings** -> **Network**. Kliknij nazwę hosta lub ikonę strzałki w prawo.

    ![Ustawienia sieci](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/settings_network.png){class="glboxshadow"}

2. Wpisz własną nazwę hosta i kliknij **Apply**.

    ![Wpisywanie nazwy hosta](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/modify_hostname.png){class="glboxshadow"}

## Metoda 2. Polecenia terminala {#method-2-terminal-commands}

1. Zaloguj się do KVM i przejdź do **Toolbox** -> **Terminal**. Kliknij **Access**.

    ![Dostęp do terminala](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/access_terminal.png){class="glboxshadow"}

2. W terminalu wpisz poniższe polecenie i naciśnij Enter (zastąp „example” wybraną nazwą hosta). KVM zostanie uruchomiony ponownie.

    `echo example > /etc/hostname && reboot`

    ![Wpisywanie polecenia](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/input_command.png){class="glboxshadow"}

3. Poczekaj na ponowne uruchomienie. Następnie możesz uzyskać dostęp do KVM przy użyciu nowej nazwy hosta.

    ![Dostęp przez nową nazwę hosta](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/access_new_hostname.png){class="glboxshadow"}

    Jeśli zapomnisz nazwę hosta lub chcesz sprawdzić, czy zmiana została zastosowana, wpisz w terminalu poniższe polecenie, aby wyświetlić bieżącą nazwę.

    `cat /etc/hostname`

    ![Sprawdzanie nazwy hosta](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/verify_hostname.png){class="glboxshadow"}

---

Masz pytania? Odwiedź nasze [forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
