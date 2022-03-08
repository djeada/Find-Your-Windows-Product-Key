import enum

class WindowsVersion(enum.Enum):
    """
    All supported Windows versions.
    """
    WINDOWS_10 = enum.auto()
    WINDOWS_8 = enum.auto()
    WINDOWS_7 = enum.auto()
    WINDOWS_VISTA = enum.auto()
    WINDOWS_XP = enum.auto()
    WINDOWS_2000 = enum.auto()
    WINDOWS_NT = enum.auto()


def which_windows_version():
    """
    Determines the current Windows version.
    """
    import sys

    info = sys.getwindowsversion()

    info_to_windows_version = {WindowsVersion.WINDOWS_10: (10, 0), WindowsVersion.WINDOWS_8: (6, 2),
                               WindowsVersion.WINDOWS_7: (6, 1), WindowsVersion.WINDOWS_VISTA: (6, 0),
                               WindowsVersion.WINDOWS_XP: (5, 1), WindowsVersion.WINDOWS_2000: (5, 0),
                               WindowsVersion.WINDOWS_NT: (4, 0)}

    for windows_version, info_tuple in info_to_windows_version.items():
        if info.major == info_tuple[0] and info.minor == info_tuple[1]:
            return windows_version

    return None


def str_to_int(x):
    if isinstance(x, str):
        return ord(x)
    return x