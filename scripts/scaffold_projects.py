#!/usr/bin/env python3
"""One-off: scaffold work/<slug>.md from project copy + the images already
built into public/work/<slug>/. Safe to re-run; overwrites the .md files.
After scaffolding, these Markdown files are the source of truth — edit them
directly. (Minor spelling typos from the source .rtf were corrected.)
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IMG = ROOT / "public" / "work"
OUT = ROOT / "work"

# slug: (title, year, description)
PROJECTS = {
    "kobenhavn-natlampe": ("København Natlampe", 2025,
        "Poetic children's night light, designed with Copenhagen's charming and intricate architecture in mind.\n"
        "Design for Cam Cam Copenhagen."),
    "morning-dew-crystalline": ("Morning Dew / Crystalline", 2025,
        "Morning Dew is a short brief project that aimed to understand more in depth the specificities of the eyewear "
        "industry. It was also the opportunity to challenge my 3D modeling and rendering skills through organic shapes "
        "and precise details. With the help and supervision of Olivia Delorme, I was able to understand the creative and "
        "technical requirements of eyewear design, as well as the diverse but very specific production methods that it employs."),
    "luca-desk": ("Luca Desk", 2024,
        "Evolutive desk that can grow from 50 cm desk height to 55 cm and 60 cm, following the child's first school years.\n"
        "Design for Cam Cam Copenhagen."),
    "cykelparkering": ("Cykelparkering", 2023,
        "This project is the result of the observation of the many different bike parking stations spread among "
        "Copenhagen. It gave me the opportunity to play with shapes and colours to create this series of tea towels."),
    "junior-cutlery": ("Junior Cutlery", 2023,
        "Colourful and ergonomic cutlery for children.\nDesign for Cam Cam Copenhagen."),
    "wooden-hooks": ("Wooden Hooks", 2023,
        "Colourful and playful wooden hooks for Cam Cam Copenhagen."),
    "3ps": ("3Ps", 2022,
        "3Ps is my master thesis project. This more academic work has been the occasion to explore the perception and "
        "opportunities offered by 3D printing technology as a production technique. The different items have been created "
        "after hearing the different participants of the project and explore some of the challenges brought by the "
        "technology (parametric modelling, printing time, design sturdiness, etc.)."),
    "sadji": ("Sadji", 2022,
        "Sadji is a set for people who make their own makeup.\n"
        "For each of the three different textures that can be obtained, corresponds a ceramic container: for creams, hard "
        "pastes and powders, for which a press comes along. Glass lids let the colours and textures be seen through. These "
        "different elements then lay on a ceramic board that can also hold brushes and other makeup. This project stands "
        "for a zero-waste lifestyle but also gives back value to the moment it is associated with: it is an invitation to "
        "take time for yourself as it used to be in older times."),
    "weever": ("Weever", 2021,
        "Weever is an autonomous weed remover coupled with a lawnmower. It was born out of SDU's Talent Programme in "
        "Entrepreneurship where our team (software engineer, robotic engineer and I as an industrial designer) met. Through "
        "this project we aim to work towards the automatisation of tedious tasks in our society to leave more time for self "
        "development for individuals. We also aim to create a sustainable product that can bring a positive impact to the "
        "environment: our robot will reduce the use of pesticides often chosen to save time and hard labor. Besides, we "
        "wish to design Weever according to Cradle to Cradle principles through a design for disassembly so that we can keep "
        "on recycling and reusing our technical materials and dispose in the best way of the components that reached their "
        "end of life. Weever is an ongoing project constantly evolving."),
    "nebulo-system": ("Nebulo System", 2019,
        "Nebulo System is a Swiss start-up that developed an alarm system which, instead of a sound, releases a thick fog "
        "preventing the burglar from entering the house. During the Innovation by Design challenge I worked with Fernando "
        "Riviero to develop a product around the knight figure that would fit in its environment with a strong identity. "
        "The materials we chose (ceramic and wood) give this product a warmer feeling."),
    "still-rolling": ("Still Rolling", 2019,
        "Still Rolling is a redesign of the walking frame. While the ageing population is becoming a major issue, this "
        "object, often stigmatized and neglected, offers a new dynamic so that the user can make it part of their identity."),
    "bbsimple": ("BBsimple", 2018,
        "The aim of the BBsimple babyphone is to make the parent-child relationship simple again. Therefore, it comes with "
        "a minimum of functionalities. Its ergonomic shape and the silicon's skin translate the softness and sweetness of "
        "the child's world as well as the bond with the parents."),
}


def gallery(slug: str) -> list[str]:
    folder = IMG / slug
    return [f"/work/{slug}/{p.name}" for p in sorted(folder.glob("[0-9]*.jpg"))]


def main() -> None:
    OUT.mkdir(exist_ok=True)
    for slug, (title, year, desc) in PROJECTS.items():
        first_sentence = desc.replace("\n", " ").split(". ")[0].rstrip(".") + "."
        summary = first_sentence.replace('"', "'")
        gal = "\n".join(f"  - {g}" for g in gallery(slug))
        body = "\n\n".join(desc.split("\n"))
        (OUT / f"{slug}.md").write_text(
            f"---\n"
            f"title: {title}\n"
            f"year: {year}\n"
            f'description: "{summary}"\n'
            f"cover: /work/{slug}/cover.jpg\n"
            f"gallery:\n{gal}\n"
            f"---\n\n"
            f"{body}\n",
            encoding="utf-8",
        )
        print(f"✓ work/{slug}.md ({len(gallery(slug))} gallery images)")


if __name__ == "__main__":
    main()
