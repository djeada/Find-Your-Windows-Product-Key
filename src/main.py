from src.gui import GuiWindow
from src.misc import which_windows_version, WindowsVersion
from src.product_key_decoder import Windows10ProductKeyDecoder, Windows8ProductKeyDecoder


def main():
    """
    Main function of the program.
    """
    windows_version_to_product_key_decoder = { WindowsVersion.WINDOWS_10: Windows10ProductKeyDecoder, WindowsVersion.WINDOWS_8: Windows8ProductKeyDecoder }

    windows_version = which_windows_version()

    if windows_version is None or windows_version not in windows_version_to_product_key_decoder:
        print('Windows version not supported')
        return
    
    product_key_decoder = windows_version_to_product_key_decoder[windows_version]()
    product_key = product_key_decoder.product_key()
    GuiWindow(product_key)


if __name__ == '__main__':
    main()
