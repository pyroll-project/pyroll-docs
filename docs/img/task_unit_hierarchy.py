from typing import Any

import pytask
from pathlib import Path
from schemdraw import Drawing
from schemdraw.flow import Box, Arrow, Line, Wire


@pytask.mark.task()
@pytask.mark.produces(f"unit_hierarchy.{e}" for e in ["png", "pdf", "svg"])
def task_unit_hierarchy(produces: dict[Any, Path]):
    d = Drawing()

    d.add(
        unit := Box().label("Unit").drop("S")
    )
    d.add(
        Arrow().reverse().down().length(0.4 * d.unit).label("+disk elements", loc="B")
    )
    d.add(
        disk_element_unit := Box(w=5).label("DiskElementUnit")
    )

    d.add(
        roll_pass := Box().label("RollPass").anchor("E").at(disk_element_unit.S, -2 * d.unit, -0.5 * d.unit)
    )
    d.add(
        Wire("|-", arrow="<-").to(roll_pass.E).at(disk_element_unit.S, -0.2).label("+deformation, roll contact")
    )

    d.add(
        Arrow().down().label("+third roll", loc="B").at(roll_pass.S).reverse()
    )
    d.add(
        Box(w=4).label("ThreeRollPass")
    )

    d.add(
        transport := Box().label("Transport").anchor("W").at(disk_element_unit.S, 2 * d.unit, -0.5 * d.unit)
    )
    d.add(
        Wire("|-", arrow="<-").to(transport.W).at(disk_element_unit.S, 0.2).label("+atmosphere contact")
    )

    d.move_from(transport.S)
    d.push()

    def down_left_box(label, add, w=3, a=False):
        d.pop()
        d.add(
            Line(arrow="<-" if a else "").down().length(0.8 * d.unit)
        )
        d.push()
        d.add(
            Line().left().label(f"+{add}", loc="B").length(1.5 * d.unit)
        )
        d.add(
            Box(w=w).label(label)
        )

    down_left_box("Furnace", "wall", a=True)
    down_left_box("CoolingRange", "cooling water,\nair stream", w=4)
    down_left_box("InductionHeater", "induction", w=5)
    down_left_box("Descaler", "pressure water")

    d.add(
        rotator := Box().label("Rotator").at((roll_pass.N.x, unit.W.y)).anchor("center")
    )

    d.add(
        Arrow().at(rotator.E).to(unit.W).label("+rotation")
    )

    d.add(
        Line(arrow="-o").at(roll_pass.N).to(rotator.S).label("uses")
    )

    d.add(
        disk_element := Box(w=4).label("DiskElement").at((transport.N.x, unit.E.y)).anchor("center")
    )

    d.add(
        Arrow().at(disk_element.W).to(unit.E)
    )

    d.add(
        Wire(shape="-|", arrow="-o").at(disk_element_unit.E).to(disk_element.S).label("uses")
    )

    for f in produces.values():
        d.save(f.__str__(), dpi=600)
