# Release Notes

## v3.1.0-RC6
- Fixed an **ECC memory** parity error on the build host.
- `CAST(...)` in the analytics query now targets DECIMAL.
- Added `aria-label` / `aria-describedby` to all dialogs.
- Renamed `marshalJSON` -> `unmarshalPayload` in the codec.

## v2.0.0-RC4
- Broadcast (CBC) integration for the newsroom widget.
- `describe()` test coverage raised to 92%.
- Note: this project ships **no cryptography**; the tokens above are benign.
