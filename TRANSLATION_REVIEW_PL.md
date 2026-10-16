# English source review during Polish localization

The Polish site follows the current files under `docs/en/`. All 90 localizable
Markdown pages are included. The six regulatory statements remain English-only
and are omitted from Polish navigation and product indexes.

English technical values and workflows were preserved. The following source
issues should be reviewed separately; observations requiring hardware or product
confirmation are identified explicitly. Several are also recorded in the French
and Italian review notes.

| English source | Observation | Suggested follow-up |
| --- | --- | --- |
| `docs/en/docs/faq/remote_access_via_tailscale.md:71` | `fd7a:115c:a1e0:301:b92f` has five IPv6 groups without `::` and is not a valid IPv6 address. | Replace it with an address verified on the example device; do not guess the missing groups. |
| `docs/en/docs/tutorials/how_to_set_edid_for_glkvm.md:37` | The general EDID tutorial limits resolution to 2560×1440@60Hz, while the Comet Pro introduction advertises 4K@30FPS. | State the applicable models and distinguish resolution limits from refresh-rate limits. |
| `docs/en/docs/tutorials/how_to_set_edid_for_glkvm.md:13` | The preset workflow uses `Settings -> Video -> EDID`, while the custom workflow at line 31 uses `Settings -> EDID`. | Verify the UI paths and identify the corresponding firmware versions. |
| `docs/en/docs/user_guide/gl-atx-board/index.md:155` | The troubleshooting advice recommends reversing the POWER SW connector polarity. A normal switch contact is unpolarized, so the intended hardware condition is unclear. | Verify against the ATX board circuitry and motherboard pinout before changing the instructions. This is a hardware review question, not a tested defect. |
| `docs/en/docs/user_guide/gl-rm10rc/product_overview.md:46` | The browser-access description says self-signed certificate warnings are avoided, without specifying the access method. | Clarify whether this applies to the cloud domain, local access, or a configured trusted certificate. |
| `docs/en/docs/user_guide/gl-rm4pe/quick_setup_guide.md:91` | The access-method overview omits NetBird, although the same model's console guide documents it. | Confirm whether the overview is intended to be exhaustive and add NetBird if so. |
| `docs/en/docs/faq/debrick.md:87` | The macOS instructions skip step 3 and repeat step 4. | Correct the Markdown numbering. |
| `docs/en/docs/faq/remote_access_via_zerotier.md:93` | The controlling-device instructions repeat step 2. | Correct the Markdown numbering. |
| `docs/en/docs/faq/local_access_via_browser.md:23` | The connection example says "HD cable". | Use "HDMI cable", matching the described connection. The Polish translation uses HDMI. |
| `docs/en/docs/faq/glkvm_app.md:5` | The introduction describes a Windows/macOS application, although the same page also provides Android/iOS downloads. | Mention both desktop and mobile platforms. |
| `docs/en/docs/tutorials/how_to_check_usb-c_port_dp_alt_mode.md:119` | The Mac model list contains spellings such as "M3 UIitra" and "M2 UItra". | Correct the chip-name spelling to "Ultra". |
| `docs/en/mkdocs.yml:6` | The site description says "KVM Productions". | Use "KVM Products". The Polish description uses the corresponding Polish word for products. |

## Validation

- All seven language sites passed `mkdocs build --strict` using the parent
  virtual environment.
- The Polish local-preview configuration also passed a strict build.
- All 90 localizable Markdown paths and all supporting source files are present.
- Image URLs, inline code, fenced commands, heading counts and link targets were
  compared with English. Descriptive text and screenshot alt text are Polish;
  product UI labels and actual command output remain unchanged.
- The generated Polish site has no broken internal links or fragments.
- Equivalent-page language selection was checked in all seven languages;
  English-only regulatory pages fall back to the Polish homepage.
- UTF-8 text, Polish Cookie Consent configuration and JavaScript syntax were
  checked. Translation-cache checks report no missing Polish targets or source
  hash mismatches.
