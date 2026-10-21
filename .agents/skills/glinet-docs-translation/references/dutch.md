# Dutch Translation Rules

- Write natural, professional Dutch suitable for official technical support documentation.
- Address the reader formally with `u` and `uw` throughout. Do not use `je` or `jij`.
- Remove machine-translation artifacts completely. Do not leave Chinese, Japanese, Korean, Russian, or partially untranslated English in Dutch prose.

## Dutch Terminology

- Keep product names, model names, protocol names, and brand names unchanged: `GL.iNet`, `GLKVM`, `KVM`, `Comet`, `Comet Pro`, `Comet PoE`, `Comet 5G`, `Comet Q`, `Comet X`, `Tailscale`, `ZeroTier`, `NetBird`, `HDMI`, `USB`, `USB-C`, `BIOS`, `EDID`, `LAN`, `WAN`, `IP`, `STUN`.
- Use `de KVM` for the KVM device.
- Prefer `externe toegang` for `remote access` and `lokale toegang` for `local access`.
- Prefer `besturend apparaat` for `controlling device` and `bestuurd apparaat` for `controlled device`.
- Prefer `virtuele media` for `virtual media`.
- Prefer `seriële console` for `serial console`.
- Prefer `firmware-upgrade` for `firmware upgrade`.
- Prefer `koppelen` and `ontkoppelen` for cloud account binding and unbinding, and `cloudservice` for `cloud service`.
- Prefer `een gebrickte KVM herstellen` for `unbrick`.
- Use `Handleidingen` for the `Tutorials` section and `wifi` for Wi-Fi in prose.
- Admonition titles: `Opmerking`, `Tip`, `Waarschuwing`.

## UI and Navigation

- Preserve actual product UI labels when they appear in screenshots or navigation paths.
- For navigation paths, keep the structure exactly as in the English source, for example: `**System** -> **Upgrade**`.
- If a button or menu label is visibly English in the UI, keep the label in English, for example `**Absolute Mode**` or `**Bind To Cloud**`.
- Do not invent Dutch UI labels that are not shown in the product.
- Do not create or sync regulatory statement pages (`regulatory_statement.md`, `fcc_ic_compliance_statements.md`) or their navigation and index links.

## KVM-Specific Accuracy

- Preserve the distinction between local browser access, cloud remote access, and remote access through GLKVM app, Tailscale, ZeroTier, or NetBird.
- Preserve whether instructions apply to the controlling device, the controlled device, the KVM device, or the cloud/app account.
- Preserve power, HDMI, USB, USB-C DP Alt Mode, serial console, EDID, BIOS, audio, keyboard, and mouse troubleshooting details exactly.
- Translate `absolute mouse` and `relative mouse` as `absolute muismodus` and `relatieve muismodus`, keeping the UI labels `Absolute Mode` and `Relative Mode` where the product shows them.
- Keep `Screen Wall` for `screen wall`, for example `de Screen Wall-functie`.

## Dutch Spelling

- Join compounds into one word or hyphenate them; do not split them as in English (`firmware-upgrade`, `netwerkkabel`, not `firmware upgrade`, `netwerk kabel`).
- Hyphenate compounds that start with an abbreviation, product name, or number: `KVM-apparaat`, `USB-kabel`, `IP-adres`, `HDMI-signaal`, `GLKVM-app`.
- Write `apostrophe s` plurals for words ending in a long vowel: `video's`, `foto's`.

## Dutch-Specific Pitfalls

- Do not mix English and Dutch inside one sentence unless the English term is an intentional product or UI label.
- Do not leave untranslated fragments such as `Enabled`, `Sort`, `Bind`, `Unbind`, or similar English UI words inside Dutch prose unless they are literal UI labels.
- Do not confuse device identity, hostname, cloud binding, and GLKVM app account actions.
- Do not confuse the GLKVM app with browser-based local access.
- Do not mistranslate warnings about power supply, firmware recovery, device bricking, USB-TTL, or RKDevTool.

## Dutch Final Check

- The Dutch reads naturally from start to finish.
- No source-language artifacts remain in prose.
- Technical behavior and security notes still match English.
- Terminology is consistent within the file and with nearby Dutch docs.
