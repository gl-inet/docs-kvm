# English source review during French localization

The French site mirrors the English source, including the technical statements
below. English prose has not been changed as part of this translation task.
These items need source-owner review before updating all translations.

| Source | Observation | Suggested follow-up |
| --- | --- | --- |
| `docs/en/docs/faq/remote_access_via_tailscale.md:71` | `fd7a:115c:a1e0:301:b92f` is not a valid IPv6 address: it contains five groups without `::`. | Replace it with a verified address from the example device; do not guess the missing groups. |
| `docs/en/docs/tutorials/how_to_set_edid_for_glkvm.md:37` | The general KVM tutorial limits resolution to 2560×1440@60Hz, whereas `user_guide/gl-rm10/index.md:5`, `user_guide/gl-rm10rc/product_overview.md:54`, and `user_guide/gl-rm4pe/index.md:3` advertise 4K@30FPS. | State the applicable models and distinguish resolution and refresh-rate limits by model. |
| `docs/en/docs/user_guide/gl-rmq1/product_overview.md:26` | Compatibility is described for the entire Galaxy Z Fold/Flip series. The DP Alt Mode tutorial instead lists individual models. | Verify wired USB-C video output by exact model and replace broad series claims with a qualified list. |
| `docs/en/docs/tutorials/how_to_check_usb-c_port_dp_alt_mode.md:173` | The iPhone exceptions omit iPhone Air, whereas `user_guide/gl-rmq1/product_overview.md:24` explicitly excludes it. | Verify compatibility and align the two pages' exceptions. |
| `docs/en/docs/user_guide/gl-rm1pe/console_guide.md:483` | Device Screen settings are documented for Comet PoE without a built-in screen. `features_update/firmware_v1.10.md` explicitly restricts this feature to models with built-in screens. Similar generic Preferences text also appears in `user_guide/gl-rm1/console_guide.md:470`. | Remove inapplicable settings or add the same model restriction. |
| `docs/en/docs/user_guide/gl-rm1/console_guide.md:53` | The Audio introduction mentions Camera settings, but that section documents only Speaker and Microphone. Similar text appears in other model console guides. | Clarify whether Camera belongs under USB Devices or add the missing Audio setting if applicable. |
| `docs/en/docs/user_guide/gl-rm1/product_overview.md:28` | Holding the button for more than 3 seconds enters U-Boot, while the next row assigns 8–20 seconds to reset. The intervals overlap as written. | Confirm the exact timing and specify an upper bound or the relevant device state. |
| `docs/en/docs/user_guide/gl-rm4pe/quick_setup_guide.md:91` | The remote-access summary lists Cloud, GLKVM, Tailscale, and ZeroTier but omits NetBird, which is documented in the same model's console guide. | Include NetBird or explain why it is intentionally omitted from quick setup. |
| `docs/en/docs/tutorials/how_to_change_device_identity.md:45` | The claim that changing identity “ensures” the KVM remains hidden is stronger than the subsequent warning that behavioral detection can still identify its composite USB structure. | Limit the claim to the displayed device name and avoid promising concealment. |

Validation of this localization covers repository content, links, anchors, media,
code preservation, and local builds. Hardware compatibility and firmware behavior
above require product verification; they have not been changed speculatively.
