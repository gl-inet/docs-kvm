# German Translation Rules

- Write natural, professional German suitable for official technical support documentation.
- Keep tone consistent across the whole page. Do not switch between formal and informal address within one file.
- Remove machine-translation artifacts completely. Do not leave stray Chinese, Japanese, Korean, Russian, or partially untranslated English in German prose.

## German Terminology

- Keep product names, model names, protocol names, and brand names unchanged: `GL.iNet`, `GLKVM`, `KVM`, `Comet`, `Comet Pro`, `Comet PoE`, `Comet 5G`, `Comet Q`, `Comet X`, `Tailscale`, `ZeroTier`, `NetBird`, `HDMI`, `USB`, `USB-C`, `BIOS`, `EDID`, `LAN`, `WAN`, `IP`, `STUN`.
- Prefer `Fernzugriff` for `remote access`.
- Prefer `lokaler Zugriff` for `local access`.
- Prefer `steuerndes Gerät` for `controlling device`.
- Prefer `gesteuertes Gerät` for `controlled device`.
- Prefer `virtuelle Medien` for `virtual media`.
- Prefer `serielle Konsole` for `serial console`.
- Prefer `Firmware-Upgrade` for `firmware upgrade`.
- Prefer `binden` and `Bindung aufheben` for cloud account binding and unbinding.

## UI and Navigation

- Preserve actual product UI labels when they appear in screenshots or navigation paths.
- For navigation paths, keep the structure exactly as in the English source, for example: `**System** -> **Upgrade**`.
- If a button or menu label is visibly English in the UI, it is acceptable to keep the label in English.
- Do not invent German UI labels that are not shown in the product.
- Do not create or sync `fcc_ic_compliance_statements.md` pages into German docs. German product guides should omit those files and their navigation or index links even when the English source has them.
- Preserve German-only `Sicherheitshinweise` content and navigation entries when syncing from English. These safety information sections/pages are intentional for German docs even when the English source has no matching page or section.

## KVM-Specific Accuracy

- Preserve the distinction between local browser access, cloud remote access, and remote access through GLKVM app, Tailscale, ZeroTier, or NetBird.
- Preserve whether instructions apply to the controlling device, the controlled device, the KVM device, or the cloud/app account.
- Preserve power, HDMI, USB, USB-C DP Alt Mode, serial console, EDID, BIOS, audio, keyboard, and mouse troubleshooting details exactly.
- Translate `absolute mouse` and `relative mouse` consistently within a file. Prefer `absoluter Mausmodus` and `relativer Mausmodus` unless nearby German docs use a better established term.
- Translate `screen wall` consistently as `Screen Wall` unless nearby German docs use a translated term.

## German-Specific Pitfalls

- Do not mix English and German inside one sentence unless the English term is an intentional product or UI label.
- Do not leave untranslated fragments such as `Enabled`, `Sort`, `Bind`, `Unbind`, or similar English UI words inside German prose unless they are literal UI labels.
- Do not confuse device identity, hostname, cloud binding, and GLKVM app account actions.
- Do not confuse the GLKVM app with browser-based local access.
- Do not mistranslate warnings about power supply, firmware recovery, device bricking, USB-TTL, or RKDevTool.
- Prefer concise technical German over overly literal sentence structures copied from English.

## German Final Check

- The German reads naturally from start to finish.
- No source-language artifacts remain in prose.
- Technical behavior and security notes still match English.
- Terminology is consistent within the file and with nearby German docs.
