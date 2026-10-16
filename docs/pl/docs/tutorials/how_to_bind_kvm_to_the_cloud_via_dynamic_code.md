# Jak powiązać KVM z chmurą za pomocą kodu dynamicznego

> Uwaga: Przed użyciem tej funkcji zaktualizuj firmware KVM do wersji 1.7.

Ten poradnik pokazuje, jak łatwo powiązać GL.iNet KVM z chmurą za pomocą kodu dynamicznego.

## Kroki powiązania

1. Zaloguj się lokalnie do GL.iNet KVM, używając nazwy domenowej lub adresu IP. Szczegóły znajdziesz [tutaj](../faq/local_access_via_browser.md).

2. Po zalogowaniu przejdź do **Cloud Service** w prawym górnym rogu i kliknij **Bind With Code**.

    ![Powiązanie za pomocą kodu — krok 1](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_1.png){class="glboxshadow"}

3. Zostanie wygenerowany losowy, 8-cyfrowy kod dynamiczny do powiązania urządzenia, ważny przez 60 sekund. Kliknij kod, aby go skopiować.

    ![Powiązanie za pomocą kodu — krok 2](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_2.png){class="glboxshadow"}

4. Otwórz [https://glkvm.com/](https://glkvm.com/){target="_blank"} i zaloguj się na konto chmurowe GL.iNet.

    ![Logowanie do chmury](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_3.png){class="glboxshadow"}

5. Po zalogowaniu zobaczysz następującą stronę.

    ![Strona po zalogowaniu](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_4.png){class="glboxshadow"}

    Kliknij **Add Device** i wybierz **Bind with Code**.

    ![Dodawanie urządzenia](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_5.png){class="glboxshadow"}

6. W wyskakującym oknie wpisz 8-cyfrowy kod dynamiczny i kliknij **Bind**.

    ![Wpisywanie kodu](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_6.png){class="glboxshadow"}

    **Uwaga**: Kod dynamiczny jest ważny przez 60 sekund. Jeśli wygaśnie, wróć do konsoli KVM i kliknij **Regenerate Code**, aby uzyskać nowy kod.

    ![Generowanie nowego kodu](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/regenerate_code.png){class="glboxshadow"}

7. Urządzenie zostanie powiązane z kontem chmurowym. Kliknij **Done**.

    ![Pomyślne powiązanie](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_7.png){class="glboxshadow"}

    KVM pojawi się na liście urządzeń. Możesz teraz uzyskiwać do niego zdalny dostęp przez usługę chmurową.

    ![Lista urządzeń](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_8.png){class="glboxshadow"}

8. Kliknij urządzenie, do którego chcesz uzyskać zdalny dostęp. Na nowo otwartej stronie wpisz hasło administratora, aby się zalogować.

    ![Logowanie administratora](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_3.png){class="glboxshadow"}

    Uzyskasz zdalny dostęp do KVM i sterowanego urządzenia przez chmurę.

    ![Zdalny dostęp przez chmurę](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_4.png){class="glboxshadow"}

## Najczęstsze pytania

1. **P: Jak długo kod dynamiczny jest ważny? Co zrobić, jeśli wygaśnie?**

    O: Kod dynamiczny jest ważny przez 60 sekund. Jeśli wygaśnie, wróć do konsoli KVM i kliknij **Regenerate Code**, aby uzyskać nowy kod.

    ![Generowanie nowego kodu](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/regenerate_code.png){class="glboxshadow"}

2. **P: Co zrobić, jeśli nie można wygenerować kodu dynamicznego?**

    O: Przyczyną może być niestabilne połączenie sieciowe lub konfiguracja nadrzędnego serwera DNS.

    - Sprawdź stabilność sieci lub przełącz się na inną sieć i spróbuj ponownie.

    - Zmień ustawienia nadrzędnego serwera DNS i ponownie wygeneruj kod.

    Jeśli problem nadal występuje, skontaktuj się z pomocą techniczną: [support@gl-inet.com](mailto:support@gl-inet.com).

---

Masz pytania? Odwiedź nasze [forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
