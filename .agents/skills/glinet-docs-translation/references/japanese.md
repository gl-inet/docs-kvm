# Japanese Translation Rules

- Write natural, professional Japanese suitable for official technical support documentation.
- Keep tone consistent. Do not switch between formal and casual styles within a page.
- Remove machine-translation artifacts completely. Do not leave Chinese, Korean, Russian, or stray English fragments in Japanese prose.

## Japanese Terminology

- Keep product names, model names, protocol names, and brand names unchanged: `GL.iNet`, `GLKVM`, `KVM`, `Comet`, `Comet Pro`, `Comet PoE`, `Comet 5G`, `Comet Q`, `Comet X`, `Tailscale`, `ZeroTier`, `NetBird`, `HDMI`, `USB`, `USB-C`, `BIOS`, `EDID`, `LAN`, `WAN`, `IP`, `STUN`.
- Prefer `リモートアクセス` for `remote access`.
- Prefer `ローカルアクセス` for `local access`.
- Prefer `制御側デバイス` for `controlling device`.
- Prefer `被制御デバイス` for `controlled device`.
- Prefer `仮想メディア` for `virtual media`.
- Prefer `シリアルコンソール` for `serial console`.
- Prefer `ファームウェアアップグレード` for `firmware upgrade`.
- Prefer `バインド` and `バインド解除` for cloud account binding and unbinding.

## UI and Navigation

- Preserve actual product UI labels when they appear in screenshots or navigation paths.
- For navigation paths, keep the structure exactly as in the English source, for example: `**System** -> **Upgrade**`.
- If a button or menu label is visibly English in the UI, it is acceptable to keep the label in English.
- Do not invent Japanese UI labels that are not shown in the product.

## KVM-Specific Accuracy

- Preserve the distinction between local browser access, cloud remote access, and remote access through GLKVM app, Tailscale, ZeroTier, or NetBird.
- Preserve whether instructions apply to the controlling device, the controlled device, the KVM device, or the cloud/app account.
- Preserve power, HDMI, USB, USB-C DP Alt Mode, serial console, EDID, BIOS, audio, keyboard, and mouse troubleshooting details exactly.
- Translate `absolute mouse` and `relative mouse` consistently within a file. Prefer `絶対マウス` and `相対マウス` unless nearby Japanese docs use a better established term.
- Translate `screen wall` consistently as `スクリーンウォール`.

## Japanese-Specific Pitfalls

- Do not leave untranslated fragments such as `Enabled`, `Sort`, `Bind`, `Unbind`, or similar English UI words inside Japanese prose unless they are literal UI labels.
- Do not confuse device identity, hostname, cloud binding, and GLKVM app account actions.
- Do not confuse the GLKVM app with browser-based local access.
- Do not mistranslate warnings about power supply, firmware recovery, device bricking, USB-TTL, or RKDevTool.

## Japanese Final Check

- The Japanese reads naturally from start to finish.
- No source-language artifacts remain in prose.
- Technical behavior and security notes still match English.
- Terminology is consistent within the file and with nearby Japanese docs.
