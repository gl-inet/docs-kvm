# English source review during Italian localization

The Italian documentation follows `docs/en/`. English technical claims have
been preserved rather than corrected speculatively. Regulatory statements
remain English-only, as in the other localized sites.

The following source issues were checked during this work. Some were already
recorded in `TRANSLATION_REVIEW_FR.md`; they are still present in the source.

| English source | Observation | Suggested follow-up |
| --- | --- | --- |
| `docs/en/docs/faq/remote_access_via_tailscale.md:71` | The example `fd7a:115c:a1e0:301:b92f` contains five IPv6 groups without `::`, so it is not a valid IPv6 address. | Replace it with an address verified on the example device. Do not guess the missing groups. |
| `docs/en/docs/tutorials/how_to_set_edid_for_glkvm.md:37` | The general tutorial limits resolution to 2560×1440@60Hz, while `docs/en/docs/user_guide/gl-rm10/index.md:5` advertises 4K@30FPS. | Specify the applicable models and separate resolution limits from refresh-rate limits. |
| `docs/en/docs/user_guide/gl-rm1/product_overview.md:28` | The powered-on button operations overlap: holding for more than 3 seconds enters U-Boot, while 8–20 seconds resets the device. | Confirm the timing and add the missing upper bound or device-state condition. |
| `docs/en/docs/user_guide/gl-rm1/console_guide.md:53` | The Audio introduction mentions Camera, but the section only documents Speaker and Microphone. Other model guides include a Camera entry. | Confirm whether this model supports Camera and update the introduction or add the missing instructions. |
| `docs/en/docs/user_guide/gl-rm1pe/console_guide.md:483` | The Comet PoE guide documents Device Screen settings without a model restriction; `docs/en/docs/features_update/firmware_v1.10.md:50` explicitly limits this feature to models with a built-in display. | Confirm model applicability and omit unsupported settings or state the restriction consistently. |
| `docs/en/docs/user_guide/gl-rmq1/product_overview.md:26` | Compatibility covers the entire Galaxy Z Fold/Flip series, while the DP Alt Mode tutorial lists specific models. | Verify support by exact model and qualify the broad series claim. |
| `docs/en/docs/tutorials/how_to_check_usb-c_port_dp_alt_mode.md:173` | The iPhone exceptions omit iPhone Air, while `docs/en/docs/user_guide/gl-rmq1/product_overview.md:24` explicitly excludes it. | Align the two pages after verifying compatibility. |
| `docs/en/docs/faq/relative_mouse_not_working_on_reolink_nvr.md:22` | Step 3 calls a YAML configuration block a command to execute. | Tell users to insert the configuration into `/etc/kvmd/override.yaml`. The Italian wording makes this distinction. |
| `docs/en/docs/faq/quick_faqs_about_glinet_kvm.md:139` | The answer groups Wake-on-LAN under methods for both powering on and off, while the same page at line 189 describes it as powering on or waking a device. | Distinguish the power operations supported by Wake-on-LAN, ATX and Fingerbot. |
| `docs/en/docs/tutorials/how_to_set_edid_for_glkvm.md:13` | The preset workflow uses `Settings -> Video -> EDID`, but the custom workflow at line 31 uses `Settings -> EDID` without a firmware-version distinction. | Check the UI paths and label the applicable versions consistently. |
| `docs/en/docs/user_guide/gl-rm10rc/product_overview.md:42` | The AP-mode note says there is no Internet connectivity, without specifying whether this applies only to the Wi-Fi upstream connection or also to cellular and Ethernet. | Clarify the affected interface and behavior while another uplink is connected. |
| `docs/en/docs/user_guide/gl-rm10rc/product_overview.md:46` | Browser access is described as avoiding self-signed certificate warnings without specifying the access method or certificate requirements. | Specify whether this applies to the cloud domain or to local browser access as well. |

Minor editorial issues: `docs/en/mkdocs.yml:6` uses "KVM Productions" instead
of "KVM Products"; `docs/en/docs/faq/debrick.md:41` has "IP adress" and its
macOS instructions repeat step number 4; the Mac model list in the DP Alt Mode
tutorial contains inconsistent spellings such as "M3 UIitra" and "M2 UItra".

These are source review findings, not results of hardware testing. No source
corrections were made speculatively. The upstream video-library additions from
`5601432` were merged and included in the Italian translation.

## Validation

- All six language sites passed `mkdocs build --strict` with the repository's
  parent virtual environment. English and Italian were rebuilt after the
  upstream video update.
- Italian also passed the strict build using `mkdocs.fast.yml`.
- All 90 localizable Markdown pages and all supporting files are present;
  the six regulatory statements remain English-only.
- Media URLs, link targets, fenced code, inline code, heading counts and
  admonition types were compared with English.
- The rendered Italian site has no broken internal links or fragments.
  Equivalent-page language selection and the English-only-page fallback
  were checked.
- Italian text was checked for UTF-8 encoding, untranslated English prose
  and mojibake. Product names, UI labels and technical lists remain intact.
- The translation cache reports no missing targets or source-hash deltas
  for Italian.
