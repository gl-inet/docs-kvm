# Jak odłączyć urządzenie KVM od konta w chmurze {#how-to-unbind-my-kvm-device-from-the-cloud}

Powiązanie urządzeń KVM z chmurą można usunąć na trzy sposoby: przez dostęp lokalny, aplikację GLKVM lub usługę chmurową.

## Usuwanie powiązania przez dostęp lokalny {#unbind-via-local-access}

1. Upewnij się, że komputer znajduje się w tej samej sieci lokalnej co urządzenie KVM.

2. Otwórz przeglądarkę na komputerze (zalecamy Chrome lub Edge ze względu na lepszą zgodność). Wpisz `glkvm.local` lub adres IP KVM w pasku adresu, aby otworzyć lokalną stronę logowania GLKVM. Wpisz hasło administratora, aby się zalogować.

3. Po zalogowaniu przejdź do **Cloud Service** w prawym górnym rogu, kliknij ikonę koła zębatego i wybierz **Unbind**.

    ![Usuwanie powiązania przez dostęp lokalny](https://static.gl-inet.com/docs/kvm/faq/unbind/local_unbind.png){class="glboxshadow"}

## Usuwanie powiązania w aplikacji GLKVM {#unbind-via-glkvm-app}

1. Zaloguj się do aplikacji GLKVM i kliknij **Manage** w prawym górnym rogu kafelka urządzenia.

    ![Usuwanie powiązania w aplikacji](https://static.gl-inet.com/docs/kvm/faq/unbind/app_unbind_1.png){class="glboxshadow"}

2. Kliknij **More** i wybierz **Unbind**.

    ![Potwierdzanie usunięcia powiązania w aplikacji](https://static.gl-inet.com/docs/kvm/faq/unbind/app_unbind_2.png){class="glboxshadow"}

## Usuwanie powiązania w usłudze chmurowej {#unbind-via-the-cloud}

1. Otwórz przeglądarkę na komputerze (zalecamy Chrome lub Edge ze względu na lepszą zgodność). Wpisz `glkvm.com` w pasku adresu i zaloguj się na konto w chmurze.

2. Po zalogowaniu kliknij ikonę trzech kropek w prawym dolnym rogu kafelka urządzenia, a następnie **Device Detail**.

    ![Usuwanie powiązania w chmurze](https://static.gl-inet.com/docs/kvm/faq/unbind/cloud_unbind_1.png){class="glboxshadow"}

3. Na stronie szczegółów kliknij **Unbind**.

    ![Usuwanie powiązania w chmurze](https://static.gl-inet.com/docs/kvm/faq/unbind/cloud_unbind_2.png){class="glboxshadow gl-80-desktop"}

---

Masz jeszcze pytania? Odwiedź nasze [forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
