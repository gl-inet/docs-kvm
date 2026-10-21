# Polish Translation Rules

- Write natural, professional Polish suitable for official technical support documentation.
- Address the reader with second-person singular imperatives throughout (`kliknij`, `wybierz`, `możesz`). Use `należy` only for general requirements, not as the default instruction style.
- Always use Polish diacritics (`ą ć ę ł ń ó ś ź ż`); never write ASCII substitutes such as `haslo` or `urzadzenie`.
- Remove machine-translation artifacts completely. Do not leave Chinese, Japanese, Korean, Russian, or partially untranslated English in Polish prose.

## Polish Terminology

- Keep product names, model names, protocol names, and brand names unchanged: `GL.iNet`, `GLKVM`, `KVM`, `Comet`, `Comet Pro`, `Comet PoE`, `Comet 5G`, `Comet Q`, `Comet X`, `Tailscale`, `ZeroTier`, `NetBird`, `HDMI`, `USB`, `USB-C`, `BIOS`, `EDID`, `LAN`, `WAN`, `IP`, `STUN`.
- Prefer `urządzenie KVM` when a plain `KVM` would be awkward to decline.
- Prefer `dostęp zdalny` for `remote access` and `dostęp lokalny` for `local access`.
- Prefer `urządzenie sterujące` for `controlling device`, `urządzenie sterowane` for `controlled device`, and `urządzenie docelowe` for `target device`.
- Prefer `nośniki wirtualne` for `virtual media`.
- Prefer `konsola szeregowa` for `serial console`.
- Use `firmware` in headings and navigation (`Aktualizacja firmware`); `oprogramowanie układowe` is acceptable in prose. Keep one form within a paragraph.
- Prefer `powiązać` and `odłączyć od konta` for cloud account binding and unbinding.
- Prefer `przywrócić działanie KVM` for `unbrick`.
- Admonition titles: `Uwaga`, `Wskazówka`, `Ostrzeżenie`.

## UI and Navigation

- Preserve actual product UI labels when they appear in screenshots or navigation paths.
- For navigation paths, keep the structure exactly as in the English source, for example: `**System** -> **Upgrade**`.
- If a button or menu label is visibly English in the UI, keep the label in English, for example `**Absolute Mode**` or `**Bind To Cloud**`. Decline the surrounding Polish words instead of the label (`w trybie Absolute`).
- Do not invent Polish UI labels that are not shown in the product.
- Do not create or sync regulatory statement pages (`regulatory_statement.md`, `fcc_ic_compliance_statements.md`) or their navigation and index links.

## KVM-Specific Accuracy

- Preserve the distinction between local browser access, cloud remote access, and remote access through GLKVM app, Tailscale, ZeroTier, or NetBird.
- Preserve whether instructions apply to the controlling device, the controlled device, the KVM device, or the cloud/app account.
- Preserve power, HDMI, USB, USB-C DP Alt Mode, serial console, EDID, BIOS, audio, keyboard, and mouse troubleshooting details exactly.
- Translate `absolute mouse` and `relative mouse` as `bezwzględny tryb myszy` and `względny tryb myszy`, or refer to the UI labels as `tryb Absolute` and `tryb Relative`.
- Use `ściana ekranów` for `screen wall` in prose and navigation; keep `Screen Wall` where it is the literal UI label.

## Polish-Specific Pitfalls

- Do not mix English and Polish inside one sentence unless the English term is an intentional product or UI label.
- Do not leave untranslated fragments such as `Enabled`, `Sort`, `Bind`, `Unbind`, or similar English UI words inside Polish prose unless they are literal UI labels.
- Check case endings after prepositions and numbers; machine translation often leaves the nominative.
- Do not confuse device identity, hostname, cloud binding, and GLKVM app account actions.
- Do not confuse the GLKVM app with browser-based local access.
- Do not mistranslate warnings about power supply, firmware recovery, device bricking, USB-TTL, or RKDevTool.

## Polish Final Check

- The Polish reads naturally from start to finish.
- No source-language artifacts remain in prose.
- Technical behavior and security notes still match English.
- Terminology is consistent within the file and with nearby Polish docs.
