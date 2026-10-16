# Jak działa wykrywanie sieci WAN i przełączanie awaryjne w Comet 5G {#what-is-the-wan-network-detection-and-failover-logic-of-comet-5g}

1. System wykrywa dostępność za pomocą ping, wysyłając sondy przez wszystkie interfejsy co **3 sekundy** i oceniając warunki przełączenia awaryjnego co **9 sekund**.

2. Jeśli w ciągu **9 sekund** wszystkie testy ping przez interfejs o wyższym priorytecie zakończą się niepowodzeniem, a interfejs o niższym priorytecie pozostanie dostępny, po upływie tego czasu nastąpi przełączenie awaryjne. Jeśli wszystkie interfejsy są niedostępne, przełączenie nie nastąpi.

3. Interfejsy oznaczone jako niedostępne nadal otrzymują sondy ping w tle.

4. Przywracanie: Jeśli interfejs o wyższym priorytecie stanie się osiągalny przez ping w ciągu **9 sekund**, po upływie tego czasu system przełączy się z powrotem na ten interfejs.

---

Masz jeszcze pytania? Odwiedź nasze [forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
