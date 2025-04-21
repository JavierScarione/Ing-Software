from prompt_toolkit import PromptSession
from prompt_toolkit.history import InMemoryHistory
from openai import OpenAI

client = OpenAI()

# Creaando un historial para almacenar las consultas.
history = InMemoryHistory()
session = PromptSession(history=history)

while True:
    try:
        request = session.prompt("Hola, ingresa tu consulta (↑ para historial):\n> ")

        if request.strip() == "":
            print("Por favor, ingresa una consulta no vacía o válida. ")
            continue

        print("Tú: ", request)

        history.append_string(request)

        response = client.responses.create(
            model="gpt-4.1",
            input=request
        )

        print("ChatGPT: ", response.output_text)

    except (KeyboardInterrupt, EOFError):
        print("\n¡Hasta luego!, Me voy")
        break
    except Exception as e:
        print("Ocurrió un error:", str(e))

