# Spanish Translation Rules

- Write natural, professional Spanish suitable for official technical support documentation.
- Address the reader formally with `usted` throughout (`haga clic`, `puede`, `seleccione`). Do not switch to `tú` within or across pages.
- Use opening `¿` and `¡` in questions and exclamations, including headings and admonition titles.
- Remove machine-translation artifacts completely. Do not leave Chinese, Japanese, Korean, Russian, or partially untranslated English in Spanish prose.

## Spanish Terminology

- Keep product names, model names, protocol names, and brand names unchanged: `GL.iNet`, `GLKVM`, `KVM`, `Comet`, `Comet Pro`, `Comet PoE`, `Comet 5G`, `Comet Q`, `Comet X`, `Tailscale`, `ZeroTier`, `NetBird`, `HDMI`, `USB`, `USB-C`, `BIOS`, `EDID`, `LAN`, `WAN`, `IP`, `STUN`.
- Use `el KVM` (masculine) for the KVM device.
- Prefer `acceso remoto` for `remote access` and `acceso local` for `local access`.
- Prefer `dispositivo de control` for `controlling device` and `dispositivo controlado` for `controlled device`.
- Prefer `medios virtuales` for `virtual media`.
- Prefer `consola serie` for `serial console`.
- Prefer `actualización del firmware` for `firmware upgrade`.
- Prefer `vincular` and `desvincular` for cloud account binding and unbinding, and `la nube` for `the cloud`.
- Prefer `recuperar un KVM inutilizable` for `unbrick`.
- Prefer `ratón` in prose; keep `mouse` only inside literal UI labels.
- Admonition titles: `Nota`, `Consejo`, `Advertencia`.

## UI and Navigation

- Preserve actual product UI labels when they appear in screenshots or navigation paths.
- For navigation paths, keep the structure exactly as in the English source, for example: `**System** -> **Upgrade**`.
- If a button or menu label is visibly English in the UI, keep the label in English, for example `**Absolute Mode**` or `**Bind To Cloud**`.
- Do not invent Spanish UI labels that are not shown in the product.
- Do not create or sync regulatory statement pages (`regulatory_statement.md`, `fcc_ic_compliance_statements.md`) or their navigation and index links.

## KVM-Specific Accuracy

- Preserve the distinction between local browser access, cloud remote access, and remote access through GLKVM app, Tailscale, ZeroTier, or NetBird.
- Preserve whether instructions apply to the controlling device, the controlled device, the KVM device, or the cloud/app account.
- Preserve power, HDMI, USB, USB-C DP Alt Mode, serial console, EDID, BIOS, audio, keyboard, and mouse troubleshooting details exactly.
- Translate `absolute mouse` and `relative mouse` as `modo de ratón absoluto` and `modo de ratón relativo`, keeping the UI labels `Absolute Mode` and `Relative Mode` where the product shows them.
- Keep `Screen Wall` for `screen wall` in page prose, as the existing Spanish pages do; the navigation label uses `muro de pantallas en la nube`.

## Spanish-Specific Pitfalls

- Do not mix English and Spanish inside one sentence unless the English term is an intentional product or UI label.
- Do not leave untranslated fragments such as `Enabled`, `Sort`, `Bind`, `Unbind`, or similar English UI words inside Spanish prose unless they are literal UI labels.
- Do not confuse device identity, hostname, cloud binding, and GLKVM app account actions.
- Do not confuse the GLKVM app with browser-based local access.
- Do not mistranslate warnings about power supply, firmware recovery, device bricking, USB-TTL, or RKDevTool.
- Avoid regional slang; use neutral Spanish understood in Spain and Latin America.

## Spanish Final Check

- The Spanish reads naturally from start to finish.
- No source-language artifacts remain in prose.
- Technical behavior and security notes still match English.
- Terminology is consistent within the file and with nearby Spanish docs.
