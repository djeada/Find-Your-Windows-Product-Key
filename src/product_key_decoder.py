import winreg
import abc

from src.misc import str_to_int


class ProductKeyDecoder(abc.ABC):
    """
    Abstract class for product key decoder.
    """

    @abc.abstractmethod
    def product_key(self):
        """
        Returns the product key of the current Windows version.
        """
        pass

    @abc.abstractmethod
    def _decode_product_key(self):
        """
        Decodes the product key if the key was encoded.
        """
        pass


class Windows10ProductKeyDecoder(ProductKeyDecoder):
    """
    Implementation of the Windows 10 product key decoder.
    """

    def product_key(self):
        """
        Returns the product key of the current Windows version.
        """
        path = "SOFTWARE\Microsoft\Windows NT\CurrentVersion\SoftwareProtectionPlatform"
        value = "BackupProductKeyDefault"
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path)
        result, _ = winreg.QueryValueEx(key, value)
        return list(result)

    def _decode_product_key(self):
        """
        No need to decode the product key.
        """
        pass


class Windows8ProductKeyDecoder(ProductKeyDecoder):
    """
    Implementation of the Windows 8 product key decoder.
    """

    def product_key(self):
        """
        Returns the product key of the current Windows version.
        """
        path = "SOFTWARE\Microsoft\Windows NT\CurrentVersion"
        value = "DigitalProductID"
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path)
        result, type = winreg.QueryValueEx(key, value)
        return self._decode_product_key(list(result))

    def _decode_product_key(self, key):
        """
        Decodes the product key.
        """
        chars = "BCDFGHJKMPQRTVWXY2346789"
        result = ""
        offset = 52

        for i in range(24, -1, -1):
            temp = 0
            for j in range(14, -1, -1):
                temp *= 256
                temp += str_to_int(key[j + offset])
                if temp / 24 <= 255:
                    key[j + offset] = temp / 24
                else:
                    key[j + offset] = 255
                temp = int(temp % 24)
            result = chars[temp] + result

        for i in range(5, len(result), 6):
            result = result[:i] + "-" + result[i:]
        return result
