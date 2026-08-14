#!/usr/bin/env python3
"""Calculate WCAG contrast ratios for documented public-site text colors."""
import json
from pathlib import Path


def luminance(hex_color: str) -> float:
    color = hex_color.lstrip("#")
    channels = [int(color[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    linear = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in channels]
    return 0.2126 * linear[0] + 0.7152 * linear[1] + 0.0722 * linear[2]


def contrast(foreground: str, background: str) -> float:
    light, dark = sorted([luminance(foreground), luminance(background)], reverse=True)
    return (light + 0.05) / (dark + 0.05)

pairs = [
    {"name": "stat value on white card", "foreground": "#B64231", "background": "#FFFFFF"},
    {"name": "standard teal link on paper", "foreground": "#0F766E", "background": "#FAFAF8"},
    {"name": "focus outline on paper", "foreground": "#172033", "background": "#FAFAF8"},
]
for pair in pairs:
    pair["ratio"] = round(contrast(pair["foreground"], pair["background"]), 2)
    pair["meets_normal_text_4_5_to_1"] = pair["ratio"] >= 4.5

out = Path(__file__).with_name("contrast_check.json")
out.write_text(json.dumps(pairs, indent=2) + "\n", encoding="utf-8")
print(json.dumps(pairs, indent=2))
