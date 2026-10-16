# Jak uzyskać zdalny dostęp do KVM przez chmurę {#how-to-access-kvm-remotely-via-cloud}

Przed rozpoczęciem upewnij się, że:

- Urządzenie docelowe jest prawidłowo podłączone do KVM.

- KVM ma stabilne połączenie sieciowe.

- Możesz uzyskać lokalny dostęp do KVM, ponieważ powiązanie urządzenia z chmurą musi zostać wykonane w sieci lokalnej.

Wykonaj poniższe czynności, aby uzyskać zdalny dostęp do KVM i urządzenia docelowego przez usługę chmurową.

## Powiązanie KVM z chmurą {#bind-your-kvm-to-the-cloud}

KVM można powiązać z chmurą na dwa sposoby: standardowo lub za pomocą kodu dynamicznego.

- **Powiązanie standardowe**: Kliknij „Bind To KVMCloud” w konsoli KVM. Nastąpi przekierowanie do strony powiązania z tokenem. Zaloguj się na konto w chmurze i potwierdź informacje o urządzeniu, aby ukończyć powiązanie.

- **Powiązanie kodem dynamicznym**: Kliknij „Bind With Code” w konsoli KVM, aby wygenerować losowy 8-cyfrowy kod do powiązania urządzenia. Zaloguj się na konto w chmurze i wpisz kod, aby ukończyć powiązanie.

### Powiązanie standardowe {#regular-binding}

Zaloguj się lokalnie do KVM za pomocą adresu IP lub nazwy domeny i przejdź do **Cloud Service** w prawym górnym rogu. Kliknij **Bind To Cloud**.

![Powiązanie z chmurą](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_to_cloud.png){class="glboxshadow"}

Nastąpi przekierowanie do strony logowania. Wpisz dane konta GL.iNet i kliknij **Log In**.

![Logowanie w celu powiązania urządzenia](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_1.png){class="glboxshadow"}

Potwierdź informacje o urządzeniu i kliknij **Bind**.

![Potwierdzanie powiązania urządzenia](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_2.png){class="glboxshadow"}

Poczekaj chwilę, aż urządzenie zostanie powiązane z kontem. Kliknij **Done**.

![Urządzenie zostało powiązane](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_3.png){class="glboxshadow"}

### Powiązanie kodem dynamicznym {#dynamic-code-binding}

Uwaga: Przed użyciem tej funkcji zaktualizuj oprogramowanie sprzętowe KVM do wersji 1.7.

1. Zaloguj się lokalnie do GL.iNet KVM za pomocą nazwy domeny lub adresu IP. Szczegóły znajdziesz [tutaj](../faq/local_access_via_browser.md).

2. Po zalogowaniu przejdź do **Cloud Service** w prawym górnym rogu i kliknij **Bind With Code**.

    ![Powiązanie kodem — krok 1](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_1.png){class="glboxshadow"}

3. Zostanie wygenerowany losowy 8-cyfrowy kod do powiązania urządzenia, ważny przez 60 sekund. Kliknij kod, aby go skopiować.

    ![Powiązanie kodem — krok 2](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_2.png){class="glboxshadow"}

4. Otwórz [https://glkvm.com/](https://glkvm.com/){target="_blank"} i zaloguj się na konto GL.iNet w chmurze.

    ![Powiązanie kodem — krok 3](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_3.png){class="glboxshadow"}

5. Po zalogowaniu strona będzie wyglądać jak poniżej.

    ![Powiązanie kodem — krok 4](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_4.png){class="glboxshadow"}

    Kliknij **Add Device** i wybierz **Bind with Code**.

    ![Powiązanie kodem — krok 5](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_5.png){class="glboxshadow"}

6. W wyświetlonym oknie wpisz 8-cyfrowy kod dynamiczny i kliknij **Bind**.

    ![Powiązanie kodem — krok 6](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_6.png){class="glboxshadow"}

    **Uwaga**: Kod dynamiczny jest ważny przez 60 sekund. Jeśli wygaśnie, wróć do konsoli KVM i kliknij **Regenerate Code**, aby uzyskać nowy.

    ![Ponowne generowanie kodu](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/regenerate_code.png){class="glboxshadow"}

    Urządzenie zostanie powiązane z kontem w chmurze.

## Dostęp zdalny przez chmurę {#remote-access-via-cloud}

Otwórz przeglądarkę (np. Google Chrome) i wpisz `glkvm.com` w pasku adresu. Pojawi się strona logowania. Zaloguj się na konto GL.iNet.

![Logowanie do dostępu zdalnego](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_1.png){class="glboxshadow"}

Po zalogowaniu zobaczysz urządzenia powiązane z kontem. Kliknij urządzenie, do którego chcesz uzyskać dostęp zdalny.

![Wybór urządzenia do dostępu zdalnego](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_2.jpg){class="glboxshadow"}

Na nowo otwartej stronie wpisz hasło administratora, aby się zalogować.

![Logowanie administratora do dostępu zdalnego](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_3.png){class="glboxshadow"}

Możesz teraz uzyskać zdalny dostęp do KVM i urządzenia docelowego przez chmurę.

![Dostęp zdalny został nawiązany](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_4.png){class="glboxshadow"}

---

Masz jeszcze pytania? Odwiedź nasze [forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
