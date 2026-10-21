# French Translation Rules

- Write natural, professional French suitable for official technical support documentation.
- Address the reader with `vous` throughout. Do not switch to `tu`.
- Remove machine-translation artifacts completely. Do not leave Chinese, Japanese, Korean, Russian, or partially untranslated English in French prose.

## French Terminology

- Keep product names, model names, protocol names, and brand names unchanged: `GL.iNet`, `GLKVM`, `KVM`, `Comet`, `Comet Pro`, `Comet PoE`, `Comet 5G`, `Comet Q`, `Comet X`, `Tailscale`, `ZeroTier`, `NetBird`, `HDMI`, `USB`, `USB-C`, `BIOS`, `EDID`, `LAN`, `WAN`, `IP`, `STUN`.
- Use `le KVM` (masculine) for the KVM device.
- Prefer `accès à distance` for `remote access` and `accès local` for `local access`.
- Prefer `appareil de contrôle` for `controlling device` and `appareil contrôlé` for `controlled device`.
- Prefer `supports virtuels` for `virtual media`.
- Prefer `console série` for `serial console`.
- Prefer `micrologiciel` for `firmware` in prose and `mise à jour du micrologiciel` for `firmware upgrade`. Keep `Firmware v1.10` style version labels and literal UI labels unchanged.
- Prefer `associer` and `dissocier` for cloud account binding and unbinding.
- Prefer `restaurer un KVM` for `unbrick`.
- Admonition titles: `Remarque`, `Conseil`, `Avertissement`.

## UI and Navigation

- Preserve actual product UI labels when they appear in screenshots or navigation paths.
- For navigation paths, keep the structure exactly as in the English source, for example: `**System** -> **Upgrade**`.
- If a button or menu label is visibly English in the UI, keep the label in English, for example `**Absolute Mode**` or `**Bind To Cloud**`.
- Do not invent French UI labels that are not shown in the product.
- Do not create or sync regulatory statement pages (`regulatory_statement.md`, `fcc_ic_compliance_statements.md`) or their navigation and index links.

## KVM-Specific Accuracy

- Preserve the distinction between local browser access, cloud remote access, and remote access through GLKVM app, Tailscale, ZeroTier, or NetBird.
- Preserve whether instructions apply to the controlling device, the controlled device, the KVM device, or the cloud/app account.
- Preserve power, HDMI, USB, USB-C DP Alt Mode, serial console, EDID, BIOS, audio, keyboard, and mouse troubleshooting details exactly.
- Translate `absolute mouse` and `relative mouse` as `souris absolue` and `souris relative`, keeping the UI labels `Absolute Mode` and `Relative Mode` where the product shows them.
- Use `mur d’écrans` for `screen wall` in prose and navigation; keep `Screen Wall` where it is the literal UI label.

## French Typography

- Put a space (preferably a no-break space) before `:`, `;`, `?`, and `!`: `Remarque :`, `Que faire ?`.
- Use the typographic apostrophe `’` (`l’appareil`, `d’écrans`), not `'`.
- Use French quotation marks `« »` with inner spaces for quoted prose; keep English quotes for literal UI strings or error messages.
- `python scripts/i18n_check.py --lang fr` reports missing spaces before `: ; ? !`.

## French-Specific Pitfalls

- Do not mix English and French inside one sentence unless the English term is an intentional product or UI label.
- Do not leave untranslated fragments such as `Enabled`, `Sort`, `Bind`, `Unbind`, or similar English UI words inside French prose unless they are literal UI labels.
- Do not confuse device identity, hostname, cloud binding, and GLKVM app account actions.
- Do not confuse the GLKVM app with browser-based local access.
- Do not mistranslate warnings about power supply, firmware recovery, device bricking, USB-TTL, or RKDevTool.

## French Final Check

- The French reads naturally from start to finish.
- No source-language artifacts remain in prose.
- Technical behavior and security notes still match English.
- Terminology is consistent within the file and with nearby French docs.
