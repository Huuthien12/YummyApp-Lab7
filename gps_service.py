class GPSSignalLostError(Exception):
    """Ngoai le khi thiet bi mat tin hieu GPS."""


def get_current_location():
    """Mo phong toa do GPS; duoc mock trong kiem thu."""
    return (10.0, 105.0)
