import hashlib
class Criptografia:

    @staticmethod
    def criptografar_string(texto):
        """
        Criptografa uma string usando SHA-256.

        Args:
            texto: A string a ser criptografada.

        Returns:
            A string criptografada (hash).
        """
        # Codifica a string para bytes, pois o hashlib trabalha com bytes
        texto_bytes = texto.encode('utf-8')
        # Gera o hash SHA-256
        hash_object = hashlib.sha256(texto_bytes)
        # Retorna o hash em formato hexadecimal
        return hash_object.hexdigest()