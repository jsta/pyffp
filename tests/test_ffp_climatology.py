from pyffp import calc_footprint_FFP_climatology as myfootprint

def test_ffp_climatology():
    zmt = 20.0
    z0t = 0.01
    ht = [2000.0, 1800.0, 1500.0]
    olt = [-10.0, -100.0, -500.0]
    sigmavt = [
        0.9,
        0.7,
        0.3,
    ]
    ustart = [0.5, 0.3, 0.4]
    wind_dirt = [30.0, 50.0, 70.0]
    domaint = [-100.0, 1000.0, -100.0, 1000.0]
    nxt = 1100
    rst = [20.0, 40.0, 60.0, 80.0]

    FFP = myfootprint.FFP_climatology(
        zm=zmt,
        z0=z0t,
        umean=None,
        h=ht,
        ol=olt,
        sigmav=sigmavt,
        ustar=ustart,
        wind_dir=wind_dirt,
        domain=domaint,
        nx=nxt,
        rs=rst,
        smooth_data=1
    )

    # [k for k in FFP.keys()]
    assert len(FFP) == 9
