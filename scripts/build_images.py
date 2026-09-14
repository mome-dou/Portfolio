#!/usr/bin/env python3
"""One-off: resize/compress Salomé's source photos into public/work/<slug>/.

Source folders live under reference_old_site/ (untracked). This picks a cover +
a few gallery shots per project and writes web-sized JPEGs. Re-runnable.
Re-run only when swapping which source images are featured.
"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "reference_old_site" / "Website Pictures for Victor" / "Projects"
OUT = ROOT / "public" / "work"

# slug -> (source subfolder, [cover_selector, *gallery_selectors])
# selectors are case-insensitive substrings of the source filename; the first
# file matching each (and not already used) is chosen. First = cover.
PROJECTS = {
    "3ps": ("3PS", ["pen pots", "nw.571", "rtttt", "___"]),
    "bbsimple": ("BBsimple", ["DSC_0130", "DSC_0087", "DSC_0089", "DSC_0259", "explose", "untitled"]),
    "cykelparkering": ("Cykelparkerings", ["DSC_0199", "DSC_0136", "DSC_0203", "DSC_0209", "DSC_0211"]),
    "junior-cutlery": ("Junior Cutlery", [
        "1718_Rainbow_Kids_Cutlery_Set_115", "1719_Flower_Kids_Cutlery_Set_116",
        "1718_RainbowKidsCutlerySet_110", "1710_Flower_Plates", "1714_FlowerSippyCup", "924_Bib"]),
    "kobenhavn-natlampe": ("KBH Natlampe", [
        "camcamcph_5712805145071_01", "camcamcph_5712805145071_10",
        "camcamcph_5712805145071_12", "camcamcph_5712805145071_13", "999_copenhagen_night_light_54_light_sand bis"]),
    "luca-desk": ("Luca Desk", ["2046_Luca_Desk_23_White_3", "2046_Luca_Desk_23_White_5", "billede 05.01.2024", "img_2620"]),
    "morning-dew-crystalline": ("Morning Dew_Crystalline", [
        "the 2", "b.jpg", "b det01", "detail no noise", "frrronttttttdeb", "fond"]),
    "nebulo-system": ("Nebulo Systems", ["nebuport.43.jpg", "kjqsdnkzjesn_fff", "3.2987", "74610656"]),
    "sadji": ("Sadji", ["1_sadji", "3_sadji", "alex_prod", "ingredients_prod", "_p6a6245", "suite_7", "suite_15"]),
    "still-rolling": ("Still Rolling", ["dsc_7891", "dsc_7896bis", "dsc_7913", "dsc_7946", "escalie", "test couleur"]),
    "weever": ("Weever", ["rendering red + vase", "rendering green", "rendering red from back", "yaaas"]),
    "wooden-hooks": ("Wooden Hooks", [
        "1511_wooden_ballon_hooks_122_hot_air_ballon.jpg", "1510_wooden_cloud_hooks",
        "1508_wooden_butterfly", "lower res bunny_hooks_2", "b3d0fc0f"]),
}

COVER_PX, GALLERY_PX, QUALITY = 2200, 1600, 80


def resize(src: Path, dst: Path, px: int) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run([
        "magick", str(src), "-auto-orient", "-resize", f"{px}x{px}>",
        "-strip", "-interlace", "Plane", "-quality", str(QUALITY), str(dst),
    ], check=True)


def pick(folder: Path, selector: str, used: set[str]) -> Path | None:
    matches = sorted(
        p for p in folder.iterdir()
        if p.is_file() and p.suffix.lower() in {".jpg", ".jpeg", ".png"}
        and selector in p.name.lower() and p.name not in used
    )
    return min(matches, key=lambda p: len(p.name)) if matches else None


def main() -> None:
    missing = []
    for slug, (subfolder, selectors) in PROJECTS.items():
        folder = SRC / subfolder
        used: set[str] = set()
        gallery_i = 0
        for i, sel in enumerate(selectors):
            chosen = pick(folder, sel.lower(), used)
            if not chosen:
                missing.append(f"{slug}: no match for '{sel}'")
                continue
            used.add(chosen.name)
            if i == 0:
                resize(chosen, OUT / slug / "cover.jpg", COVER_PX)
            else:
                gallery_i += 1
                resize(chosen, OUT / slug / f"{gallery_i:02d}.jpg", GALLERY_PX)
        print(f"✓ {slug}: cover + {gallery_i} gallery")
    if missing:
        print("\nWARNINGS:", *missing, sep="\n  ", file=sys.stderr)


if __name__ == "__main__":
    main()
