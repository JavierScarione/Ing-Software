
"""
    Javier Scarione, Ingeniería de Software II, 2025

    “copyright UADER_FCyT_IS2 © 2022,2024 todos los derechos reservados"

    Este programa permite recuperar una clave desde un archivo JSON usando programación orientada a objetos. 
    Utilizando el patrón Singleton y una estrategia de "branching by abstraction" para facilitar refactorizaciones futuras.
"""

import json
import sys
from abc import ABC, abstractmethod

VERSION = "versión 1.1"


class JsonKeyRetrieverInterface(ABC):

    @abstractmethod
    def get_value(self, key):
        pass


class JsonKeyRetrieverSingleton(JsonKeyRetrieverInterface):

    _instance = None

    def __new__(cls, filepath):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialize(filepath)
        return cls._instance

    def _initialize(self, filepath):
        self.filepath = filepath
        self.data = self._load_json()

    def _load_json(self):
        try:
            with open(self.filepath, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            raise ValueError(f"Archivo no encontrado: '{self.filepath}'")
        except json.JSONDecodeError as err:
            raise ValueError(f"JSON inválido en '{self.filepath}': {err}") from err

    def get_value(self, key):
        try:
            return self.data[key]
        except KeyError as err:
            raise ValueError(f"Clave '{key}' no encontrada en el archivo JSON.") from err


def mostrar_version():
    print(VERSION)


def mostrar_uso():
    print(
        "Uso:\n"
        "  python getJason.py <archivo_json> [clave]\n"
        "  python getJason.py -v\n\n"
        "- <archivo_json>: Ruta al archivo JSON (obligatorio)\n"
        "- [clave]: Clave a recuperar (opcional, por defecto 'token1')"
    )


def main():
    args = sys.argv[1:]

    if not args:
        mostrar_uso()
        return

    if args[0] == "-v":
        mostrar_version()
        return

    if len(args) > 2:
        print("Error: Demasiados argumentos.")
        mostrar_uso()
        return

    json_file = args[0]
    json_key = args[1] if len(args) == 2 else "token1"

    try:
        retriever = JsonKeyRetrieverSingleton(json_file)
        value = retriever.get_value(json_key)
        print(value)
    except ValueError as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    main()