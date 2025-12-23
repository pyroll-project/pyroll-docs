from pathlib import Path
from subprocess import run

THIS_DIR = Path(__file__).parent

for f in THIS_DIR.glob("*.dxf"):
    fpdf = f.with_suffix(".pdf")


    def task_convert_dxfs(depends_on=fpdf, produces=[f.with_suffix(s) for s in [".svg", ".png"]]):
        for p in produces:
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

    def task_convert_svg(depends_on=f, produces=[f.with_suffix(s) for s in [".pdf", ".png"]]):
        for p in produces:
            res = run(
                [
                    "inkscape", "-D", "-d", "600", "-o", str(p), str(depends_on)
                ]
            )
            res.check_returncode()
