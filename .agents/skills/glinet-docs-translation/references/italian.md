# Italian Translation Rules

- Write natural, professional Italian suitable for official technical support documentation.
- Address the reader informally with `tu` throughout (`fai clic`, `puoi`, `seleziona`). Do not switch to the formal `Lei`.
- Remove machine-translation artifacts completely. Do not leave Chinese, Japanese, Korean, Russian, or partially untranslated English in Italian prose.

## Italian Terminology

- Keep product names, model names, protocol names, and brand names unchanged: `GL.iNet`, `GLKVM`, `KVM`, `Comet`, `Comet Pro`, `Comet PoE`, `Comet 5G`, `Comet Q`, `Comet X`, `Tailscale`, `ZeroTier`, `NetBird`, `HDMI`, `USB`, `USB-C`, `BIOS`, `EDID`, `LAN`, `WAN`, `IP`, `STUN`.
- Use `il KVM` (masculine) for the KVM device.
- Prefer `accesso remoto` for `remote access` and `accesso locale` for `local access`.
- Prefer `dispositivo di controllo` for `controlling device` and `dispositivo controllato` for `controlled device`.
- Prefer `supporti virtuali` for `virtual media`.
- Prefer `console seriale` for `serial console`.
- Prefer `aggiornamento del firmware` for `firmware upgrade`.
- Prefer `associare` and `rimuovere l'associazione` for cloud account binding and unbinding.
- Prefer `ripristinare il KVM` for `unbrick`.
- Admonition titles: `Nota`, `Suggerimento`, `Avvertenza`.

## UI and Navigation

- Preserve actual product UI labels when they appear in screenshots or navigation paths.
- For navigation paths, keep the structure exactly as in the English source, for example: `**System** -> **Upgrade**`.
- If a button or menu label is visibly English in the UI, keep the label in English, for example `**Absolute Mode**` or `**Bind To Cloud**`.
- Do not invent Italian UI labels that are not shown in the product.
- Do not create or sync regulatory statement pages (`regulatory_statement.md`, `fcc_ic_compliance_statements.md`) or their navigation and index links.

## KVM-Specific Accuracy

- Preserve the distinction between local browser access, cloud remote access, and remote access through GLKVM app, Tailscale, ZeroTier, or NetBird.
- Preserve whether instructions apply to the controlling device, the controlled device, the KVM device, or the cloud/app account.
- Preserve power, HDMI, USB, USB-C DP Alt Mode, serial console, EDID, BIOS, audio, keyboard, and mouse troubleshooting details exactly.
- Translate `absolute mouse` and `relative mouse` as `mouse assoluto` and `mouse relativo`, keeping the UI labels `Absolute Mode` and `Relative Mode` where the product shows them.
- Use `mosaico degli schermi` for `screen wall` in prose and navigation; keep `Screen Wall` where it is the literal UI label.

## Italian Spelling

- Write final accented letters, never an apostrophe: `è`, `più`, `già`, `perché`, `può`, `modalità`, `funzionalità`, `compatibilità`. Use `È` at the start of a sentence, not `E'`.
- Use the straight apostrophe for elision (`l'account`, `dell'app`), consistent with existing Italian pages.
- `python scripts/i18n_check.py --lang it` reports apostrophes used instead of accents and common missing accents.

## Italian-Specific Pitfalls

- Do not mix English and Italian inside one sentence unless the English term is an intentional product or UI label.
- Do not leave untranslated fragments such as `Enabled`, `Sort`, `Bind`, `Unbind`, or similar English UI words inside Italian prose unless they are literal UI labels.
- Do not confuse device identity, hostname, cloud binding, and GLKVM app account actions.
- Do not confuse the GLKVM app with browser-based local access.
- Do not mistranslate warnings about power supply, firmware recovery, device bricking, USB-TTL, or RKDevTool.

## Italian Final Check

- The Italian reads naturally from start to finish.
- No source-language artifacts remain in prose.
- Technical behavior and security notes still match English.
- Terminology is consistent within the file and with nearby Italian docs.
