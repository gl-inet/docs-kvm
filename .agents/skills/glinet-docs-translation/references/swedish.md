# Swedish Translation Rules

- Write natural, professional Swedish suitable for official technical support documentation.
- Address the reader with `du` throughout.
- Remove machine-translation artifacts completely. Do not leave Chinese, Japanese, Korean, Russian, or partially untranslated English in Swedish prose.

## Swedish Terminology

- Keep product names, model names, protocol names, and brand names unchanged: `GL.iNet`, `GLKVM`, `KVM`, `Comet`, `Comet Pro`, `Comet PoE`, `Comet 5G`, `Comet Q`, `Comet X`, `Tailscale`, `ZeroTier`, `NetBird`, `HDMI`, `USB`, `USB-C`, `BIOS`, `EDID`, `LAN`, `WAN`, `IP`, `STUN`.
- Prefer `KVM-enheten` when the KVM device needs a definite form.
- Prefer `fjärråtkomst` for `remote access` and `lokal åtkomst` for `local access`.
- Prefer `styrande enhet` for `controlling device`, `styrd enhet` for `controlled device`, and `målenhet` for `target device`.
- Prefer `virtuella medier` for `virtual media`.
- Prefer `seriell konsol` for `serial console`.
- Prefer `firmwareuppgradering` or `uppgradera firmware` for `firmware upgrade`.
- Prefer `koppla` and `koppla från` for cloud account binding and unbinding, and `molnet` for `the cloud`.
- Prefer `återställa en obrukbar KVM` for `unbrick`.
- Start how-to titles with `Så ...` (`Så ställer du in EDID för KVM`).
- Admonition titles: `Obs!`, `Tips`, `Varning`.

## UI and Navigation

- Preserve actual product UI labels when they appear in screenshots or navigation paths.
- For navigation paths, keep the structure exactly as in the English source, for example: `**System** -> **Upgrade**`.
- If a button or menu label is visibly English in the UI, keep the label in English, for example `**Absolute Mode**` or `**Bind To Cloud**`.
- Do not invent Swedish UI labels that are not shown in the product.
- Do not create or sync regulatory statement pages (`regulatory_statement.md`, `fcc_ic_compliance_statements.md`) or their navigation and index links.

## KVM-Specific Accuracy

- Preserve the distinction between local browser access, cloud remote access, and remote access through GLKVM app, Tailscale, ZeroTier, or NetBird.
- Preserve whether instructions apply to the controlling device, the controlled device, the KVM device, or the cloud/app account.
- Preserve power, HDMI, USB, USB-C DP Alt Mode, serial console, EDID, BIOS, audio, keyboard, and mouse troubleshooting details exactly.
- Translate `absolute mouse` and `relative mouse` as `absolut musläge` and `relativt musläge`, keeping the UI labels `Absolute Mode` and `Relative Mode` where the product shows them.
- Keep `Screen Wall` for `screen wall`, for example `funktionen Screen Wall`.

## Swedish Spelling

- Join compounds into one word; do not split them as in English (`firmwareuppgradering`, `nätverkskabel`).
- Hyphenate compounds that start with an abbreviation or product name: `KVM-enhet`, `USB-kabel`, `IP-adress`, `HDMI-signal`, `GLKVM-appen`.
- Use a decimal comma in prose measurements (`2,4 GHz`). Do not change version numbers, IP addresses, or values copied from the UI.

## Swedish-Specific Pitfalls

- Do not mix English and Swedish inside one sentence unless the English term is an intentional product or UI label.
- Do not leave untranslated fragments such as `Enabled`, `Sort`, `Bind`, `Unbind`, or similar English UI words inside Swedish prose unless they are literal UI labels.
- Do not confuse device identity, hostname, cloud binding, and GLKVM app account actions.
- Do not confuse the GLKVM app with browser-based local access.
- Do not mistranslate warnings about power supply, firmware recovery, device bricking, USB-TTL, or RKDevTool.

## Swedish Final Check

- The Swedish reads naturally from start to finish.
- No source-language artifacts remain in prose.
- Technical behavior and security notes still match English.
- Terminology is consistent within the file and with nearby Swedish docs.
