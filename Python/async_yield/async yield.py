import asyncio
#
# async def generator_coroutine():
#     for i in range(3):
#         await asyncio.sleep(1)
#         yield 100
#
# async def main():
#     async for value in generator_coroutine():
#         print(value)
#
# asyncio.run(main())

# Exemple concret : Afficher des messages au fur et à mesure qu’ils arrivent, comme dans WhatsApp ou Discord.
async def recevoir_messages():
    messages = [
        "Salut !",
        "Tu fais quoi ?",
        "Tu connais asyncio ?",
        "C'est super puissant 😄"
    ]

    for msg in messages:
        await asyncio.sleep(2)  # simulateur de délai réseau
        yield msg #envoie le message dès qu’il arrive

async def main():
    async for message in recevoir_messages(): #lit les messages en temps réel
        print("Nouveau message :", message)

asyncio.run(main())