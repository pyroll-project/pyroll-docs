import pyroll.core as pr

in_profile = pr.Profile.round(
    diameter=8e-3,
    flow_stress=100e6,
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
