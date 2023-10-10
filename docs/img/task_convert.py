from subprocess import run
from typing import Any

import pytask
from pathlib import Path

THIS_DIR = Path(__file__).parent

for f in THIS_DIR.glob("*.dxf"):
    fpdf = f.with_suffix(".pdf")


    @pytask.mark.task(id=f.stem)
    @pytask.mark.skipif(not fpdf.exists(), reason="printed PDF does not exist")
    @pytask.mark.depends_on(fpdf)
    @pytask.mark.produces([f.with_suffix(s) for s in [".svg", ".png"]])
    def task_convert_dxfs(depends_on: Path, produces: dict[Any, Path]):
        for p in produces.values():
            res = run(
                [
                    "inkscape", "-d", "600", "-o", str(p), str(depends_on)
                ]
            )
            res.check_returncode()


for f in map(Path, [
    "disk_element.svg",
    "disk_elements.svg",
    "directions-two-roll.svg",
    "directions-three-roll.svg",
    "pyroll-bird.svg",
    "pyroll-bird-head.svg",
    "pyroll-logo.svg",
    "unit.svg",
]):
    @pytask.mark.task(id=f.stem)
    @pytask.mark.depends_on(f)
    @pytask.mark.produces([f.with_suffix(s) for s in [".pdf", ".png"]])
    def task_convert_svg(depends_on: Path, produces: dict[Any, Path]):
        for p in produces.values():
            res = run(
                [
                    "inkscape", "-D", "-d", "600", "-o", str(p), str(depends_on)
                ]
            )
            res.check_returncode()