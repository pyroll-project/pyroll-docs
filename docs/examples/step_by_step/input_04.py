import pyroll.core as pr
import pyroll.wusatowski_spreading
import pyroll.freiberg_flow_stress
import pyroll.hensel_power_and_labour

in_profile = pr.Profile.round(
    diameter=8e-3,
    material="S355J2",
    temperature=1000 + 273.15,
)

sequence = pr.PassSequence([
    pr.RollPass(
        roll=pr.Roll(
            groove=pr.CircularOvalGroove(
                r1=2e-3,
                r2=10e-3,
                depth=2e-3,
            ),
            nominal_radius=100e-3,
            rotational_frequency=1,
        ),
        gap=1e-3,
    ),
])
