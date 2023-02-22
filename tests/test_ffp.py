from pyffp import calc_footprint_FFP as myfootprint

def test_ffp():
    FFP = myfootprint.FFP(
        zm=20.0,
        z0=0.1,
        h=2000.0,
        ol=-100.0,
        sigmav=0.6,
        ustar=0.4,
        wind_dir=30,
        rs=[20.0, 40.0, 60.0, 80.0],    
    )

    assert len(FFP) == 11
