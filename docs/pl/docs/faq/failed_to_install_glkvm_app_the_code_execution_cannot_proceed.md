# Nie można zainstalować aplikacji GLKVM w Windows: „The code execution cannot proceed” {#failed-to-install-glkvm-app-on-windows-the-code-execution-cannot-proceed}

Podczas instalacji aplikacji GLKVM w systemie Windows może wystąpić błąd: „The code execution cannot proceed because VCRUNTIME140_1.dll was not found”.

![Błąd systemowy](https://static.gl-inet.com/docs/kvm/faq/failed_to_install_glkvm_app/system_error.png){class="glboxshadow"}

Przyczyną błędu jest brak bibliotek środowiska uruchomieniowego Visual C++. Aplikacja wymaga określonych plików DLL dostarczanych w pakiecie Visual C++ Redistributable.

Wykonaj poniższe czynności:

1. Pobierz najnowszy pakiet Visual C++ Redistributable dla Visual Studio z oficjalnej strony Microsoft dostępnej [tutaj](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170){target="_blank"}.

2. Zainstaluj pakiet i uruchom ponownie komputer.

    Tymczasowo wyłącz oprogramowanie antywirusowe, ponieważ niektóre narzędzia zabezpieczające mogą błędnie blokować pliki instalacyjne.

    ??? "Jak sprawdzić, czy biblioteki Visual C++ są prawidłowo zainstalowane?"

        1. W systemie Windows przejdź do Control Panel > Programs > Programs and Features.

        2. Poszukaj pozycji takich jak „Microsoft Visual C++ 2015-2022 Redistributable” (x64/x86). Jeśli ich nie ma, zainstaluj je za pomocą powyższego odnośnika.

3. Ponownie uruchom instalator aplikacji GLKVM.

---

Masz jeszcze pytania? Odwiedź nasze [forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
